document.addEventListener('DOMContentLoaded', () => {
    /* ================= MENU TOGGLE LOGIC ================= */
    const navMenu = document.getElementById("nav-menu");
    const navToggle = document.getElementById("nav-toggle");
    const navLinks = document.querySelectorAll(".nav__link");
    const menuIcon = document.querySelector(".nav__toggle-menu");
    const closeIcon = document.querySelector(".nav__toggle-close");

    if (navToggle && navMenu) {
        navToggle.addEventListener("click", () => {
            const isOpen = navMenu.classList.toggle("show-menu");
            
            // Toggle Icons
            if (isOpen) {
                if(menuIcon) {
                    menuIcon.style.opacity = "0";
                    menuIcon.style.pointerEvents = "none";
                }
                if(closeIcon) {
                    closeIcon.style.opacity = "1";
                    closeIcon.style.pointerEvents = "auto";
                }
            } else {
                if(menuIcon) {
                    menuIcon.style.opacity = "1";
                    menuIcon.style.pointerEvents = "auto";
                }
                if(closeIcon) {
                    closeIcon.style.opacity = "0";
                    closeIcon.style.pointerEvents = "none";
                }
            }
        });
    }

    /* ================= DROPDOWN LOGIC ================= */
    const dropdownButtons = document.querySelectorAll('.dropdown__button');

    dropdownButtons.forEach(button => {
        button.addEventListener('click', (e) => {
            e.stopPropagation(); // Prevent bubbling
            const parent = button.closest('.dropdown__item');
            
            // Close other open dropdowns first
            document.querySelectorAll('.dropdown__item.active').forEach(item => {
                if (item !== parent) item.classList.remove('active');
            });

            // Toggle current
            parent.classList.toggle('active');
        });
    });

    // Close dropdowns when clicking outside
    document.addEventListener('click', () => {
        document.querySelectorAll('.dropdown__item.active').forEach(item => {
            item.classList.remove('active');
        });
    });
    
    // Close mobile menu when a non-dropdown link is clicked
    navLinks.forEach(link => {
        link.addEventListener("click", () => {
            if(!link.classList.contains('dropdown__button') && navMenu) {
                navMenu.classList.remove("show-menu");
                
                // Reset Icons
                if(menuIcon) {
                    menuIcon.style.opacity = "1";
                    menuIcon.style.pointerEvents = "auto";
                }
                if(closeIcon) {
                    closeIcon.style.opacity = "0";
                    closeIcon.style.pointerEvents = "none";
                }
            }
        });
    });
});