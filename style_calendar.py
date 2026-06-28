import re

with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

# 1. Remove inline styles from home-calendar-container
html = html.replace(
    '<div class="houses-grid" id="home-calendar-container" style="display:flex; flex-direction:column; padding:0; height:100%;"></div>',
    '<div class="houses-grid" id="home-calendar-container"></div>'
)

# 2. Add specific CSS for home-calendar-container
calendar_css = '''
#home-calendar-container {
  flex: 1;
  min-height: 0;
  margin: 12px 20px 80px 20px;
  padding: 16px;
  background: rgba(255, 255, 255, 0.45);
  backdrop-filter: blur(14px);
  -webkit-backdrop-filter: blur(14px);
  border: 2px solid rgba(255, 255, 255, 0.85);
  border-radius: 26px;
  box-shadow: 0 16px 40px rgba(80, 40, 10, 0.1), inset 0 2px 0 rgba(255, 255, 255, 0.9);
  display: flex;
  flex-direction: column;
  overflow-y: auto;
}
'''

# Find a good place to inject the CSS. Right before `/* ── SCREEN 2: LEVELS ── */` or just append to `<style>`
html = html.replace('/* ── SCREEN 2: LEVELS ── */', calendar_css + '\n/* ── SCREEN 2: LEVELS ── */')

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(html)
