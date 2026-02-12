

arr=[
    'https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRcabcl_IhEZrMWpCZDFRBDiq3avwhPm5TYKA&s',
    'https://dz3we2x72f7ol.cloudfront.net/expansions/mega-evolution/en-us/JL2G_EN_25-2x.png',
    'https://dz3we2x72f7ol.cloudfront.net/expansions/mega-evolution/en-us/JL2G_EN_77-2x.png',
    'https://dz3we2x72f7ol.cloudfront.net/expansions/mega-evolution/en-us/JL2G_EN_88-2x.png',
    'https://dz3we2x72f7ol.cloudfront.net/expansions/mega-evolution/en-us/JL2G_EN_95-2x.png',
    'https://dz3we2x72f7ol.cloudfront.net/expansions/mega-evolution/en-us/JL2G_EN_100-2x.png'
];

let main=document.getElementsByClassName('main')[0]

s=''

for(let i=1;i<=44;i++){
    n=Math.ceil(Math.random()*5)
    s+=`<div class="card">
                <img src=${arr[n]} width="119px" height="149px" alt='pokemon card'>
        </div>`
}

main.innerHTML=s;