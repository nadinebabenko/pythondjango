const express = require('express');

const app = express();

const PORT = 5000;

app.get('/posts', async (req, res) => {
    try {
      const response = await dataService.fetchPosts();
      const posts = response.data;
      res.send(posts);
      console.log('Data successfully retrieved and sent as a response');
    } catch (error) {
      console.error(error);
      res.status(500).send('Server Error');
    }
  });
  
  app.listen(PORT, () => {
    console.log(`Server running on port ${PORT}`);
  });