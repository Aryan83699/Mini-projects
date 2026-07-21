const playBTN=document.querySelector('button');
const body=document.querySelector('body');
const navbar=document.querySelector('.navbar');
const images1=document.querySelectorAll('img')[0];
const images2=document.querySelectorAll('img')[1];
const text=document.querySelectorAll('p');
const choice=document.querySelector('.choices');
const choicesids=document.querySelectorAll('.choice');
const opt1=document.querySelector('.playerMove img');
const opt2=document.querySelector('.computerMove img');
const compScore=document.querySelector('#computerScore');
const hScore=document.querySelector('#humanScore');
const message=document.querySelector('.message');
const player_NO=document.querySelector('.player_choice');
const computer_YES=document.querySelector('.computer_choice');

let clicked=false;


let computerScore=0;
let humanScore=0;
let moves=['rock','scissor','paper'];
let computerMove;


const delay = () =>{
    setTimeout(() => {
        message.style.visibility='hidden';
    }, 1500);
}

const humanwin = () =>{
    humanScore=humanScore+1;
    hScore.innerText=`Score :${humanScore}`;
    message.innerText='You Win';
    message.style.backgroundColor='#104911';
    message.style.visibility='visible';
    delay();
}

const computerwin = () =>{
    computerScore=computerScore+1;
    compScore.innerText=`Score :${computerScore}`;
    message.innerText='Computer Win';
    message.style.backgroundColor='#9c4506';
    message.style.visibility='visible';
    delay()

}



const removeBlacksheet = () => {
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


// console.log(Math.floor(Math.random()*3))
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
        removeBlacksheet();
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


const things = () => {
    removeBlacksheet();


}



// function checkWinner(humanMove){
//     if(humanMove==computerMove){
//         if(humanMove=='rock'){
//             opt1.src="images/Rock.jpg";
//             opt2.src='images/Rock.jpg';
//         }
//         else if(humanMove=='scissor'){
//             opt1.src="images/Scissor.jpg";
//             opt2.src="images/Scissor.jpg";
            
//         }
//         else{
//             opt1.src="images/Paper.jpg";
//             opt2.src="images/Paper.jpg";
//         }
//         console.log('Draw');
//     }
//     else if(humanMove=='rock')// rock vs paper and scissor
            
//         {
//             opt1.src="images/Rock.jpg";
//         if(computerMove=='scissor'){
//             opt2.src='images/Scissor.jpg';
//             console.log('Human Winner');
//         }
//         else{
//             opt2.src="images/Paper.jpg";
//             console.log('Computer Winner');
//         }
//     }
//     else if(humanMove=='paper'){ 
//         opt1.src="images/Paper.jpg";
        
//         //paper vs scissor and rock
//         if(computerMove=='scissor'){
//             opt2.src='images/Scissor.jpg';
//             console.log('Computer Winner');
//         }
//         else{
//             opt2.src="images/Rock.jpg";
//             console.log('Human Winner');
//         }
//     }
//     else //scissor vs rock and paper
//       {
//         opt1.src="images/Scissor.jpg";
//         if(computerMove=='rock'){
//             opt2.src="images/Rock.jpg";
//             console.log('Computer Winner');
//         }
//         else{
//             opt2.src="images/Paper.jpg";
//             console.log('Human Winner');
//         }
//     }
// }

function checkWinner(humanMove) {

    // Set the images first
    opt1.src = `images/${humanMove.charAt(0).toUpperCase() + humanMove.slice(1)}.jpg`;
    opt2.src = `images/${computerMove.charAt(0).toUpperCase() + computerMove.slice(1)}.jpg`;

    if (humanMove == computerMove) {
            message.innerText='Match Draw';
            message.style.backgroundColor='black';
            message.style.visibility='visible';
            delay();
    }
    else if (humanMove == "rock") {
        if (computerMove == "scissor") {
            console.log("Human Winner");
            humanwin();
        } else {
            computerwin();
        }
    }
    else if (humanMove == "paper") {
        if (computerMove == "scissor") {
            computerwin();
        } else {
            humanwin();
        }
    }
    else { // scissor
        if (computerMove == "rock") {
            computerwin();
        } else {
            humanwin();
        }
    }
}





choicesids.forEach((choose) => {
    choose.addEventListener('click',() =>{
        let humanMove=choose.id;
        computerMove=moves[Math.floor(Math.random()*3)];
        console.log(computerMove);
        player_NO.classList.remove("NO");
    computer_YES.classList.remove("YES");

    // Restart animation
    player_NO.classList.remove("animate-player");
    computer_YES.classList.remove("animate-computer");

    void player_NO.offsetWidth;
    void computer_YES.offsetWidth;

    player_NO.classList.add("animate-player");
    computer_YES.classList.add("animate-computer");

    things();
    checkWinner(humanMove);

    setTimeout(() => {
        player_NO.classList.add("NO");
        computer_YES.classList.add("YES");
    }, 1500);
        })
});
