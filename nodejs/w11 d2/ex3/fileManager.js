const fs = require('fs');

module.exports = {
  readFile: (filePath) => {
    return new Promise((resolve, reject) => {
      fs.readFile(filePath, 'utf8', (err, data) => {
        if (err) {
          reject(err);
        } else {
          resolve(data);
        }
      });
    });
  },
  writeFile: (filePath, content) => {
    return new Promise((resolve, reject) => {
      fs.writeFile(filePath, content, (err) => {
        if (err) {
          reject(err);
        } else {
          resolve();
        }
      });
    });
  }
};
//echo "Hello World !!" > "Hello World.txt" 
//echo "Bye World !!" > "Bye World.txt"