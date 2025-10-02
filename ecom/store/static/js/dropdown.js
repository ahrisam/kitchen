const navToggle = document.getElementById('nav-toggle');
const navMenu = document.getElementById('nav-menu');

// Toggle mobile menu
navToggle.addEventListener('click', () => {
    navMenu.classList.toggle('show-menu');
    navToggle.classList.toggle('active');
});

// Handle dropdowns
document.querySelectorAll('.dropdown__button').forEach(button => {
    button.addEventListener('click', (e) => {
        e.stopPropagation(); // Prevent bubbling that might close the menu
        const parent = button.closest('.dropdown__item');
        parent.classList.toggle('active');

        // close other dropdowns
        document.querySelectorAll('.dropdown__item').forEach(item => {
            if (item !== parent) item.classList.remove('active');
        });
    });
});