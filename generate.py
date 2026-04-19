import requests

url = "https://pub-26bab83910ab4b5781549d12d2f0e6ff.r2.dev/thapcam.json"

data = requests.get(url).json()

m3u = "#EXTM3U\n"

for group in data.get("groups", []):
for ch in group.get("channels", []):
name = ch.get("name", "No Name")

```
    for source in ch.get("sources", []):
        for content in source.get("contents", []):
            for stream in content.get("streams", []):
                for link in stream.get("stream_links", []):
                    if link.get("default"):
                        m3u += f"#EXTINF:-1,{name}\n"
                        m3u += "#EXTVLCOPT:http-referrer=https://thapcamtvbc.mobi/\n"
                        m3u += "#EXTVLCOPT:http-user-agent=Mozilla/5.0\n"
                        m3u += link.get("url") + "\n\n"
```

with open("thapcam.m3u", "w", encoding="utf-8") as f:
f.write(m3u)
