import re

with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

# Replace logo.png with icon.png in the head
html = html.replace('href="logo.png"', 'href="icon.png"')
html = html.replace('"src":"logo.png"', '"src":"icon.png"')

# Change name to HOME in manifest
html = html.replace('"name":"Hogar"', '"name":"HOME"')
html = html.replace('"short_name":"Hogar"', '"short_name":"HOME"')

# Add apple-mobile-web-app-title if it doesn't exist
if 'apple-mobile-web-app-title' not in html:
    html = html.replace('<meta name="apple-mobile-web-app-capable" content="yes">', '<meta name="apple-mobile-web-app-capable" content="yes">\n<meta name="apple-mobile-web-app-title" content="HOME">')

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(html)
