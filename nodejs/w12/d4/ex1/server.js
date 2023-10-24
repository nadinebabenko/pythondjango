const express = require('express');
const app = express();


const { Pool } = require('pg');
const pool = new Pool({
  user: 'your_user',
  host: 'your_host',
  database: 'your_database',
  password: 'your_password',
  port: 5432,
});

pool.query('CREATE TABLE IF NOT EXISTS posts (id SERIAL PRIMARY KEY, title VARCHAR(255), content TEXT)');

app.get('/posts', async (req, res) => {
  try {
    const result = await pool.query('SELECT * FROM posts');
    res.send(result.rows);
  } catch (err) {
    console.error(err);
    res.status(500).send('Server Error');
  }
});


app.get('/posts/:id', async (req, res) => {
  try {
    const result = await pool.query('SELECT * FROM posts WHERE id = $1', [req.params.id]);
    if (result.rows.length === 0) {
      res.status(404).send('Post not found');
    } else {
      res.send(result.rows[0]);
    }
  } catch (err) {
    console.error(err);
    res.status(500).send('Server Error');
  }
});


app.post('/posts', async (req, res) => {
  try {
    const { title, content } = req.body;
    const result = await pool.query('INSERT INTO posts (title, content) VALUES ($1, $2) RETURNING *', [title, content]);
    res.send(result.rows[0]);
  } catch (err) {
    console.error(err);
    res.status(500).send('Server Error');
  }
});


app.put('/posts/:id', async (req, res) => {
  try {
    const { title, content } = req.body;
    const result = await pool.query('UPDATE posts SET title = $1, content = $2 WHERE id = $3 RETURNING *', [title, content, req.params.id]);
    if (result.rows.length === 0) {
      res.status(404).send('Post not found');
    } else {
      res.send(result.rows[0]);
    }
  } catch (err) {
    console.error(err);
    res.status(500).send('Server Error');
  }
});


app.delete('/posts/:id', async (req, res) => {
  try {
    const result = await pool.query('DELETE FROM posts WHERE id = $1 RETURNING *', [req.params.id]);
    if (result.rows.length === 0) {
      res.status(404).send('Post not found');
    } else {
      res.send(result.rows[0]);
    }
  } catch (err) {
    console.error(err);
    res.status(500).send('Server Error');
  }
});


app.use((req, res) => {
  res.status(404).send('Invalid Route');
});

app.use((err, req, res, next) => {
  console.error(err);
  res.status(500).send('Server Error');
});


const port = 5000;
app.listen(port, () => {
  console.log(`Server started on port ${port}`);
});