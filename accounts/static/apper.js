const menu = document.querySelector('#mobile-menu');
const menuLinks = document.querySelector('.navbar__menu');

//funtion to display menu
const mobileMenu = () => {
    menu.classList.toggle('is-active');
    menuLinks.classList.toggle('active');
}
menu.addEventListener('click', mobileMenu);

// image navigation script.
var counter = 1;
setInterval(function() {
    document.getElementById('radio' + counter).checked = true;
    counter++;
    if (counter > 6) {
        counter = 1;
    }
}, 5000);

// Auto-typing script begins here..
var typed = new Typed(".auto-type", {
    strings: ["Web development", "Web-based Applications", "Desktop Apps", "Management Systems", "Information Systems", "Inventory Systems", "Mobile Apps", "Graphic design", "Banners/Posters", "Logos", "Photo/Video Editing"],
    typeSpeed: 70,
    backSpeed: 70,
    loop: true
});

var typed = new Typed(".visions", {
        strings: ["Vision 1", "Vision 2", "Vision 3", "Vision 4"],
        typeSpeed: 150,
        backSpeed: 150,
        loop: true
    })
    // random balls script begins here...
const colors = ["#3CC157", "#2AA7FF", "#1B1B1B", "#FCBC0F", "#F85F36"];

const numBalls = 50;
const balls = [];

for (let i = 0; i < numBalls; i++) {
    let ball = document.createElement("div");
    ball.classList.add("ball");
    ball.style.background = colors[Math.floor(Math.random() * colors.length)];
    ball.style.left = `${Math.floor(Math.random() * 100)}vw`;
    ball.style.top = `${Math.floor(Math.random() * 100)}vh`;
    ball.style.transform = `scale(${Math.random()})`;
    ball.style.width = `${Math.random()}em`;
    ball.style.height = ball.style.width;

    balls.push(ball);
    document.body.append(ball);
}