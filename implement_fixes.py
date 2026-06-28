import re

with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

# --- 1. JS Drag Logic ---
js_drag_logic = '''
// ── CALENDAR DRAG & DROP ──
let DRAG_CAL_ITEM = null;
function startCalItemDrag(e) {
  if(e.button !== 0 && e.pointerType === 'mouse') return;
  e.stopPropagation();
  
  const el = e.currentTarget;
  const key = el.getAttribute('data-cal-key');
  const id = el.getAttribute('data-item-id');
  if(!key || !id) return;
  
  const rect = el.getBoundingClientRect();
  const clone = el.cloneNode(true);
  clone.classList.add('cal-item-clone');
  clone.style.width = rect.width + 'px';
  clone.style.height = rect.height + 'px';
  clone.style.left = rect.left + 'px';
  clone.style.top = rect.top + 'px';
  document.body.appendChild(clone);
  
  el.style.opacity = '0.2';
  
  DRAG_CAL_ITEM = { sourceKey: key, itemId: id, originalEl: el, clone: clone, offsetX: e.clientX - rect.left, offsetY: e.clientY - rect.top, lastHover: null, isDragging: false, fromModal: false };
  
  document.addEventListener('pointermove', moveCalItemDrag, {passive: false});
  document.addEventListener('pointerup', endCalItemDrag);
}

function startModalItemDrag(e, id) {
  if(e.button !== 0 && e.pointerType === 'mouse') return;
  e.stopPropagation();
  const el = e.currentTarget.closest('.cal-line');
  if(!el) return;
  
  const rect = el.getBoundingClientRect();
  const clone = el.cloneNode(true);
  clone.classList.add('cal-item-clone');
  clone.style.width = rect.width + 'px';
  clone.style.height = rect.height + 'px';
  clone.style.left = rect.left + 'px';
  clone.style.top = rect.top + 'px';
  document.body.appendChild(clone);
  
  // Close the modal visually without wiping memory
  document.getElementById('cal-note-ov').classList.remove('open');
  
  DRAG_CAL_ITEM = { sourceKey: CAL_NOTE_DAY, itemId: id, originalEl: el, clone: clone, offsetX: e.clientX - rect.left, offsetY: e.clientY - rect.top, lastHover: null, isDragging: true, fromModal: true };
  
  document.addEventListener('pointermove', moveCalItemDrag, {passive: false});
  document.addEventListener('pointerup', endCalItemDrag);
}

function moveCalItemDrag(e) {
  if(!DRAG_CAL_ITEM) return;
  e.preventDefault();
  DRAG_CAL_ITEM.isDragging = true;
  
  DRAG_CAL_ITEM.clone.style.left = (e.clientX - DRAG_CAL_ITEM.offsetX) + 'px';
  DRAG_CAL_ITEM.clone.style.top = (e.clientY - DRAG_CAL_ITEM.offsetY) + 'px';
  
  DRAG_CAL_ITEM.clone.style.display = 'none';
  const target = document.elementFromPoint(e.clientX, e.clientY);
  DRAG_CAL_ITEM.clone.style.display = '';
  
  const calDay = target ? target.closest('.cal-day') : null;
  const targetKey = calDay ? calDay.getAttribute('data-cal-key') : null;
  
  if(DRAG_CAL_ITEM.lastHover && DRAG_CAL_ITEM.lastHover !== calDay) {
    DRAG_CAL_ITEM.lastHover.classList.remove('drag-over');
  }
  if(calDay && targetKey !== DRAG_CAL_ITEM.sourceKey) {
    calDay.classList.add('drag-over');
    DRAG_CAL_ITEM.lastHover = calDay;
  } else {
    DRAG_CAL_ITEM.lastHover = null;
  }
}

function endCalItemDrag(e) {
  if(!DRAG_CAL_ITEM) return;
  document.removeEventListener('pointermove', moveCalItemDrag);
  document.removeEventListener('pointerup', endCalItemDrag);
  
  const { sourceKey, itemId, originalEl, clone, lastHover, isDragging, fromModal } = DRAG_CAL_ITEM;
  DRAG_CAL_ITEM = null;
  
  clone.remove();
  if(originalEl) originalEl.style.opacity = '';
  if(lastHover) lastHover.classList.remove('drag-over');
  
  if(!isDragging && !fromModal) {
    openCalNote(sourceKey);
    return;
  }
  
  const targetKey = lastHover ? lastHover.getAttribute('data-cal-key') : null;
  
  if(targetKey && targetKey !== sourceKey) {
    // Valid drop on a different day!
    // Since fromModal modifies current editing, we use getCalItems to pull fresh from storage if not from modal, or we use CAL_NOTE_ITEMS if from modal?
    // Wait, if we are fromModal, CAL_NOTE_ITEMS was already saved on every edit! So getCalItems(sourceKey) is fresh.
    const sourceItems = getCalItems(sourceKey);
    const targetItems = getCalItems(targetKey);
    const idx = sourceItems.findIndex(it => it.id === itemId);
    if(idx !== -1) {
      const itemToMove = sourceItems.splice(idx, 1)[0];
      targetItems.push(itemToMove);
      
      const saveItems = (k, list) => {
        const textItems = list;
        const activeText = textItems.filter(it=>!it.done).map(it=>it.text).join('\\n');
        const allText = textItems.map(it=>(it.done?'✓ ':'')+it.text).join('\\n');
        if(list.length) lsSet(calItemsKey(k), JSON.stringify(list)); else lsRemove(calItemsKey(k));
        if(allText) lsSet('cal_'+k, activeText||allText); else lsRemove('cal_'+k);
      };
      
      saveItems(sourceKey, sourceItems);
      saveItems(targetKey, targetItems);
      lsSet('h_updated', String(Date.now()));
      scheduleCloudSave();
      
      // If we moved it, we don't reopen the modal. 
      renderHomeGrid();
      return;
    }
  }
  
  // If we didn't drop it on a new day AND it came from the modal, reopen the modal!
  if(fromModal) {
    document.getElementById('cal-note-ov').classList.add('open');
  }
}
'''
if 'function startCalItemDrag' not in html:
    html = html.replace('// ── PDF EXPORT ──', js_drag_logic + '\n// ── PDF EXPORT ──')

