// Simple script for demonstration

/* ===== MENU TOGGLE ===== */
const navMenu = document.getElementById("nav-menu"),
      navToggle = document.getElementById("nav-toggle"),
      navLinks = document.querySelectorAll(".nav__link");

/* Defensive: Only add listeners if elements exist */
if (navToggle && navMenu) {
  // Show/Hide menu on toggle click
  navToggle.addEventListener("click", () => {
    navMenu.classList.toggle("show-menu");

    // Toggle the icons (menu ↔ close)
    const menuIcon = navToggle.querySelector(".nav__toggle-menu");
    const closeIcon = navToggle.querySelector(".nav__toggle-close");
    if (menuIcon && closeIcon) {
      if (navMenu.classList.contains("show-menu")) {
        menuIcon.style.opacity = "0";
        menuIcon.style.pointerEvents = "none";
        closeIcon.style.opacity = "1";
        closeIcon.style.pointerEvents = "auto";
      } else {
        menuIcon.style.opacity = "1";
        menuIcon.style.pointerEvents = "auto";
        closeIcon.style.opacity = "0";
        closeIcon.style.pointerEvents = "none";
      }
    }
  });

  // Hide menu after clicking a link (for mobile UX)
  navLinks.forEach(link => {
    link.addEventListener("click", () => {
      navMenu.classList.remove("show-menu");
      const menuIcon = navToggle.querySelector(".nav__toggle-menu");
      const closeIcon = navToggle.querySelector(".nav__toggle-close");
      if (menuIcon && closeIcon) {
        menuIcon.style.opacity = "1";
        menuIcon.style.pointerEvents = "auto";
        closeIcon.style.opacity = "0";
        closeIcon.style.pointerEvents = "none";
      }
    });
  });
}