const _ = require('lodash');
const math = require('./math-app');

const a = 5;
const b = 10;

const sum = math.add(a, b);
const product = math.multiply(a, b);
const squaredSum = _.chain([a, b])
  .map(num => num ** 2)
  .sum()
  .value();

console.log(`The sum of ${a} and ${b} is ${sum}`);
console.log(`The product of ${a} and ${b} is ${product}`);
console.log(`The squared sum of ${a} and ${b} is ${squaredSum}`);