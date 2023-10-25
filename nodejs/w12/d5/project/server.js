const express = require('express');
const bodyParser = require('body-parser');
const cors = require('cors');
const axios = require('axios');
const Parser = require('rss-parser');
const parser = new Parser();
 
const app = express();
app.use(bodyParser.urlencoded({ extended: false }));
app.use(bodyParser.json());
app.use(cors());

app.get('/', async (req, res) => {
  try {
    const feed = await parser.parseURL('https://thefactfile.org/feed/');
    res.render('pages/index', { posts: feed.items });
  } catch (err) {
    console.error(err);
    res.status(500).send('Error fetching RSS feed');
  }
});
app.get('/search', (req, res) => {
  res.render('pages/search');
});
app.post('/search/title', async (req, res) => {
  try {
    const feed = await parser.parseURL('https://thefactfile.org/feed/');
    const title = req.body.title;
    const post = feed.items.find(item => item.title === title);
    res.render('pages/search', { post });
  } catch (err) {
    console.error(err);
    res.status(500).send('Error fetching RSS feed');
  }
});
app.post('/search/category', async (req, res) => {
  try {
    const feed = await parser.parseURL('https://thefactfile.org/feed/');
    const category = req.body.category;
    const posts = feed.items.filter(item => item.categories.includes(category));
    res.render('pages/search', { posts });
  } catch (err) {
    console.error(err);
    res.status(500).send('Error fetching RSS feed');
  }
});

const PORT = process.env.PORT || 3000;
app.listen(PORT, () => {
  console.log(`Server listening on port ${PORT}`);
});