const express = require('express');
const app = express();
const router = express.Router();

app.use('/', router);

app.listen(5000, () => {
    console.log('Server listening on port 3000');
  });


router.get('/', (req, res) => {
    res.send('Hello World!');
  });
  
  module.exports = router;