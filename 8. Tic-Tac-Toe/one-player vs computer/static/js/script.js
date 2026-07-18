let board=document.querySelector(".board");
let boxes=board.querySelectorAll('.boxes');
let resetButton=document.querySelector('#reset');
let win_container=document.querySelector(".win-container");
let h2=document.querySelector(".win-container h2");
let newGame=document.querySelector("#newGame");


let turnO;
let computer;
let gameOver=false;

let winPatterns=[
    [0,1,2],
    [3,4,5],
    [6,7,8],
    [0,4,8],
    [2,4,6],
    [0,3,6],
    [1,4,7],
    [2,5,8]
];


if(player=='X'){
   turnO=false; 
   computer='O';
}
else{
    turnO=true;
    computer='X';
}

let moves=['X','O'];


let humanTurn=true;


const disb_all =()=>{
    for(box of boxes){
        box.disabled=true;
    }
}


const empty_boxes = () =>{
        for(box of boxes){
        box.innerText="";
        box.disabled=false;
    }
}


newGame.addEventListener('click',()=>{
    empty_boxes();
    win_container.classList.add('hide');
    gameOver=false;
        if (player == 'X') {
        turnO = false;
        computer = 'O';
    } else {
        turnO = true;
        computer = 'X';
    }
})

resetButton.addEventListener('click',()=>{
    empty_boxes();
        gameOver=false;
        if (player == 'X') {
        turnO = false;
        computer = 'O';
    } else {
        turnO = true;
        computer = 'X';
    }
}
)


function checkWinner(){
    for(patterns of winPatterns){
        let pos1=boxes[patterns[0]].innerText;
        let pos2=boxes[patterns[1]].innerText;
        let pos3=boxes[patterns[2]].innerText;

        if(pos1=='X' && pos2=='X' && pos3=='X'){
            gameOver=true;
            h2.innerText="Winner is X"
            win_container.classList.remove('hide');

            disb_all()
            
        }
        else if(pos1=='O' && pos2=='O' && pos3=='O'){
            gameOver=true;
            h2.innerText="Winner is O"
            win_container.classList.remove('hide');
            disb_all()
        }
    }
}


function play () {
    boxes.forEach(box => {
    box.addEventListener('click',()=>{
        if(turnO){
            box.innerText=player;
            turnO=false;
            
        }
        else{
            box.innerText=player;
            turnO=true;
            
        }
        box.disabled=true;
        checkWinner();
        if (!gameOver) {
            setTimeout(() => {
                comp_play(computer);
            }, 800);
        }
    })
    
});

}


play();



const enable_all =()=>{
    for(box of boxes){
        box.disabled=false;
    }
}


const comp_play=(player_val)=>{
    disb_all();
    let empty=[];

    boxes.forEach((box,index)=>{
        if(box.innerText==""){
            empty.push(index);  
        }

    })

    let randomIndex = Math.floor(Math.random() * empty.length);
    let move = empty[randomIndex];

    boxes[move].innerText = player_val;
    boxes[move].disabled = true;
    checkWinner();
    enable_all();
    
}