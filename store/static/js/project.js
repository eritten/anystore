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

const footerDate = document.querySelector('#date')
const date = new Date()
footerDate.innerHTML = date.getFullYear()




