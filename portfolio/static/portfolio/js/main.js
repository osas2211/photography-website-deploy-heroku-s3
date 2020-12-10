const toggleButton = document.querySelector('.toggle-nav');
const navBarlinks = document.getElementById('main-nav');
toggleButton.addEventListener('click',() => {
    navBarlinks.classList.toggle('active-nav');  
})

/* 
const activeList = document.querySelector('#main-nav li');
var listRange = [...Array(activeList.length).keys()]
activeList.addEventListener('click', () =>{
    activeList.classList.toggle('active');
})

*/


