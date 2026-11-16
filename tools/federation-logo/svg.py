import math
med=open('med.txt').read()
A=(59.5,0.6);BL=(0.8,102.2);BR=(118.2,102.2)
IA=(59.5,11.8);IL=(17.6,94.2);IR=(101.4,94.2)
def lerp(p,q,t):return (p[0]+(q[0]-p[0])*t,p[1]+(q[1]-p[1])*t)
def xat(y,side):  # x on inner triangle edge
  t=(y-IA[1])/(IL[1]-IA[1]);return IA[0]+(IL[0]-IA[0])*t if side<0 else IA[0]+(IR[0]-IA[0])*t
ys=64.5
xl,xr=xat(ys,-1),xat(ys,1)
# snowcap jagged
yc=26.5;sl,sr=xat(yc,-1),xat(yc,1)
jag=[(sl,yc),(sl+2.2,yc-1.2),(sl+3.2,yc+1.2),(sl+4.6,yc-0.6),(sl+5.6,yc+1.8),(sl+7.0,yc-0.4),(sl+8.2,yc+1.4),(sl+9.6,yc-0.8),(sl+10.8,yc+1.0),(sl+12.0,yc-1.0),(sr,yc)]
P=lambda pts:' '.join(f'{x:.2f},{y:.2f}' for x,y in pts)
F="font-family:'TeX Gyre Adventor';font-weight:700"
# left text baseline: parallel to inner-left edge, offset outward
def off(p,q,d):
  dx,dy=q[0]-p[0],q[1]-p[1];L=math.hypot(dx,dy);nx,ny=dy/L,-dx/L
  return (p[0]+nx*d,p[1]+ny*d),(q[0]+nx*d,q[1]+ny*d)
lb=off(IL,IA,1.6)   # outward normal to the left (for IL->IA direction, normal (dy,-dx) points left/outward)
rb=off(IA,IR,1.6)
svg=f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="-1 -1 120 105" width="1200" height="1050">
<defs><path id="lp" d="M{lb[0][0]:.2f},{lb[0][1]:.2f} L{lb[1][0]:.2f},{lb[1][1]:.2f}"/><path id="rp" d="M{rb[0][0]:.2f},{rb[0][1]:.2f} L{rb[1][0]:.2f},{rb[1][1]:.2f}"/></defs>
<polygon points="{P([A,BL,BR])}" fill="#fff" stroke="#111" stroke-width="1.1" stroke-linejoin="miter"/>
<polygon points="{P([IA,(xl,ys),(xr,ys)])}" fill="#0072b8"/>
<polygon points="{P([(xl,ys),IL,(59.5,94.2),(59.5,ys)])}" fill="#da251c"/>
<polygon points="{P([(59.5,ys),(59.5,94.2),IR,(xr,ys)])}" fill="#f9c001"/>
<polygon points="{P([IA]+jag)}" fill="#fff" stroke="#111" stroke-width=".45" stroke-linejoin="round"/>
<polygon points="{P([IA,IL,IR])}" fill="none" stroke="#111" stroke-width=".8"/>
<line x1="{BL[0]+5}" y1="94.6" x2="{BR[0]-5}" y2="94.6" stroke="#111" stroke-width=".8"/>
<polygon points="59.5,4.2 56.6,9.6 62.4,9.6" fill="#111"/>
<polygon points="3.4,100.4 9.6,100.4 6.5,95.0" fill="#111"/>
<polygon points="109.4,100.4 115.6,100.4 112.5,95.0" fill="#111"/>
<circle cx="59.5" cy="68.5" r="24.4" fill="#fff" stroke="#111" stroke-width=".9"/>
<circle cx="59.5" cy="68.5" r="17.6" fill="none" stroke="#111" stroke-width=".5"/>
{med}
<text style="{F};font-size:9px" fill="#111" stroke="#111" stroke-width=".55" stroke-linejoin="round"><textPath href="#lp" startOffset="50%" text-anchor="middle" textLength="76" lengthAdjust="spacing">ARMENIAN</textPath></text>
<text style="{F};font-size:9px" fill="#111" stroke="#111" stroke-width=".55" stroke-linejoin="round"><textPath href="#rp" startOffset="50%" text-anchor="middle" textLength="80" lengthAdjust="spacing">FEDERATION</textPath></text>
<text x="59.5" y="99.9" text-anchor="middle" style="{F};font-size:4.6px" textLength="90" lengthAdjust="spacingAndGlyphs" fill="#111" stroke="#111" stroke-width=".28">MOUNTAINEERING &amp; HIKING</text>
</svg>'''
open('fed.svg','w').write(svg)
open('fed.html','w').write('<html><body style="margin:0;background:transparent">'+svg+'</body></html>')
