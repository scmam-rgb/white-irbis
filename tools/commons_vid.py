import json, os, re, time, urllib.parse, urllib.request
UA={"User-Agent":"WhiteIrbisSiteBuilder/1.0 (antuanvisit@gmail.com)"}
def get(u):
    with urllib.request.urlopen(urllib.request.Request(u,headers=UA),timeout=120) as r: return r.read()
os.makedirs("vcand",exist_ok=True); meta={}
for line in open("tools/vqueries.txt",encoding="utf-8"):
    line=line.strip()
    if not line: continue
    key,q=line.split("|",1)
    api="https://commons.wikimedia.org/w/api.php?"+urllib.parse.urlencode({"action":"query","generator":"search","gsrsearch":q+" filetype:video","gsrnamespace":6,"gsrlimit":8,"prop":"imageinfo","iiprop":"url|size|extmetadata|mediatype","iiextmetadatafilter":"Artist|LicenseShortName","format":"json"})
    try: d=json.loads(get(api))
    except Exception as e: print("ERR",key,e); continue
    for i,p in enumerate(sorted(d.get("query",{}).get("pages",{}).values(),key=lambda p:p.get("index",99))):
        ii=p["imageinfo"][0]; em=ii.get("extmetadata",{})
        if ii.get("size",0)>120e6: continue
        n=f"{key}_{i}"+os.path.splitext(ii["url"])[1].lower()
        try: open("vcand/"+n,"wb").write(get(ii["url"]))
        except Exception as e: print("ERR",n,e); continue
        meta[n]={"title":p["title"],"page":ii.get("descriptionurl"),"w":ii.get("width"),"h":ii.get("height"),"dur":ii.get("duration"),
                 "artist":re.sub("<[^>]+>","",em.get("Artist",{}).get("value","")).strip(),"license":em.get("LicenseShortName",{}).get("value","")}
        time.sleep(0.5)
json.dump(meta,open("vcand/meta.json","w"),ensure_ascii=False,indent=1); print(len(meta))
