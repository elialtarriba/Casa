import re

with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

# 1. Update Grid
html = html.replace(
    '.home-title-row{display:grid;grid-template-columns:76px minmax(0,1fr) auto;align-items:center;gap:12px}',
    '.home-title-row{display:grid;grid-template-columns:76px minmax(0,1fr) 76px;align-items:center;gap:12px}'
)
html = html.replace(
    '.home-title-row{grid-template-columns:62px minmax(0,1fr) 44px;gap:9px}',
    '.home-title-row{grid-template-columns:62px minmax(0,1fr) 62px;gap:9px}'
)

# 2. Update CSS for .home-calc-btn to remove old styles since we will just reuse brand-face logic
# Or we can just remove .home-calc-btn entirely and style the button inline, but let's just make a new class .home-calc-icon
html = re.sub(r'\.home-title-row \.home-calc-btn\{.*?\}', '', html)
html = re.sub(r'\.home-title-row \.home-calc-btn::before\{.*?\}', '', html)

# 3. Replace the button HTML in s-home
old_btn = '<button class="home-calc-btn" onclick="openCalc()" title="Calculadora">🧮 Calculadora</button>'
new_btn = '''<button class="brand-flip" style="perspective:none;" type="button" onclick="openCalc()" title="Calculadora">
          <span class="brand-flip-inner" style="transition: transform 0.1s;">
            <span class="brand-face" style="position:relative;"><img src="iconocalcu.png" alt="Calculadora" style="width:100%;height:100%;object-fit:cover;display:block;"></span>
          </span>
        </button>'''
html = html.replace(old_btn, new_btn)

# Add active scale effect so it feels like a button
html = html.replace(
    '.brand-flip.flipped:active .brand-flip-inner{transform:rotateY(180deg) scale(.95)}',
    '.brand-flip.flipped:active .brand-flip-inner{transform:rotateY(180deg) scale(.95)}\n.brand-flip:active .brand-flip-inner{transform:scale(.95)}'
)

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(html)
