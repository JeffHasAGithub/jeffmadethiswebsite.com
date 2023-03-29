const header = document.querySelector("header");
const main = document.querySelector("main");

const headToggle = header.querySelector("button");
const mainToggle = main.querySelector("button");

headToggle.addEventListener("click", (_) => {
    header.style.width = 0;
})
mainToggle.addEventListener("click", (_) => {
    header.style.width = "100vw";
});
