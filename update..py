import urllib.request

url = "https://raw.githubusercontent.com/kurdishiptvchannels/KURDISTANIPTV/refs/heads/main/KURDISTAN%20IPTV.m3u"

try:
  req = urllib.request.Request(url, headers={"User-Agent": "Mozilla/5.0"})
  with urllib.request.urlopen(req) as response:
    content = response.read().decode("utf-8")
    with open("playlist.m3u", "w", encoding="utf-8") as f:
      f.write(content)
  print("Updated successfully!")
except Exception as e:
  print("Error:", e)
