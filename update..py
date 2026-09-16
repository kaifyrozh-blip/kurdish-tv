import requests

SOURCE_URL = "https://raw.githubusercontent.com/kurdishiptvchannels/KURDISTANIPTV/refs/heads/main/KURDISTAN%20IPTV.m3u"

try:
  response = requests.get(SOURCE_URL)
  if response.status_code == 200:
    with open("playlist.m3u", "w", encoding="utf-8") as f:
      f.write(response.text)
    print("Playlist updated successfully!")
  else:
    print("Error downloading:", response.status_code)
except Exception as e:
  print("Error:", e)
