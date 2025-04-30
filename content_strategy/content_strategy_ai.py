import requests
import json

# Fetch trends from Reddit API (Your API is expected to be running at localhost:3000)
def fetch_reddit_trends():
    url = 'http://localhost:3000/trends/realtime'  # Assuming you're running the Node.js server
    try:
        response = requests.get(url)
        response.raise_for_status()  # Raise an error for bad responses (4xx or 5xx)
        return response.json()  # Return the trend data in JSON format
    except requests.exceptions.RequestException as e:
        print(f"Error fetching trends: {e}")
        return []

# Categorize the fetched trends into specific categories
def categorize_trends(trends):
    categories = {
        'technology': [],
        'gaming': [],
        'fitness': [],
        'cooking': [],
        'AI': []
    }

    # Let's assume 'title' is the main focus of each trend
    for trend in trends:
        title = trend.get('title', '').lower()
        if 'AI' in title:
            categories['AI'].append(trend)
        elif 'gaming' in title:
            categories['gaming'].append(trend)
        elif 'fitness' in title:
            categories['fitness'].append(trend)
        elif 'cooking' in title:
            categories['cooking'].append(trend)
        elif 'technology' in title:
            categories['technology'].append(trend)

    return categories

# Function to generate script content based on the trend
def generate_script(trend):
    title = trend.get('title', 'No Title')
    description = trend.get('description', 'No description available.')

    # Basic script generation
    script = f"""
    Title: {title}

    Introduction: In today's trending topic, we discuss {title}.

    Main Body: {description}

    Conclusion: What are the key takeaways from {title}?
    """
    return script

# Main function to integrate everything (fetching, categorizing, and generating content)
def main():
    print("🔍 Fetching Reddit trends...")
    trends = fetch_reddit_trends()

    if trends:
        print(f"Found {len(trends)} trends. Categorizing them...")
        categorized_trends = categorize_trends(trends)
        
        # Save categorized trends to a file for reference
        with open('categorized_trends.json', 'w') as f:
            json.dump(categorized_trends, f, indent=4)

        print("📂 Trends saved to 'categorized_trends.json'.")
        
        # Trigger content creation (generate scripts for each category)
        print("📝 Generating scripts for relevant trends...")
        
        for category, relevant_trends in categorized_trends.items():
            print(f"\n🎬 Generating scripts for category: {category}")
            for trend in relevant_trends:
                script_content = generate_script(trend)  # Generate script from the trend
                print(f"Generated script for: {trend['title']}")
                # Here you could save the script or pass it to another AI agent for further processing
                # For example, save_script_to_database(script_content)  # Optional step to store scripts
                # Or directly pass it on to another AI component

    else:
        print("No trends found.")

if __name__ == '__main__':
    main()
