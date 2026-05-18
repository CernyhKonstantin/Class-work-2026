// Task 1

const task1 =
    document.getElementById("task1");


const container =
    document.createElement("div");

container.classList.add("container");


const language1 =
    document.createElement("p");

language1.innerText = "C++";


const language2 =
    document.createElement("p");

language2.innerText = "C#";


const language3 =
    document.createElement("p");

language3.innerText = "JS";


container.append(
    language1,
    language2,
    language3
);


const button =
    document.createElement("button");

button.innerText = "Show";


task1.append(
    container,
    button
);


button.addEventListener("click", () => {

    const newLanguage =
        prompt(
            "Enter new programming language:"
        );


    if (
        newLanguage !== null &&
        newLanguage.trim() !== ""
    ) {

        const newParagraph =
            document.createElement("p");

        newParagraph.innerText =
            newLanguage;


        container.append(newParagraph);


        console.log(
            "New language added:",
            newLanguage
        );
    }
});

// Task 2

const textBlock =
    document.getElementById("textBlock");


function getRandomColor() {

    const letters =
        "0123456789ABCDEF";

    let color = "#";


    for (let i = 0; i < 6; i++) {

        color += letters[
            Math.floor(
                Math.random() * 16
            )
        ];
    }

    return color;
}


textBlock.addEventListener("click", () => {

    const randomColor =
        getRandomColor();


    textBlock.style.color =
        randomColor;


    console.log(
        "New text color:",
        randomColor
    );
});