import re

with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

old_header = '''      <div class="home-title-row">
        <button class="brand-flip" type="button" onclick="showHomeScreen()" aria-label="Volver">
          <span class="brand-flip-inner" style="transform:none; border:none; box-shadow:none; background:transparent;">
            <span class="brand-face brand-front" style="font-size:32px; font-weight:bold; display:flex; align-items:center; justify-content:center; color:#573722; background:transparent; border:none; box-shadow:none;">‹</span>
          </span>
        </button>
        <div>
          <div class="home-title">Mis Casas</div>
        </div>
      </div>'''

# We want a button similar to pill or back-btn, but let's style it explicitly to match height
new_header = '''      <div style="display:flex; justify-content:space-between; align-items:center;">
        <button onclick="showHomeScreen()" style="height:44px; padding:0 20px; background:rgba(255,255,255,0.7); border:1.5px solid rgba(160,100,50,0.2); border-radius:22px; font-size:14px; font-weight:800; color:rgba(80,40,10,0.6); box-shadow:0 4px 14px rgba(160,90,40,0.14); backdrop-filter:blur(8px); cursor:pointer; display:flex; align-items:center; justify-content:center; white-space:nowrap;">INICIO</button>
        <div class="home-title" style="margin:0; text-align:right; font-size:28px; line-height:44px; height:44px;">Mis Casas</div>
      </div>'''

html = html.replace(old_header, new_header)

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(html)
