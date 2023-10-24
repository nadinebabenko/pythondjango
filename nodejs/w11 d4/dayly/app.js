const express = require('express');
const app = express();

app.listen(3000, () => {
    console.log('Server started on port 3000');
  });
 
  const emojis = [
    { name: 'smiling face with heart-eyes', emoji: '😍' },
    { name: 'face with tears of joy', emoji: '😂' },
    { name: 'red heart', emoji: '❤️' },
    { name: 'folded hands', emoji: '🙏' },
    { name: 'smiling face with sunglasses', emoji: '😎' },
    { name: 'face with rolling eyes', emoji: '🙄' },
    { name: 'face with medical mask', emoji: '😷' },
    { name: 'face with tongue', emoji: '😛' },
    { name: 'pile of poo', emoji: '💩' },
    { name: 'clapping hands', emoji: '👏' }
  ];

 
app.get('/game', (req, res) => {
   
  const randomIndex = Math.floor(Math.random() * emojis.length);
  const randomEmoji = emojis[randomIndex];

 
  const distractors = emojis
    .filter((emoji) => emoji.name !== randomEmoji.name)
    .sort(() => 0.5 - Math.random())
    .slice(0, 3);

  
  const options = [randomEmoji, ...distractors].sort(() => 0.5 - Math.random());

 
  res.render('game', { emoji: randomEmoji.emoji, options });
});

 
app.post('/game', (req, res) => {
  const { guess } = req.body;
  const { name } = req.query;

  
  if (guess === name) {
    // Update the player's score
  }

 
  res.send(`Your guess was ${guess === name ? 'correct' : 'incorrect'}.`);
});


