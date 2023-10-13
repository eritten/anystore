// aos initialisation
AOS.init({
    offset: 100,
    delay: 100,
    duration: 600,
    easing: 'ease',
    once: false,
    mirror: false,
    anchorPlacement: 'top-bottom'
})

// nav links stay highlighted when clicked
// assigning variables
const navLinks = document.querySelectorAll(".nav-wrapper .nav-list a")

navLinks.forEach(link => {
    link.addEventListener("click", highlightLink)
})

function highlightLink() {
    navLinks.forEach(link =>{
        link.classList.remove("highlight")
        this.classList.add("highlight")
    })
}
// nav btns
const menuBtn = document.querySelector(".icon-box .menu-btn")
const searchForm = document.querySelector(".search-form")
const menuNav = document.querySelector("nav .nav-list")

// event listeners
window.addEventListener("scroll", ()=> {
    if(scrollY > 0) {
        deactivateMobileNav()
        deactivateSearch()
    } 
})
menuBtn.addEventListener("click", activateMobileNav)

function activateMobileNav() {
    menuBtn.classList.toggle("active")
    menuNav.classList.toggle("active")
    deactivateSearch()
}
function deactivateMobileNav() {
    menuBtn.classList.remove("active")
    menuNav.classList.remove("active")
}
function activateSearch() {
    searchForm.classList.toggle("active")
    deactivateMobileNav()
}
function deactivateSearch() {
    searchForm.classList.remove("active")
}

// select all the buttons in nav .icon-box with querySelectorAll
const navIcons = document.querySelectorAll("nav .icon-box button")

// loop through the buttons and add click event listeners to toggle active class on searchForm
navIcons.forEach(icon => {
    icon.addEventListener("click", () => {
        searchForm.classList.toggle("active")
    })
}) 



