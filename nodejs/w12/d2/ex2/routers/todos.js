const todos = [];

const express = require('express');
const router = express.Router();

// Get all to-do items
router.get('/', (req, res) => {
  res.send(todos);
});

// Add a new to-do item
router.post('/', (req, res) => {
  const todo = req.body;
  todos.push(todo);
  res.send(todo);
});

// Update a to-do item by ID
router.put('/:id', (req, res) => {
  const id = req.params.id;
  const todo = req.body;
  todos[id] = todo;
  res.send(todo);
});

// Delete a to-do item by ID
router.delete('/:id', (req, res) => {
  const id = req.params.id;
  todos.splice(id, 1);
  res.send('Todo deleted');
});

module.exports = router;