# --- 2. Fix Header Calculator Button ---
html = html.replace(
    '<button class="brand-flip" style="perspective:none;" type="button" onclick="openCalc()" title="Calculadora">',
    '<button class="brand-flip" style="perspective:none; grid-column: 3; align-self: center;" type="button" onclick="openCalc()" title="Calculadora">'
)


# --- 3. Fix Calendar Height CSS ---
html = html.replace(
    '.cal-card{grid-column:1/-1;background:rgba(255,255,255,.64);border:1.5px solid rgba(160,100,50,.12);border-radius:16px;padding:12px;box-shadow:0 4px 16px rgba(0,0,0,.08)}',
    '.cal-card{grid-column:1/-1;background:rgba(255,255,255,.64);border:1.5px solid rgba(160,100,50,.12);border-radius:16px;padding:12px;box-shadow:0 4px 16px rgba(0,0,0,.08); display:flex; flex-direction:column; flex:1; min-height:0; height:100%;}'
)
html = html.replace(
    '.cal-week,.cal-grid{display:grid;grid-template-columns:repeat(7,minmax(0,1fr));gap:5px}',
    '.cal-week{display:grid;grid-template-columns:repeat(7,minmax(0,1fr));gap:5px; flex-shrink: 0;} .cal-grid{display:grid;grid-template-columns:repeat(7,minmax(0,1fr));gap:5px; flex:1;}'
)
html = html.replace(
    '.year-grid{grid-template-columns:1fr}',
    '.year-grid{grid-template-columns:1fr; flex:1;}'
)


# --- 4. Modal Drag UI ---
html = html.replace(
    '.cal-line{display:grid;grid-template-columns:32px 26px minmax(0,1fr) 32px 30px;gap:7px;align-items:center}',
    '.cal-line{display:grid;grid-template-columns:24px 32px 26px minmax(0,1fr) 32px 30px;gap:7px;align-items:center}'
)

old_cal_line_html = '''return `<div class="cal-line ${it.done?'done':''}" data-id="${it.id}">
      <button class="cal-check'''
new_cal_line_html = '''return `<div class="cal-line ${it.done?'done':''}" data-id="${it.id}">
      <button class="cal-drag-handle" style="cursor:grab; background:transparent; border:none; padding:0; display:flex; align-items:center; justify-content:center; color:rgba(80,40,10,0.4); touch-action:none; font-size:24px;" onpointerdown="${real?`startModalItemDrag(event, '${it.id}')`:'addCalLine()'}" title="Arrastrar para mover de día">≡</button>
      <button class="cal-check'''
html = html.replace(old_cal_line_html, new_cal_line_html)


with open('index.html', 'w', encoding='utf-8') as f:
    f.write(html)
