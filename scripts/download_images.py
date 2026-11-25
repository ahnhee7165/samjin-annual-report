"""img_urls.json 의 메타 소재 이미지를 img/{creative_id}.jpg 로 내려받습니다.
메타 이미지 주소는 임시 주소라 받은 뒤 며칠 지나면 만료됩니다."""
import json, os, sys, urllib.request
urls = json.load(open("img_urls.json", encoding="utf-8"))
os.makedirs("img", exist_ok=True)
ok = fail = 0
for cid, url in urls.items():
    path = f"img/{cid}.jpg"
    if os.path.exists(path) and os.path.getsize(path) > 0:
        ok += 1; continue
    try:
        req = urllib.request.Request(url, headers={"User-Agent": "Mozilla/5.0"})
        with urllib.request.urlopen(req, timeout=30) as r, open(path, "wb") as f:
            f.write(r.read())
        ok += 1
    except Exception as e:
        fail += 1; print("실패", cid, e, file=sys.stderr)
print(f"완료 {ok}개 / 실패 {fail}개")
