let position = 0;
const cards = document.getElementById("cards");

function slideRight(){
    position -= 250;
    cards.style.transform = `translateX(${position}px)`;
}

function slideLeft(){
    if(position < 0){
        position += 250;
        cards.style.transform = `translateX(${position}px)`;
    }
}

document.querySelector(".right").onclick = slideRight;
document.querySelector(".left").onclick = slideLeft;
