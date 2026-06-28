import re

with open('../CALCULADORA/index.html', 'r', encoding='utf-8') as f:
    calc_html = f.read()

with open('index.html', 'r', encoding='utf-8') as f:
    home_html = f.read()

# EXTRACT NEW STUFF
# CSS
css_start = calc_html.find('.calculator-shell{')
css_end = calc_html.find('</style>', css_start)
new_css = calc_html[css_start:css_end].strip()
new_css = new_css.replace('width:100%; height:100dvh; min-height:100vh; overflow-y:auto; overflow-x:hidden; -webkit-overflow-scrolling:touch; padding:env(safe-area-inset-top, 40px) 20px env(safe-area-inset-bottom, 40px) 20px;', 'margin:16px; border-radius:18px; padding:16px; border:1.5px solid rgba(120,85,55,.2);')

# HTML
html_start = calc_html.find('<div class="calculator-shell"')
html_end = calc_html.find('<script>', html_start)
new_html = calc_html[html_start:html_end].strip()
new_html = re.sub(r'<div class="calc-top-bar">.*?</div>', '', new_html, flags=re.DOTALL)

# JS
js_start = calc_html.find('<script>', html_end) + len('<script>')
js_end = calc_html.find('</script>', js_start)
new_js = calc_html[js_start:js_end].strip()
# The new JS doesn't contain openCalc() or closeCalc()! We need to inject them.
open_close_js = """
function openCalc(){
  const palette=document.getElementById('calculator-palette');
  CALC_SOUND=lsGet('hogar_calc_sound')!=='0';
  if(palette&&!palette.innerHTML)palette.innerHTML=CALCULATOR_THEMES.map((theme,index)=>`<button class="calc-color" title="${theme.name}" style="background:linear-gradient(135deg,${theme.accent},${theme.display},${theme.opBottom})" onclick="setCalculatorTheme(CALCULATOR_THEMES[${index}])" oncontextmenu="if(typeof handleLongPressTheme==='function') { event.preventDefault(); handleLongPressTheme(CALCULATOR_THEMES[${index}], event); }"></button>`).join('');
  try{
    const modDefs = JSON.parse(lsGet('hogar_calc_modified_defaults') || '{}');
    Object.keys(modDefs).forEach(k => { if (CALCULATOR_THEMES[k]) Object.assign(CALCULATOR_THEMES[k], modDefs[k]); });
    const saved=JSON.parse(lsGet('hogar_calc_theme')||'null');
    if(saved)setCalculatorTheme(saved);
    else setCalculatorTheme(CALCULATOR_THEMES[0]);
  }catch(e){}
  
  // Attach event handlers for the calculator-grid if needed, but the new HTML has inline onclicks for calc-key!
  // So we only need to open the overlay.
  updateCalc();
  document.getElementById('calc-ov').classList.add('open');
}
function closeCalc(){document.getElementById('calc-ov').classList.remove('open');}
"""
new_js += '\n' + open_close_js

# INJECT INTO HOME
# 1. Replace CSS
h_css_start = home_html.find('.calculator-shell{--calc-accent:')
h_css_end = home_html.find('@media(max-width:430px){.calculator-shell', h_css_start)
if h_css_start != -1 and h_css_end != -1:
    home_html = home_html[:h_css_start] + new_css + '\n' + home_html[h_css_end:]

# 2. Replace HTML
h_html_start = home_html.find('<div class="calculator-shell" id="calculator-shell">')
h_html_end = home_html.find('</div>\n  </div>\n</div>\n\n<!-- Firebase', h_html_start)
if h_html_start != -1 and h_html_end != -1:
    home_html = home_html[:h_html_start] + new_html + '\n  ' + home_html[h_html_end:]

# 3. Replace JS
h_js_start = home_html.find('// ── CALCULATOR ──')
h_js_end = home_html.find('// ── PDF EXPORT ──', h_js_start)
if h_js_start != -1 and h_js_end != -1:
    home_html = home_html[:h_js_start] + '// ── CALCULATOR ──\n' + new_js + '\n\n' + home_html[h_js_end:]

# Update the v1.0 position per user request: "la V1 ponlo en la parte de abajo, en la parte derecha"
home_html = home_html.replace('bottom:12px; left:0; width:100%; text-align:center;', 'bottom:12px; right:12px; text-align:right;')

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(home_html)

print("Migration applied successfully.")
