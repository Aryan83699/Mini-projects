const tl=gsap.timeline()



tl.from('nav .logo',{
    opacity:0,
    x:-20,
    duration:0.5,
})

tl.from('nav li',{
    opacity:0,
    x:-20,
    duration:0.2,
    stagger:0.25
})