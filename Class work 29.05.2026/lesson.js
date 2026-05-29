const cityInput =
    document.getElementById(
        "cityInput"
    );

const searchButton =
    document.getElementById(
        "searchButton"
    );

const weatherResult =
    document.getElementById(
        "weatherResult"
    );


const apiKey =
    "0006fae8c55ab1d0d3917f71859c8058";


async function getWeather() {

    const city =
        cityInput.value.trim();


    if (city === "") {

        weatherResult.innerHTML =

            `
            <p>
                Please enter a city
            </p>
            `;

        return;
    }


    try {


        const response =
            await fetch(

                `https://api.openweathermap.org/data/2.5/weather?q=${city}&appid=${apiKey}&units=metric`

            );


        if (!response.ok) {

            throw new Error(
                "City not found"
            );
        }


        const data =
            await response.json();


        const cityName =
            data.name;

        const country =
            data.sys.country;

        const temperature =
            data.main.temp;

        const feelsLike =
            data.main.feels_like;

        const humidity =
            data.main.humidity;

        const description =
            data.weather[0].description;


        weatherResult.innerHTML =

            `
            <div class="weather-box">

                <h2>
                    ${cityName}, ${country}
                </h2>

                <div class="temperature">
                    ${temperature}°C
                </div>

                <p>
                    Weather:
                    ${description}
                </p>

                <p>
                    Feels Like:
                    ${feelsLike}°C
                </p>

                <p>
                    Humidity:
                    ${humidity}%
                </p>

            </div>
            `;


        console.log(data);

    } catch (error) {

        weatherResult.innerHTML =

            `
            <p>
                ${error.message}
            </p>
            `;
    }
}


searchButton.addEventListener(
    "click",
    getWeather
);


cityInput.addEventListener(
    "keydown",
    function (event) {

        if (event.key === "Enter") {

            getWeather();
        }
    }
);