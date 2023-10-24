const express = require('express');
const router = express.Router();

// Sample in-memory database for storing books
const books = [];

// Get all books
router.get('/', (req, res) => {
  res.send(books);
});

// Add a new book
router.post('/', (req, res) => {
  const book = req.body;
  books.push(book);
  res.send('Book added successfully');
});

// Update a book by ID
router.put('/:id', (req, res) => {
  const id = req.params.id;
  const newBook = req.body;
  books[id] = newBook;
  res.send(`Book with ID ${id} has been updated`);
});

// Delete a book by ID
router.delete('/:id', (req, res) => {
  const id = req.params.id;
  books.splice(id, 1);
  res.send(`Book with ID ${id} has been deleted`);
});

module.exports = router;