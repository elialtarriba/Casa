import json
import re

with open('../CALCULADORA/index.html', 'r', encoding='utf-8') as f:
    calc_html = f.read()

with open('index.html', 'r', encoding='utf-8') as f:
    home_html = f.read()

# Extract CSS from CALCULADORA
css_start = calc_html.find('.calculator-shell{')
css_end = calc_html.find('</style>', css_start)
new_css = calc_html[css_start:css_end].strip()

# Extract HTML from CALCULADORA
html_start = calc_html.find('<div class="calculator-shell"')
html_end = calc_html.find('<script>', html_start)
new_html = calc_html[html_start:html_end].strip()

# Extract JS from CALCULADORA
# Since we know it's between the first <script> and </script>
js_start = calc_html.find('<script>', html_end) + len('<script>')
js_end = calc_html.find('</script>', js_start)
new_js = calc_html[js_start:js_end].strip()

# Now inject into HOME
# 1. CSS
h_css_start = home_html.find('.calculator-shell{--calc-accent:')
# Find the end of the calculator CSS block in HOME.
# It ends right before @media(max-width:430px){.calculator-shell
h_css_end = home_html.find('@media(max-width:430px){.calculator-shell', h_css_start)
if h_css_start != -1 and h_css_end != -1:
    home_html = home_html[:h_css_start] + new_css + '\n' + home_html[h_css_end:]
else:
    print("Could not find CSS boundaries in HOME")

# 2. HTML
h_html_start = home_html.find('<div class="calculator-shell" id="calculator-shell">')
# Find the end of the calculator HTML block in HOME.
# It ends with </div></div></div><!-- Firebase
h_html_end = home_html.find('<!-- Firebase', h_html_start)
# Backtrack to keep the closing divs of calc-dialog and calc-ov.
# In HOME:
# <div class="calc-dialog">
#   <div class="calc-header">...</div>
#   <div class="calculator-shell">...</div>
# </div>
# </div>
# <!-- Firebase
# We want to replace `<div class="calculator-shell">...</div>`
# So we need to find the `</div>` that closes `calculator-shell`.
# In HOME, calculator-shell closes at `</div>` before `</div>\n</div>\n\n<!-- Firebase`
search_str = '</div>\n  </div>\n</div>\n\n<!-- Firebase'
h_html_end_exact = home_html.find(search_str, h_html_start)
if h_html_start != -1 and h_html_end_exact != -1:
    home_html = home_html[:h_html_start] + new_html + '\n  ' + home_html[h_html_end_exact + 6:]
else:
    print("Could not find HTML boundaries in HOME")

# 3. JS
# In HOME, JS starts at `let CALC_CURRENT='0'`
h_js_start = home_html.find("let CALC_CURRENT='0'")
# Ends at the end of `toggleCalcPercentTool`
h_js_end_func = home_html.find('function toggleCalcPercentTool(tool){', h_js_start)
h_js_end = home_html.find('}\n', h_js_end_func) + 2
if h_js_start != -1 and h_js_end != -1:
    home_html = home_html[:h_js_start] + new_js + '\n' + home_html[h_js_end:]
else:
    print("Could not find JS boundaries in HOME")

# 4. Buttons
home_html = home_html.replace("onclick=\"window.location.href='../calculadora/'\"", "onclick=\"openCalc()\"")

with open('index_new.html', 'w', encoding='utf-8') as f:
    f.write(home_html)

print("Python script executed successfully.")
