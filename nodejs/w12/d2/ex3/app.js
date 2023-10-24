const express = require('express');
const app = express();
const booksRouter = require('./routes/books');

app.use('/books', booksRouter);
app.get('/', (req, res) => {
  res.send('Hello Nadya!');
});

app.listen(5000, () => {
  console.log(' The  app listening on port 5000!');
});