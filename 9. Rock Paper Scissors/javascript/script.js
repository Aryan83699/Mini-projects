const playBTN=document.querySelector('button');
const body=document.querySelector('body');
const navbar=document.querySelector('.navbar');
const images1=document.querySelectorAll('img')[0];
const images2=document.querySelectorAll('img')[1];
const text=document.querySelectorAll('p');
const choice=document.querySelector('.choices');
const choicesids=document.querySelectorAll('.choice');

let clicked=false;

let computerScore=0;
let humanScore=0;


playBTN.addEventListener('click',() =>{

    if(clicked==false){

            images1.style.opacity="0.1";
            images2.style.opacity="0.1";
            body.classList.add('black-sheet');
            navbar.style.backgroundColor="#104911";

            text.forEach((txt) => {
            txt.style.opacity = "0.1";
            });
            choice.style.visibility="visible";
            playBTN.innerText="Leave";
            playBTN.style.backgroundColor="red";

            choicesids.forEach((chc) => {
            chc.classList.add('popup');
            });


            clicked=true;



    }

    else{
        images1.style.opacity="1";
        images2.style.opacity="1";
        body.classList.remove('black-sheet');
        navbar.style.backgroundColor="#548C2F";

        text.forEach((txt) => {
        txt.style.opacity = "1";
        });
        choice.style.visibility="hidden";
        playBTN.innerText="Play";
        playBTN.style.backgroundColor="#104911";
        choicesids.forEach((chc) => {
            chc.classList.remove('popup');
            });

        clicked=false;
    }

});

// playBTN.addEventListener('click',() =>{
//     images1.style.opacity="1";
//     images2.style.opacity="1";
//     body.classList.remove('black-sheet');
//     navbar.style.backgroundColor="#548C2F";

//     text.forEach((txt) => {
//     txt.style.opacity = "1";
//     });
//     choice.style.visibility="hidden";
// });

function checkWinner(humanMove){
    if(humanMove==ComputerMove){
        console.log('Draw');
    }
    else if(humanMove=='rock')// rock vs paper and scissor
        {
        if(computerMove=='scissor'){
            console.log('Human Winner');
        }
        else{
            console.log('Computer Winner');
        }
    }
    else if(humanMove=='paper'){ //paper vs scissor and rock
        if(computerMove=='scissor'){
            console.log('Computer Winner');
        }
        else{
            console.log('Human Winner');
        }
    }
    else //scissor vs rock and paper
      {
        if(computerMove=='rock'){
            console.log('Computer Winner');
        }
        else{
            console.log('Human Winner');
        }
    }
}

choicesids.forEach((choose) => {
    choose.addEventListener('click',() =>{
        let humanMove=choose.id;
        checkWinner(humanMove);
    })
});