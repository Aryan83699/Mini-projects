const menu=document.querySelector('nav i');
const close = document.querySelector('.menu i');


let tl=gsap.timeline();

tl.to('.menu',{
    transform:"translateX(-100%)",
    ease:'bounse.out',
    duration:0.7,
    delay:0.1,
    ease:'power.out'
})


tl.from('.links h1 , .menu i',{
    x:150,
    opacity:0,
    ease:'power.out',
    duration:0.2,
    stagger:0.2
})



tl.pause();

menu.addEventListener('click',() =>{
    tl.play();
});


close.addEventListener('click',()=>{
    tl.reverse();
})