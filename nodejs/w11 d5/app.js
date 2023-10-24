const express = require('express');
const fs = require('fs');
const app = express();
const router = express.Router();

// Middleware
app.use(express.json());

// Routes
router.get('/tasks', (req, res) => {
  fs.readFile('tasks.json', 'utf8', (err, data) => {
    if (err) {
      console.error(err);
      return res.status(500).send('Error reading tasks file');
    }
    const tasks = JSON.parse(data);
    res.send(tasks);
  });
});

router.get('/tasks/:id', (req, res) => {
  const taskId = req.params.id;
  fs.readFile('tasks.json', 'utf8', (err, data) => {
    if (err) {
      console.error(err);
      return res.status(500).send('Error reading tasks file');
    }
    const tasks = JSON.parse(data);
    const task = tasks.find(t => t.id === taskId);
    if (!task) {
      return res.status(404).send('Task not found');
    }
    res.send(task);
  });
});

router.post('/tasks', (req, res) => {
  const task = req.body;
  if (!task.title || !task.description) {
    return res.status(400).send('Title and description are required');
  }
  fs.readFile('tasks.json', 'utf8', (err, data) => {
    if (err) {
      console.error(err);
      return res.status(500).send('Error reading tasks file');
    }
    const tasks = JSON.parse(data);
    const newTask = { ...task, id: Date.now().toString() };
    tasks.push(newTask);
    fs.writeFile('tasks.json', JSON.stringify(tasks), err => {
      if (err) {
        console.error(err);
        return res.status(500).send('Error writing tasks file');
      }
      res.send(newTask);
    });
  });
});

router.put('/tasks/:id', (req, res) => {
  const taskId = req.params.id;
  const taskUpdates = req.body;
  if (!taskUpdates.title && !taskUpdates.description) {
    return res.status(400).send('At least one field is required');
  }
  fs.readFile('tasks.json', 'utf8', (err, data) => {
    if (err) {
      console.error(err);
      return res.status(500).send('Error reading tasks file');
    }
    const tasks = JSON.parse(data);
    const taskIndex = tasks.findIndex(t => t.id === taskId);
    if (taskIndex === -1) {
      return res.status(404).send('Task not found');
    }
    const updatedTask = { ...tasks[taskIndex], ...taskUpdates };
    tasks[taskIndex] = updatedTask;
    fs.writeFile('tasks.json', JSON.stringify(tasks), err => {
      if (err) {
        console.error(err);
        return res.status(500).send('Error writing tasks file');
      }
      res.send(updatedTask);
    });
  });
});

router.delete('/tasks/:id', (req, res) => {
  const taskId = req.params.id;
  fs.readFile('tasks.json', 'utf8', (err, data) => {
    if (err) {
      console.error(err);
      return res.status(500).send('Error reading tasks file');
    }
    const tasks = JSON.parse(data);
    const taskIndex = tasks.findIndex(t => t.id === taskId);
    if (taskIndex === -1) {
      return res.status(404).send('Task not found');
    }
    tasks.splice(taskIndex, 1);
    fs.writeFile('tasks.json', JSON.stringify(tasks), err => {
      if (err) {
        console.error(err);
        return res.status(500).send('Error writing tasks file');
      }
      res.sendStatus(204);
    });
  });
});

app.use('/api', router);

// Error handling
app.use((err, req, res, next) => {
  console.error(err.stack);
  res.status(500).send('Something went wrong!');
});

// Start server
app.listen(4000, () => {
  console.log('Server started on port 4000');
});
