import Button from "./User.js";

const button1 = new Button(
    50,
    150,
    "Login",
    20,
    "Blue",
    "White"
);

const button2 = new Button(
    60,
    200,
    "Register",
    22,
    "Green",
    "Black"
);

const button3 = new Button(
    40,
    120,
    "Exit",
    18,
    "Red",
    "White"
);


button1.show();

button2.show();

button3.show();


console.log(button1.height);

console.log(button1.width);


button1.height = 70;

button1.width = 250;

console.log(button1.height);

console.log(button1.width);


Button.showCounter();


console.log(button1.toString());

console.log(button2.toString());

console.log(button3.toString());