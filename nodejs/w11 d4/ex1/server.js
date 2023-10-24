const express = require('express');
const app = express();
const port = 3000;

// Simulated database
let data = [
  { id: 1, title: 'First Post', content: 'This is the first blog post.' },
  { id: 2, title: 'Second Post', content: 'This is the second blog post.' },
  { id: 3, title: 'Third Post', content: 'This is the third blog post.' }
];

app.use(express.json());

app.get('/posts', (req, res) => {
    res.send(data);
  });

app.get('/posts/:id', (req, res) => {
    const id = parseInt(req.params.id);
    const post = data.find(post => post.id === id);
    if (post) {
      res.send(post);
    } else {
      res.status(404).send('Post not found');
    }
  });

  app.post('/posts', (req, res) => {
    const post = req.body;
    post.id = data.length + 1;
    data.push(post);
    res.send(post);
  });

  app.put('/posts/:id', (req, res) => {
    const id = parseInt(req.params.id);
    const post = data.find(post => post.id === id);
    if (post) {
      post.title = req.body.title;
      post.content = req.body.content;
      res.send(post);
    } else {
      res.status(404).send('Post not found');
    }
  });

  app.delete('/posts/:id', (req, res) => {
    const id = parseInt(req.params.id);
    const index = data.findIndex(post => post.id === id);
    if (index !== -1) {
      data.splice(index, 1);
      res.send(`Post ${id} deleted`);
    } else {
      res.status(404).send('Post not found');
    }
  });

  app.use((req, res) => {
    res.status(404).send('Invalid route');
  });

  app.use((err, req, res, next) => {
    console.error(err.stack);
    res.status(500).send('Server error');
  });

  app.listen(port, () => {
    console.log(`Server listening on port ${port}`);
  });