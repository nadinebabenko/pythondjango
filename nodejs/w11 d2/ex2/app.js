import { people } from './data.js';

function calculateAverageAge(people) {
  const totalAge = people.reduce((sum, person) => sum + person.age, 0);
  const averageAge = totalAge / people.length;
  console.log(`The average age of all people is ${averageAge}.`);
}

calculateAverageAge(people);