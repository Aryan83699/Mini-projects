let search = document.querySelector('.search-bar');


window.addEventListener("scroll", () => {
  if (window.scrollY >= 800) {
    search.classList.remove('hidden');
  }else{
    search.classList.add('hidden');
  }
  
});

