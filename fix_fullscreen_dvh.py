import re

with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

old_css = '''  height: 100% !important;
  background: #f5ead8 !important;
  padding: calc(16px + env(safe-area-inset-top)) 16px 16px 16px !important;'''

new_css = '''  height: 100dvh !important;
  background: #f5ead8 !important;
  padding: calc(16px + env(safe-area-inset-top)) 16px calc(16px + env(safe-area-inset-bottom)) 16px !important;'''

html = html.replace(old_css, new_css)
html = html.replace('V6</div>', 'V7</div>')

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(html)
