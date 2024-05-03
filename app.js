let secretNum=Math.trunc(Math.random()*20)+1;
let score=20;
let highcore=0;

document.querySelector('.score').textContent=score;
document.querySelector('.number').textContent='?';

function display(message){
  const Message=document.querySelector('.message');
  Message.textContent=message;
  
};

document.querySelector('.check-btn').addEventListener('click', function(){
  const guess=Number(document.querySelector('.guess-inp').value);
  
  if (!guess){
    alert('please pick a number between 1-20!')
  }else if(guess===secretNum){
    if(score > highcore){
      highcore=score;
      document.querySelector('.highscore').textContent=highcore;
    }
    display('correct');
    document.querySelector('.number').textContent=secretNum;
    
  }else if (guess > secretNum){
    if(score>1){
      display('too high 📈');
      score--;
      document.querySelector('.score').textContent=score;

    
    }else{
      display('you lost the game');
      document.querySelector('.score').textContent=0;
    }
    

  }else if(guess < secretNum){
    if(score>1){
      display('too low 📉');
      score--;
      document.querySelector('.score').textContent=score;

    
    }else{
      display('you lost the game');
      document.querySelector('.score').textContent=0;
    }
  }

  document.querySelector('.guess-inp').value='';
  
});

document.querySelector('.again').addEventListener('click', function(){
  score=20;
  document.querySelector('.score').textContent=score;
  guess='';
  document.querySelector('.message').textContent='start guessing...';
  secretNum=Math.trunc(Math.random()*20)+1;
  document.querySelector('.number').textContent='?';
  document.querySelector('.guess-inp').value='';
})





// building again for the sake of practicing


