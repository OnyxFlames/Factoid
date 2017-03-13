function Game(val){
    this.curr = val;
    // TODO: Add some proper questions.
    this.questions = ["In Javascript, variables are declared with int variable = 0;",
     "The alert() function is best for printing to the console.",
     "Functions are useful for when you only have to you use code once.",
     "Javascript uses the square brackets([ and ]) for accessing an arrays elements.",
     ];
    this.answers = [false, false, false, true];
    // 'weight' of the question. The higher the 'weight' the more likely it is to big the question.
    this.weight = [1, 1, 1, 1];
    this.getCurr = function() { return this.curr; }
    this.setCurr = function(val) {
        if (val >= this.questions.length || val < 0) {
            console.log("Error: Attempted to set curr to invalid value.");
            return;
        }
        else {
            this.curr = val;
            return;
        }
    }
    this.getCurrQuestion = function() {
        if(this.questions.length <= 0)
            return "You answered all the questions sufficiently!";
        else
            return this.questions[this.curr];
    }
    this.getCurrAnswer = function() { return this.answers[this.curr]; }
    this.getCurrWeight = function() { return this.weight[this.curr];}
    this.correct = function() { this.weight[this.curr] -= 2;  this.updateCurr(); }
    this.incorrect = function() { this.weight[this.curr] += 2; this.updateCurr(); }
    // TODO: Add weighted randomization for heavier 'weighted' questions.
    this.updateCurr = function() {
        if (this.getCurrWeight() <= 0) {
            this.questions.splice(this.getCurr(), 1);
            this.answers.splice(this.getCurr(), 1);
            this.weight.splice(this.getCurr(), 1);
        }
        this.curr = Math.floor(Math.random() * (this.questions.length - 1));
    }
}

var inst = new Game(3);

var gameQuestionLabel = document.getElementById('gamecard');

gameQuestionLabel.innerText = inst.getCurrQuestion();

function eval(buttonVal) {
  if(Boolean(buttonVal) === inst.getCurrAnswer()) {
    console.log('correct');
    inst.correct();
  } else {
    console.log('incorrect')
    inst.incorrect();
  }
  gameQuestionLabel.innerText = inst.getCurrQuestion();
}
