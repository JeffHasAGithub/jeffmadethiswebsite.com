const sidenav = document.getElementById("sidenav");
const navopen = document.getElementById("open-nav");

navopen.addEventListener("click", _ => {
    sidenav.style.width = "100vw";
});
