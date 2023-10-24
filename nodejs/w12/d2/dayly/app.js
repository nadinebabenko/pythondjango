const express = require('express');
const app = express();
const quizRouter = express.Router();

app.use('/quiz', quizRouter);


app.listen(5000, () => {
    console.log('Server started on port 5000');
  });

  quizRouter.get('/', (req, res) => {
   
    score = 0;
    currentQuestion = 0;
    
    res.send(`
      <h1>Trivia Quiz</h1>
      <p>${quiz[currentQuestion].question}</p>
      <form method="post" action="/quiz">
        <input type="text" name="answer" placeholder="Your answer" required>
        <button type="submit">Submit</button>
      </form>
    `);
  });

  quizRouter.post('/', (req, res) => {
   
    if (req.body.answer.toLowerCase() === quiz[currentQuestion].answer.toLowerCase()) {
      
      score++;
     
      res.send(`
        <h1>Trivia Quiz</h1>
        <p>Correct!</p>
        <p>Your score is ${score}.</p>
        <form method="get" action="/quiz">
          <button type="submit">Next question</button>
        </form>
      `);
    } else {
      
      res.send(`
        <h1>Trivia Quiz</h1>
        <p>Incorrect. The correct answer is ${quiz[currentQuestion].answer}.</p>
        <p>Your score is ${score}.</p>
        <form method="get" action="/quiz">
          <button type="submit">Next question</button>
        </form>
      `);
    }
   
    currentQuestion++;
    
    if (currentQuestion === quiz.length) {
     
      res.redirect('/quiz/score');
    }
  });

  quizRouter.get('/score', (req, res) => {
    res.send(`
      <h1>Trivia Quiz</h1>
      <p>Your final score is ${score} out of ${quiz.length}.</p>
    `);