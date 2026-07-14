const board = document.querySelector(".board");
const buttons = board.querySelectorAll("button");
const resetButton = document.querySelector("#resetButton");
const newButton=document.querySelector("#newButton");
const msg_container=document.querySelector(".msg-container");
const msg = document.querySelector("#msg");


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


// reset button
const disButtons=()=>{
    for(let button of buttons){
        button.disabled=true;
    }
}

const reset=()=>{
    for(let button of buttons){
        button.disabled=false;
        button.innerText="";
        turnO=true;
    }
}


// winner checking and show
const showWinner=(winner)=>{

    msg.innerText=`Winner is ${winner}`;
    msg_container.classList.remove('hide');
}

const checkWinner = () => {
    for (pattern of winPatterns){
        let pos1=buttons[pattern[0]].innerText;
        let pos2=buttons[pattern[1]].innerText;
        let pos3=buttons[pattern[2]].innerText;

        if (pos1=='X' && pos2=='X' && pos3=='X'){
            showWinner(pos1);
            disButtons();
            
        }
        else if(pos1=='O' && pos2=='O' && pos3=='O'){
        showWinner(pos2);
        disButtons();
        
    }
}
}


//turn
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
        checkWinner();
        
    });

    

});


resetButton.addEventListener('click',reset);

newButton.addEventListener('click',()=>{
    reset();
    msg_container.classList.add('hide');
});

