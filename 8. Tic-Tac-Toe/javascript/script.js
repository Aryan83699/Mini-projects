const board = document.querySelector(".board");
const buttons = board.querySelectorAll("button");
const resetButton = document.querySelector("#resetButton");
console.log(buttons);
console.log(resetButton);

console.log(buttons[-1])


let turnO=true;


const winPatterns = [
    [0,1,2],
    [3,4,5],
    [6,7,8],
    [0,4,8],
    [2,4,6],
    [0,3,6],
    [1,4,7],
    [2,5,8]
]

buttons.forEach(button =>{
    button.addEventListener('click',()=>{
        if(turnO){ // player O
            button.innerText="O";
            turnO=false;
         
        }
        else{ // player X
            button.innerText="X";
            turnO=true;
            
        }
        button.disabled=true;
    });

    checkWinner();

});


const checkWinner = () => {
    for (pattern of winPatterns){
        console.log(pattern);
    }
}