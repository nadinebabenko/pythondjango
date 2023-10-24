const axios = require('axios');

function fetchPosts() {
  return axios.get('https://jsonplaceholder.typicode.com/posts');
}

module.exports = {
  fetchPosts
};