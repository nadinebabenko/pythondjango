const fileManager = require('./fileManager');

fileManager.readFile('Hello World.txt')
  .then((data) => {
    return fileManager.writeFile('Bye World.txt', 'Writing to the file');
  })
  .then(() => {
    console.log('File reading and writing operations successful');
  })
  .catch((err) => {
    console.error(err);
  });