circle=document.querySelector('.circle');
body=document.querySelector('body');
overlay=document.querySelector('.overlay');


body.addEventListener("mousemove",(e) =>{
  
    gsap.to(".circle",{
        x:e.x,
        y:e.y,
        ease:'black.out'
    })
})


overlay.addEventListener("mouseenter",()=>{
    gsap.to(".circle",{
        scale:3,
        backgroundColor:"transparent",
        border:"0.01px solid white"
    })
})


overlay.addEventListener("mouseleave",()=>{
    gsap.to(".circle",{
        scale:1,
        backgroundColor:"white"
    })
})