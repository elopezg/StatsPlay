//funcion js


let lon;
let lat;
let temperature = document.querySelector(".temp");
let loc = document.querySelector(".location");
let icon = document.querySelector(".icon");
const kelvin = 273.15;

window.addEventListener("load", () => {


    if (navigator.geolocation) {
        navigator.geolocation.getCurrentPosition((position) => {

            console.log(position);
            lon = position.coords.longitude;
            lat = position.coords.latitude;

            const appid = `4c5c539868a09c108be62b0741b26ca5`
            const url_base = `https://api.openweathermap.org/data/2.5/weather?lat=${lat}&lon=${lon}&appid=${appid}`
            fetch(url_base)
                .then((response) => {
                    console.log("respuesta json");
                    return response.json();
                })
                .then((data) => {
                    console.log("Esta es la data");
                    console.log(data);

                    temperature.textContent =
                        Math.floor(data.main.temp - kelvin) + "°C";
                    loc.textContent = data.name + "," + data.sys.country;
                });
        }
        )
    }
});