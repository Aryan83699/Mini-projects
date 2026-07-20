const playBTN=document.querySelector('button');
const body=document.querySelector('body');
const navbar=document.querySelector('.navbar');
const images1=document.querySelectorAll('img')[0];
const images2=document.querySelectorAll('img')[1];
const text=document.querySelectorAll('p');

playBTN.addEventListener('mouseenter',() =>{
    images1.style.opacity="0.02";
    images2.style.opacity="0.02";
    body.classList.add('black-sheet');
    navbar.style.backgroundColor="#104911";

    text.forEach((txt) => {
    txt.style.opacity = "0.02";
    });
    
});

playBTN.addEventListener('mouseleave',() =>{
    images1.style.opacity="1";
    images2.style.opacity="1";
    body.classList.remove('black-sheet');
    navbar.style.backgroundColor="#548C2F";

    text.forEach((txt) => {
    txt.style.opacity = "1";
    });
});
