// Game instance
/*var Game = {
    curr:       0,
    questions:  ["test1", "test2", "test3", "test4"],
    answers:    [true, false, true, false],
    weight:     [5, 5, 5, 5],
    getCurr: function() { return Game.curr; },
    setCurr: function(val) { Game.curr = val; },
}
*/
function Game(val){
    this.curr = val;
    
    // TODO: Add some proper questions.
    this.questions = ["test1", "test2", "test3", "test4"];
    this.answers = [true, false, true, false];
    // 'weight' of the question. The higher the 'weight' the more likely it is to big the question.
    this.weight = [5, 5, 5, 5];
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
    this.getCurrQuestion = function() { return this.questions[this.curr]; }
    this.getCurrAnswer = function() { return this.answers[this.curr]; }
    this.getCurrWeight = function() { return this.weight[curr];}
    this.correct = function() { this.weight[this.curr] -= 2;  this.updateCurr(); }
    this.incorrect = function() { this.weight[this.curr] += 2; this.updateCurr(); }
    // TODO: Add weighted randomization for heavier 'weighted' questions.
    this.updateCurr = function() {
        this.curr = Math.floor(Math.random() * (this.questions.length - 1));
    }
}

var inst = new Game(3);

var gamequestionlabel = document.getElementById('gamecard');

gamequestionlabel.innerText = inst.getCurrQuestion();

function truebutton_onclick(){
    if(inst.getCurrAnswer() === true) {
        inst.correct();
    }
    else {
        inst.incorrect();
    }
}

function falsebutton_onclick(){
    if(inst.getCurrAnswer() === false) {
        inst.correct();
    }
    else {
        inst.incorrect();
    }
}