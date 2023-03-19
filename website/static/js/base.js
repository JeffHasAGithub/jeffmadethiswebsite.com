const sidenav = document.getElementById("sidenav");
const navopen = document.getElementById("open-nav");
const navclose = document.getElementById("close-nav");

navopen.addEventListener("click", _ => {
    sidenav.style.width = "100vw";
});

navclose.addEventListener("click", _ => {
    sidenav.style.width = "0vw";
});
