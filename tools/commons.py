import json, os, re, sys, time, urllib.parse, urllib.request
UA = {"User-Agent": "WhiteIrbisSiteBuilder/1.0 (antuanvisit@gmail.com)"}
def get(url):
    req = urllib.request.Request(url, headers=UA)
    with urllib.request.urlopen(req, timeout=60) as r:
        return r.read()
os.makedirs("cand", exist_ok=True)
meta = {}
for line in open("tools/queries.txt", encoding="utf-8"):
    line = line.strip()
    if not line or line.startswith("#"): continue
    key, q = line.split("|", 1)
    api = "https://commons.wikimedia.org/w/api.php?" + urllib.parse.urlencode({
        "action": "query", "generator": "search", "gsrsearch": q + " filetype:bitmap",
        "gsrnamespace": 6, "gsrlimit": 8, "prop": "imageinfo",
        "iiprop": "url|size|extmetadata", "iiextmetadatafilter": "Artist|LicenseShortName|ImageDescription",
        "iiurlwidth": 1400, "format": "json"})
    try:
        data = json.loads(get(api))
    except Exception as e:
        print("ERR", key, e); continue
    pages = sorted(data.get("query", {}).get("pages", {}).values(), key=lambda p: p.get("index", 99))
    for i, p in enumerate(pages):
        ii = p["imageinfo"][0]
        em = ii.get("extmetadata", {})
        name = f"{key}_{i}.jpg"
        try:
            open(os.path.join("cand", name), "wb").write(get(ii["thumburl"]))
        except Exception as e:
            print("ERR img", name, e); continue
        meta[name] = {"title": p["title"], "page": ii.get("descriptionurl"), "w": ii.get("width"), "h": ii.get("height"),
                      "artist": re.sub("<[^>]+>", "", em.get("Artist", {}).get("value", "")).strip(),
                      "license": em.get("LicenseShortName", {}).get("value", ""),
                      "desc": re.sub("<[^>]+>", "", em.get("ImageDescription", {}).get("value", ""))[:200]}
        time.sleep(0.5)
json.dump(meta, open("cand/meta.json", "w"), ensure_ascii=False, indent=1)
print(len(meta))
