const fs = require('fs');

// read content from source.txt and write to destination.txt
fs.readFile('source.txt', 'utf8', (err, data) => {
  if (err) throw err;
  fs.writeFile('destination.txt', data, (err) => {
    if (err) throw err;
    console.log('The file has been saved!');
  });
});

fs.readdir('/path/to/directory', (err, files) => {
    if (err) throw err;
    files.forEach(file => {
      console.log(file);
    });
  });