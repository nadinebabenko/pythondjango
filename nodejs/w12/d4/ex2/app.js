const express = require('express');
const app = express();

const books = [
    { id: 1, title: 'Book 1', author: 'Author 1', publishedYear: 2021 },
    { id: 2, title: 'Book 2', author: 'Author 2', publishedYear: 2022 },
    { id: 3, title: 'Book 3', author: 'Author 3', publishedYear: 2023 }
  ];

  app.listen(5000, () => {
    console.log('Server is running on port 5000');
  });
  app.get('/api/books/:bookId', (req, res) => {
    const bookId = parseInt(req.params.bookId);
    const book = books.find(b => b.id === bookId);
    if (book) {
      res.json(book);
    } else {
      res.status(404).send('Book not found');
    }
  });
  
  app.post('/api/books', (req, res) => {
 
  });