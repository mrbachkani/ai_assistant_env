import requests
import pandas as pd

def fetch_reddit_trends():
    try:
        print("🔍 Fetching trending posts from Reddit...")
        r = requests.get('http://localhost:3000/trends/realtime')
        r.raise_for_status()
        raw = r.json()
        return raw
    except Exception as e:
        print(f"❌ Failed to fetch Reddit trends: {e}")
        return []

def clean_trends(raw_trends):
    if not raw_trends:
        return []

    cleaned = []
    for post in raw_trends:
        cleaned.append({
            "title": post.get("title", "N/A"),
            "subreddit": post.get("subreddit", "N/A"),
            "score": post.get("score", 0),
            "comments": post.get("num_comments", 0),
            "url": post.get("url", "")
        })
    return cleaned

def save_trends_to_csv(trends, filename="reddit_trends.csv"):
    if not trends:
        print("⚠️ No trends to save.")
        return

    df = pd.DataFrame(trends)
    df.to_csv(filename, index=False)
    print(f"✅ Saved {len(df)} trends to {filename}")

if __name__ == "__main__":
    raw_trends = fetch_reddit_trends()
    cleaned_trends = clean_trends(raw_trends)
    save_trends_to_csv(cleaned_trends)
