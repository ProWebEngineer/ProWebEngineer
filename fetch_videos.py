import requests
import os

api_key = os.getenv('YOUTUBE_API_KEY')
channel_id = 'UCGq2Y94R8nXkJw0m2YFO4fA'
url = f"https://www.googleapis.com/youtube/v3/search?key={api_key}&channelId={channel_id}&part=snippet&order=date&maxResults=5"

response = requests.get(url)
videos = response.json()
print('videos', videos)

with open('latest-videos.md', 'w') as file:
    for video in videos['items']:
        video_id = video['id']['videoId']
        title = video['snippet']['title']
        thumbnail_url = video['snippet']['thumbnails']['medium']['url']
        file.write(f"![{title}]({thumbnail_url})\n")
        file.write(f"[{title}](https://www.youtube.com/watch?v={video_id})\n\n")
