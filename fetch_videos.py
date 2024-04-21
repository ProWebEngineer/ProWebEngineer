import requests
import os

# 環境変数からAPIキーを取得
api_key = os.getenv('YOUTUBE_API_KEY')
channel_id = 'UCGq2Y94R8nXkJw0m2YFO4fA'
url = f"https://www.googleapis.com/youtube/v3/search?key={api_key}&channelId={channel_id}&part=snippet&order=date&maxResults=5"

response = requests.get(url)
videos = response.json()

# Markdownファイルに書き込むHTMLコードを生成
html_content = '<p>\n'
for video in videos['items']:
    video_id = video['id']['videoId']
    title = video['snippet']['title']
    thumbnail_url = video['snippet']['thumbnails']['medium']['url']
    video_link = f"https://www.youtube.com/watch?v={video_id}"
    html_content += f'  <a href="{video_link}">\n'
    html_content += f'    <img src="{thumbnail_url}" alt="{title}" style="width: 160px; height: auto; margin-right: 10px;">\n'
    html_content += '  </a>\n'
html_content += '</p>\n'

# HTMLコンテンツをファイルに書き込み
with open('latest-videos.md', 'w') as file:
    file.write(html_content)
