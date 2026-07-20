const playBTN=document.querySelector('button');
const body=document.querySelector('body');
const navbar=document.querySelector('.navbar');
const images1=document.querySelectorAll('img')[0];
const images2=document.querySelectorAll('img')[1];
const text=document.querySelectorAll('p');
const choice=document.querySelector('.choices');

let clicked=false;

playBTN.addEventListener('click',() =>{

    if(clicked==false){

            images1.style.opacity="0.02";
            images2.style.opacity="0.02";
            body.classList.add('black-sheet');
            navbar.style.backgroundColor="#104911";

            text.forEach((txt) => {
            txt.style.opacity = "0.02";
            });
            choice.style.visibility="visible";
            playBTN.innerText="Leave";
            playBTN.style.backgroundColor="red";

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
