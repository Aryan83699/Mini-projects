let squareBox = document.getElementById('square');
let number = document.getElementById('sq');
let circle=document.getElementById('circle')

squareBox.addEventListener('click', function () {
    number.innerHTML = Math.ceil(Math.random() * 32);
    circle.style.backgroundColor='white';
});



circle.addEventListener('mouseenter',function(){
    let rand=Math.ceil(Math.random()*256);
    let rand1=Math.ceil(Math.random()*256);
    let rand2=Math.ceil(Math.random()*256);
    circle.style.backgroundColor=`rgb(${rand},${rand1},${rand2})`;
})

circle.addEventListener('mouseleave',function(){
    circle.style.backgroundColor='white';
})


let diamond=document.getElementById('diamond');
let diaNumber=document.getElementById('dia');

diamond.addEventListener('mouseenter', function () {
    let num = Math.ceil(Math.random() * 360);
    diamond.style.transform = `rotate(${num}deg)`;
    diaNumber.style.transform=`rotate(${-num}deg)`;
});

diamond.addEventListener('mouseleave', function () {
    diamond.style.transform = 'rotate(-45deg)';
    let rand=Math.ceil(Math.random()*256);
    let rand1=Math.ceil(Math.random()*256);
    let rand2=Math.ceil(Math.random()*256);
    circle.style.backgroundColor=`rgb(${rand},${rand1},${rand2})`;
});