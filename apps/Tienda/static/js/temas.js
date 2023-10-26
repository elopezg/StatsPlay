function darkMode() {

    document.querySelector('body').setAttribute("data-bs-theme", "dark");
    
}
function lightMode() {

    document.querySelector('body').setAttribute("data-bs-theme", "light");
    
}
function defaultMode() {
    
        document.querySelector('body').removeAttribute("data-bs-theme");
        
    }
function changeMode() {
    var mode = document.getElementById("mode").value;
    if (mode == "dark") {
        darkMode();
    } else if (mode == "light") {
        lightMode();
    } else {
        defaultMode();
    }
}   
