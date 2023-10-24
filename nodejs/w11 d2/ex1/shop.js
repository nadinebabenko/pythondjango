const products = require("./product.js")

function findProductByName(name) {
    return products.find(product => product.name === name);
  }
console.log(findProductByName("Product 1"));
console.log(findProductByName("Product 3"));
console.log(findProductByName("Product 5"));