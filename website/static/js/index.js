let pi = 0;

const dom = {
    pbtn:       document.getElementById("pbtn"),
    nbtn:       document.getElementById("nbtn"),
    projects:   document.getElementsByClassName("project"),
};

dom.projects[pi].classList.add("active");

dom.pbtn.addEventListener("click", _ => {
    dom.projects[pi].classList.remove("active");

    if (pi-- === 0)
        pi = dom.projects.length - 1;

    dom.projects[pi].classList.add("active");
})
