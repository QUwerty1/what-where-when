const setProgressBar = () => {
    document.getElementById("js-progress-bar").style.width =
        window.scrollY / (document.body.offsetHeight - window.innerHeight) * 100 + "%";
};
const setTheme = (theme) => {
    document.body.dataset.theme = theme;
    setDBTheme(theme);
    document.getElementById("js-theme-icon").className = theme === "light" ? "bi bi-sun" : "bi bi-moon-fill";
};
const getDBTheme = () => {
    return window.localStorage.getItem("theme");
}
const setDBTheme = (theme) => {
    return window.localStorage.setItem("theme", theme);
}

{
    let a = !!getDBTheme() ? {} : setDBTheme(
        window.matchMedia("(prefers-color-scheme: dark)").matches ? "dark" : "light"
    );
    setTheme(getDBTheme());
    setProgressBar();
}

window.addEventListener("scroll", () => {
    setProgressBar();
});
document.getElementById("js-theme-changer").addEventListener("click", () => {
    setTheme(getDBTheme() === "light" ? "dark" : "light");
});



