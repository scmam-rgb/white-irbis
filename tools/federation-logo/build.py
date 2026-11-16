import numpy as np
from PIL import Image
from skimage import measure, filters
src=Image.open('/mnt/user-data/attachments/c930c61e-808f-5364-bb79-14eac62f56de/7c9d7624-image.png').convert('RGBA').crop((0,18,117,121))
c=Image.new('RGB',src.size,(255,255,255));c.paste(src,(0,0),src)
CX,CY,R=59.5,68.5,24.6
S=16
x0,y0=int(CX-R-2),int(CY-R-2);x1,y1=int(CX+R+3),int(CY+R+3)
crop=c.crop((x0,y0,x1,y1)).resize(((x1-x0)*S,(y1-y0)*S),Image.BICUBIC)
a=np.asarray(crop.convert('L'),dtype=float)/255
a=filters.gaussian(a,sigma=S*0.35)
dark=(a<0.45).astype(float)
yy,xx=np.mgrid[0:a.shape[0],0:a.shape[1]]
px=x0+(xx+0.5)/S;py=y0+(yy+0.5)/S
d=np.hypot(px-CX,py-CY)
dark[d>R-0.9]=0
dark=filters.gaussian(dark,sigma=S*0.12)
cs=measure.find_contours(dark,0.5)
paths=[]
for ct in cs:
  ct=measure.approximate_polygon(ct,tolerance=S*0.08)
  if len(ct)<4:continue
  pts=' '.join(f'{x0+p[1]/S:.2f},{y0+p[0]/S:.2f}' for p in ct)
  paths.append('M'+pts+'Z')
med=f'<path fill="#111" fill-rule="evenodd" d="{" ".join(paths)}"/>'
open('med.txt','w').write(med)
print(len(paths))
