const express = require('express');
const bcrypt = require('bcrypt');
const { Pool } = require('pg');

const router = express.Router();


const pool = new Pool({
    user: 'your_username',
    host: 'your_host',
    database: 'your_database',
    password: 'your_password',
    port: 5432,
  });

  router.post('/register', async (req, res) => {
    try {
      const { username, password } = req.body;
      const hashedPassword = await bcrypt.hash(password, 10);
      const client = await pool.connect();
      try {
        await client.query('BEGIN');
        const { rows } = await client.query('INSERT INTO users (username) VALUES ($1) RETURNING id', [username]);
        const userId = rows[0].id;
        await client.query('INSERT INTO hashpwd (username, password) VALUES ($1, $2)', [username, hashedPassword]);
        await client.query('COMMIT');
        res.status(201).json({ message: 'User created successfully', userId });
      } catch (error) {
        await client.query('ROLLBACK');
        throw error;
      } finally {
        client.release();
      }
    } catch (error) {
      console.error(error);
      res.status(500).json({ message: 'Internal server error' });
    }
  });
  
  router.post('/login', async (req, res) => {
    try {
      const { username, password } = req.body;
      const client = await pool.connect();
      try {
        const { rows } = await client.query('SELECT password FROM hashpwd WHERE username = $1', [username]);
        if (rows.length === 0) {
          res.status(401).json({ message: 'Invalid username or password' });
        } else {
          const hashedPassword = rows[0].password;
          const isMatch = await bcrypt.compare(password, hashedPassword);
          if (isMatch) {
            res.status(200).json({ message: 'Login successful' });
          } else {
            res.status(401).json({ message: 'Invalid username or password' });
          }
        }
      } finally {
        client.release();
      }
    } catch (error) {
      console.error(error);
      res.status(500).json({ message: 'Internal server error' });
    }
  });
  
  router.get('/users', async (req, res) => {
    try {
      const client = await pool.connect();
      try {
        const { rows } = await client.query('SELECT * FROM users');
        res.status(200).json(rows);
      } finally {
        client.release();
      }
    } catch (error) {
      console.error(error);
      res.status(500).json({ message: 'Internal server error' });
    }
  });
  
  router.get('/users/:id', async (req, res) => {
    try {
      const { id } = req.params;
      const client = await pool.connect();
      try {
        const { rows } = await client.query('SELECT * FROM users WHERE id = $1', [id]);
        if (rows.length === 0) {
          res.status(404).json({ message: 'User not found' });
        } else {
          res.status(200).json(rows[0]);
        }
      } finally {
        client.release();
      }
    } catch (error) {
      console.error(error);
      res.status(500).json({ message: 'Internal server error' });
    }
  });
  
  router.put('/users/:id', async (req, res) => {
    try {
      const { id } = req.params;
      const { email, username, first_name, last_name } = req.body;
      const client = await pool.connect();
      try {
        await client.query('UPDATE users SET email = $1, username = $2, first_name = $3, last_name = $4 WHERE id = $5', [email, username, first_name, last_name, id]);
        res.status(200).json({ message: 'User updated successfully' });
      } finally {
        client.release();
      }
    } catch (error) {
      console.error(error);
      res.status(500).json({ message: 'Internal server error' });
    }
  });


  module.exports = router;