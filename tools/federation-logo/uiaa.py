import re
fed=open('fed.svg').read()
inner=re.search(r'<svg[^>]*>(.*)</svg>',fed,re.S).group(1)
B='#0a93d8'
mtn="2,30 6,24.5 8,27 11.2,20.2 12.8,22.4 16.2,16 19.6,21.4 21.6,19.4 24.2,25.6 26.2,23.4 31,31 31,50 2,50"
u=f'''<g transform="translate(130,13) scale(1.45)">
<defs><clipPath id="uc"><circle cx="16.5" cy="31.5" r="13.6"/></clipPath></defs>
<circle cx="16.5" cy="31.5" r="13.6" fill="{B}"/>
<polygon points="{mtn}" fill="#fff" clip-path="url(#uc)"/>
<polygon points="17.4,10.6 15.4,18.2 19.6,18.2" fill="#fff"/>
<path d="M17.4,10.6 L15.6,17.4 M17.4,10.6 L19.4,17.4" stroke="{B}" stroke-width=".7" fill="none"/>
<circle cx="16.5" cy="31.5" r="14.6" fill="none" stroke="{B}" stroke-width="1.5"/>
<text x="36" y="42.6" style="font-family:'TeX Gyre Adventor';font-weight:700;font-size:28px" fill="{B}" stroke="{B}" stroke-width=".6" textLength="74" lengthAdjust="spacingAndGlyphs">UIAA</text>
</g>'''
svg=f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="-3 -3 298 110" width="1490" height="550">{inner}{u}</svg>'
open('combo.svg','w').write(svg)
open('combo.html','w').write('<html><body style="margin:0">'+svg+'</body></html>')
