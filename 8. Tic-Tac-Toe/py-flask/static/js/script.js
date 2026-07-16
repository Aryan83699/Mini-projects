let board=document.querySelector(".board");
let boxes=board.querySelectorAll('.boxes');
let resetButton=document.querySelector('#reset');
let win_container=document.querySelector(".win-container");
let h2=document.querySelector(".win-container h2");
let newGame=document.querySelector("#newGame");





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


let turnO=true;


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
})

resetButton.addEventListener('click',()=>{
    empty_boxes();
}
)


function checkWinner(){
    for(patterns of winPatterns){
        let pos1=boxes[patterns[0]].innerText;
        let pos2=boxes[patterns[1]].innerText;
        let pos3=boxes[patterns[2]].innerText;

        if(pos1=='X' && pos2=='X' && pos3=='X'){
            h2.innerText="Winner is X"
            win_container.classList.remove('hide');

            disb_all()
            
        }
        else if(pos1=='O' && pos2=='O' && pos3=='O'){
            h2.innerText="Winner is O"
            win_container.classList.remove('hide');
            disb_all()
        }
    }
}










boxes.forEach(box => {
    box.addEventListener('click',()=>{
        if(turnO){
            box.innerText="O";
            turnO=false;
            
        }
        else{
            box.innerText="X";
            turnO=true;
            
        }
        box.disabled=true;
        checkWinner();
    })
    
});