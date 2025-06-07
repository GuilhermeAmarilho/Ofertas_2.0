function toggleMenu() {
    const navItems = document.querySelector('.nav-items');
    navItems.classList.toggle('active');
    navItems.style.top = document.querySelector('nav.navbar').offsetHeight + 'px'    
}