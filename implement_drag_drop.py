import re

with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

# 1. Update renderCalDayItems
old_render_items = '''function renderCalDayItems(key,mini){
  const items=calVisibleItems(key).slice(0,mini?2:3);
  if(!items.length)return '';
  return `<div class="cal-note">${items.map(it=>{const color=CAL_COLORS[it.color]||CAL_COLORS.none;const photos=calItemPhotoIds(it).length;return `<div class="cal-note-line ${it.done?'done':''}"><span class="cal-note-box" style="background:${color.bg};border-color:${color.dot}"></span><span class="cal-note-text">${esc(it.text)||(photos?`📷 ${photos} foto${photos===1?'':'s'}`:'')}</span></div>`;}).join('')}</div>`;
}'''

new_render_items = '''function renderCalDayItems(key,mini){
  const items=calVisibleItems(key).slice(0,mini?2:3);
  if(!items.length)return '';
  return `<div class="cal-note">${items.map(it=>{
    const color=CAL_COLORS[it.color]||CAL_COLORS.none;
    const photos=calItemPhotoIds(it).length;
    return `<div class="cal-note-line ${it.done?'done':''}" data-cal-key="${key}" data-item-id="${it.id}" style="touch-action:none; cursor:grab;" onpointerdown="startCalItemDrag(event)"><span class="cal-note-box" style="background:${color.bg};border-color:${color.dot}"></span><span class="cal-note-text">${esc(it.text)||(photos?`📷 ${photos} foto${photos===1?'':'s'}`:'')}</span></div>`;
  }).join('')}</div>`;
}'''
html = html.replace(old_render_items, new_render_items)


# 2. Update renderMonthGrid to include data-cal-key
old_cal_day = '''    h+=`<div class="cal-day${weekend?' weekend':''}${muted?' muted':''}${sameDay(date,today)?' today':''}${hasColor?' has-color':''}" ${style} ${click}><div>${d}</div>${note?`${renderCalDayItems(key,mini)}<div class="cal-dot" style="background:${color.dot}"></div>`:''}</div>`;'''
new_cal_day = '''    h+=`<div class="cal-day${weekend?' weekend':''}${muted?' muted':''}${sameDay(date,today)?' today':''}${hasColor?' has-color':''}" data-cal-key="${key}" ${style} ${click}><div>${d}</div>${note?`${renderCalDayItems(key,mini)}<div class="cal-dot" style="background:${color.dot}"></div>`:''}</div>`;'''
html = html.replace(old_cal_day, new_cal_day)


# 3. Inject JS Logic
js_drag_logic = '''
// ── CALENDAR DRAG & DROP ──
let DRAG_CAL_ITEM = null;
function startCalItemDrag(e) {
  // Solo arrastrar si es pulsación simple (botón primario o táctil)
  if(e.button !== 0 && e.pointerType === 'mouse') return;
  e.stopPropagation(); // Evitar que el clic abra la nota si estamos arrastrando
  
  const el = e.currentTarget;
  const key = el.getAttribute('data-cal-key');
  const id = el.getAttribute('data-item-id');
  if(!key || !id) return;
  
  // Create clone
  const rect = el.getBoundingClientRect();
  const clone = el.cloneNode(true);
  clone.classList.add('cal-item-clone');
  clone.style.width = rect.width + 'px';
  clone.style.height = rect.height + 'px';
  clone.style.left = rect.left + 'px';
  clone.style.top = rect.top + 'px';
  document.body.appendChild(clone);
  
  el.style.opacity = '0.2'; // Mute original
  
  DRAG_CAL_ITEM = {
    sourceKey: key,
    itemId: id,
    originalEl: el,
    clone: clone,
    offsetX: e.clientX - rect.left,
    offsetY: e.clientY - rect.top,
    lastHover: null,
    isDragging: false // we will set true if moved
  };
  
  document.addEventListener('pointermove', moveCalItemDrag, {passive: false});
  document.addEventListener('pointerup', endCalItemDrag);
}

function moveCalItemDrag(e) {
  if(!DRAG_CAL_ITEM) return;
  e.preventDefault(); // Evitar scroll
  DRAG_CAL_ITEM.isDragging = true;
  
  // Move clone
  DRAG_CAL_ITEM.clone.style.left = (e.clientX - DRAG_CAL_ITEM.offsetX) + 'px';
  DRAG_CAL_ITEM.clone.style.top = (e.clientY - DRAG_CAL_ITEM.offsetY) + 'px';
  
  // Find element under pointer
  DRAG_CAL_ITEM.clone.style.display = 'none';
  const target = document.elementFromPoint(e.clientX, e.clientY);
  DRAG_CAL_ITEM.clone.style.display = '';
  
  const calDay = target ? target.closest('.cal-day') : null;
  const targetKey = calDay ? calDay.getAttribute('data-cal-key') : null;
  
  // Update hover classes
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
  
  const { sourceKey, itemId, originalEl, clone, lastHover, isDragging } = DRAG_CAL_ITEM;
  DRAG_CAL_ITEM = null;
  
  clone.remove();
  originalEl.style.opacity = '';
  if(lastHover) lastHover.classList.remove('drag-over');
  
  // If we just clicked (didn't drag), let it open the note
  if(!isDragging) {
    openCalNote(sourceKey);
    return;
  }
  
  const targetKey = lastHover ? lastHover.getAttribute('data-cal-key') : null;
  if(targetKey && targetKey !== sourceKey) {
    // Perform the move in data
    const sourceItems = getCalItems(sourceKey);
    const targetItems = getCalItems(targetKey);
    const idx = sourceItems.findIndex(it => it.id === itemId);
    if(idx !== -1) {
      const itemToMove = sourceItems.splice(idx, 1)[0];
      targetItems.push(itemToMove); // add to end of target day
      
      // Save
      const saveItems = (k, list) => {
        const textItems = list;
        const activeText = textItems.filter(it=>!it.done).map(it=>it.text).join('\\n');
        const allText = textItems.map(it=>(it.done?'✓ ':'')+it.text).join('\\n');
        if(list.length) lsSet(calItemsKey(k), JSON.stringify(list)); else lsRemove(calItemsKey(k));
        if(allText) lsSet('cal_'+k, activeText||allText); else lsRemove('cal_'+k);
        // color is preserved per day, not transferring day color.
      };
      
      saveItems(sourceKey, sourceItems);
      saveItems(targetKey, targetItems);
      lsSet('h_updated', String(Date.now()));
      scheduleCloudSave();
      
      renderHomeGrid();
    }
  }
}
'''
html = html.replace('// ── CLOUD SYNC & FIREBASE ──', js_drag_logic + '\n// ── CLOUD SYNC & FIREBASE ──')

# 4. Inject CSS
css_drag = '''
.cal-item-clone {
  position: fixed;
  z-index: 99999;
  pointer-events: none;
  background: rgba(255, 255, 255, 0.95);
  box-shadow: 0 8px 24px rgba(80, 40, 10, 0.2);
  border-radius: 6px;
  padding: 4px;
  transform: scale(1.1);
  opacity: 0.95;
}
.cal-day.drag-over {
  background: rgba(255, 200, 150, 0.6) !important;
  box-shadow: inset 0 0 0 2px #d05828 !important;
  transform: scale(1.02);
}
'''
html = html.replace('/* ── SCREEN 2: LEVELS ── */', css_drag + '\n/* ── SCREEN 2: LEVELS ── */')

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(html)

print("Drag and Drop implemented!")
