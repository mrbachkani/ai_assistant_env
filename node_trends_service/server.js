const express = require('express');
const axios = require('axios');
const app = express();

// Trending subreddits from Reddit
app.get('/trends/realtime', async (req, res) => {
  try {
    const response = await axios.get('https://www.reddit.com/r/popular.json');
    const posts = response.data.data.children.map(post => ({
      title: post.data.title,
      subreddit: post.data.subreddit,
      url: post.data.url
    }));
    res.json(posts.slice(0, 10)); // Return top 10 trending posts
  } catch (err) {
    console.error('❌ Error fetching Reddit trends:', err.message);
    res.status(500).json({ error: 'Failed to fetch Reddit trends' });
  }
});

const PORT = 3000;
app.listen(PORT, () => console.log(`✅ Reddit Trends API running on http://localhost:${PORT}`));
