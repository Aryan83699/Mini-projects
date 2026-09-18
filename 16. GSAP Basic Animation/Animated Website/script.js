gsap.registerPlugin(ScrollTrigger);

const tl=gsap.timeline()

const tl2=gsap.timeline({
    scrollTrigger:{
        trigger:'section',
        scroller:'body',
        start:"top 50%",
        end:"top 5",
        scrub:1.5,
    }
})

tl.from('nav .logo',{
    opacity:0,
    x:-500,
    duration:1,
    ease:'power.out'
},"0")

tl.from('nav li',{
    opacity:0,
    x:-20,
    duration:0.15,
    ease:'power.out',
    stagger:0.1
},"0")


tl.from('main .left > *',{
    opacity:0,
    x:-100,
    duration:0.5,
    stagger:0.25
},"1")


tl.from("main .right", {
  opacity: 0,
  x: 100,
  duration: 0.5
}, "1"); 


tl.from('.bottom img',{
    opacity:0,
    duration:0.7,
    stagger:0.3,
    duration:0.5
},"0")




tl2.from('.services h1',{
    x:-200,
    opacity:0,
    duration:5
})


tl2.from('.services h1',{
    x:-200,
    opacity:0
})


tl2.from('.cards #card1',{
    x:-200,
    opacity:0,
    duration:3
    
})


tl2.from('.cards #card2',{
    x:200,
    opacity:0,
    duration:3  
})