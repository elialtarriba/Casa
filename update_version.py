import re
with open('index.html', 'r') as f:
    html = f.read()

version_html = '<div style="position:fixed; bottom:12px; left:0; width:100%; text-align:center; font-size:11px; font-weight:800; color:rgba(80,40,10,0.35); pointer-events:none; z-index:9000;">v61</div>\n</body>'
html = re.sub(r'</body>', version_html, html)

with open('index.html', 'w') as f:
    f.write(html)
