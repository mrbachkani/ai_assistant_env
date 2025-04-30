from googleapiclient.discovery import build

# Set up YouTube API
YOUTUBE_API_KEY = 'AIzaSyDwhck7ttmt81nDsUdhCUaDigHGoUXmQnI'  # Replace with your actual API Key
youtube = build('youtube', 'v3', developerKey=YOUTUBE_API_KEY)

# Fetch trending videos
def fetch_trending_videos():
    request = youtube.videos().list(
        part="snippet,contentDetails,statistics",
        chart="mostPopular",
        regionCode="US",  # You can change to your region
        maxResults=10
    )
    response = request.execute()

    trending_videos = []
    for item in response['items']:
        title = item['snippet']['title']
        description = item['snippet']['description']
        video_url = f"https://www.youtube.com/watch?v={item['id']}"
        trending_videos.append({
            "title": title,
            "description": description,
            "url": video_url
        })
    return trending_videos

# Get and print trending videos
if __name__ == "__main__":
    trending_videos = fetch_trending_videos()
    for video in trending_videos:
        print(f"Title: {video['title']}")
        print(f"Description: {video['description']}")
        print(f"URL: {video['url']}")
        print("-" * 50)
