function toggleMenu() {
    const burger = document.querySelector('.burger');
    const nav = document.querySelector('.nav-links');
    const navLinks = document.querySelectorAll('.nav-links li');
    const loginRegisterLinks = document.querySelectorAll('.nav-links li.login, .nav-links li.register');

    nav.classList.toggle('nav-active');
    burger.classList.toggle('active');

    navLinks.forEach((link, index) => {
        if (link.style.animation) {
            link.style.animation = '';
            link.style.display = `block`;
        } else {
            link.style.animation = `navLinkFade 0.5s ease forwards ${index / 7 + 0.5}s`;
            link.style.display = `block`;
        }
    });

    loginRegisterLinks.forEach((link) => {
        link.classList.toggle('nav-responsive-btn');
    });
}

document.querySelector('.burger').onclick = toggleMenu;
