const heading=document.querySelector('div');

text=heading.innerText;


function splitter(text){
splitText=text.split("");

length=splitText.length/2;

let clutter="";

console.log(splitText);

splitText.forEach((element,idx) => {
    if(['V','/','s'].includes(element)){
        clutter+=`<span class='c'>${element}</span>`;
    }
    else if(idx<length){

        clutter+=`<span class='a'>${element}</span>`;
    }
    else{

        clutter+=`<span class='b'>${element}</span>`;
    }
});

heading.innerHTML=clutter;
};

splitter(text); 


gsap.from('.a',{
    opacity:0,
    y:50,
    delay:0.3,
    duration:0.6,
    ease:'power.out',
    stagger:0.15
})


gsap.from('.b',{
    opacity:0,
    y:-50,
    delay:0.3,
    duration:0.6,
    ease:'power.out',
    stagger:-0.15
})



gsap.from('.c',{
    opacity:0,
    y:-500,
    delay:0.3,
    duration:0.6,
    ease:'bounce.out',
    stagger:-0.15
})

