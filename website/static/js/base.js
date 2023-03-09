function toggleNavbar() {
    const nav = document.getElementsByTagName("nav")[0];
    if (nav.className === "toggle")
        nav.className = "";
    else
        nav.className = "toggle";
}
