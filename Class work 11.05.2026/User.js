class Button {

    #height;

    #width;


    static #counter = 0;


    constructor(
        height,
        width,
        text_back,
        font_size,
        color_back,
        color_text
    ) {

        this.#height = height;

        this.#width = width;

        this.text_back = text_back;

        this.font_size = font_size;

        this.color_back = color_back;

        this.color_text = color_text;

        Button.#counter++;
    }


    get height() {

        return this.#height;
    }

    get width() {

        return this.#width;
    }


    set height(value) {

        this.#height = value;
    }

    set width(value) {

        this.#width = value;
    }


    static showCounter() {

        console.log("Buttons created:", Button.#counter);
    }


    show() {

        console.log("Button text:", this.text_back);
    }


    toString() {

        return `
Height: ${this.#height}
Width: ${this.#width}
Text: ${this.text_back}
Font size: ${this.font_size}
Background color: ${this.color_back}
Text color: ${this.color_text}
`;
    }
}

export default Button;