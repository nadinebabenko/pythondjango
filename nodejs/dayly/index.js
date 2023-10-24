const express = require('express');
const bcrypt = require('bcrypt');
const bodyParser = require('body-parser');
const fs = require('fs');
const bcrypt = require('bcrypt');

const app = express();
app.use(express.json());
const saltRounds = 10;
const usersFile = 'users.json';

app.use(bodyParser.json());

// POST /register
app.post('/register', (req, res) => {
  const { username, password } = req.body;
  const saltRounds = 10;
  bcrypt.hash(password, saltRounds, (err, hash) => {
    if (err) {
      console.error(err);
      res.status(500).send('Internal server error');
    } else {
      const users = JSON.parse(fs.readFileSync('users.json'));
      users.push({ username, password: hash });
      fs.writeFileSync('users.json', JSON.stringify(users));
      res.send('User registered successfully');
    }
  });
});
bcrypt.hash(password, 10, (err, hash) => {
  if (err) {
    return res.status(500).send('Error hashing password');
  }
  const user = { id: users.length + 1, username, password: hash };
  users.push(user);
  saveUsers(users);
  res.send(`User ${username} registered successfully`);
});

// POST /login
app.post('/login', (req, res) => {
  const { username, password } = req.body;
  const users = JSON.parse(fs.readFileSync('users.json'));
  const user = users.find(user => user.username === username);
  if (user) {
    bcrypt.compare(password, user.password, (err, result) => {
      if (err) {
        console.error(err);
        res.status(500).send('Internal server error');
      } else if (result) {
        res.send('Login successful');
      } else {
        res.status(401).send('Incorrect password');
      }
    });
  } else {
    res.status(401).send('User not found');
  }
});
bcrypt.compare(password, user.password, (err, result) => {
  if (err) {
    return res.status(500).send('Error comparing passwords');
  }
  if (!result) {
    return res.status(401).send('Invalid username or password');
  }
  res.send(`User ${username} logged in successfully`);
});

// GET /users
app.get('/users', (req, res) => {
  const users = JSON.parse(fs.readFileSync('users.json'));
  res.send(users);
});

// GET /users/:id
app.get('/users/:id', (req, res) => {
  const users = JSON.parse(fs.readFileSync('users.json'));
  const user = users.find(user => user.id === req.params.id);
  if (user) {
    res.send(user);
  } else {
    res.status(404).send('User not found');
  }
});

// PUT /users/:id
app.put('/users/:id', (req, res) => {
  const users = JSON.parse(fs.readFileSync('users.json'));
  const userIndex = users.findIndex(user => user.id === req.params.id);
  if (userIndex !== -1) {
    users[userIndex] = { ...users[userIndex], ...req.body };
    fs.writeFileSync('users.json', JSON.stringify(users));
    res.send('User updated successfully');
  } else {
    res.status(404).send('User not found');
  }
});

app.listen(5000, () => {
  console.log('Server started on port 5000');
});