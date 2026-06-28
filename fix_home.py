import re

with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

# 1. Remove the standalone 100vh sizing from .calculator-shell in HOME
# Find width:100%; height:100dvh; min-height:100vh;
html = html.replace('width:100%; height:100dvh; min-height:100vh; overflow-y:auto; overflow-x:hidden; -webkit-overflow-scrolling:touch; padding:env(safe-area-inset-top, 40px) 20px env(safe-area-inset-bottom, 40px) 20px;', 'margin:16px; border-radius:18px; padding:16px; border:1.5px solid rgba(120,85,55,.2);')

# 2. Remove the calc-top-bar (which has the "Salir" button from the standalone version)
# We want to remove this block:
# <div class="calc-top-bar">
#    <button class="calc-close-btn" onclick="alert(...)">Salir</button>
# </div>
top_bar_pattern = re.compile(r'<div class="calc-top-bar">.*?</div>', re.DOTALL)
html = top_bar_pattern.sub('', html)

# 3. Ensure the HOME calc close button uses the right CSS. The HOME calc close button is outside the shell.
# It uses class="calc-close" which is already defined in HOME CSS.

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(html)

print("Fixed standalone remnants.")
