const blocksContainer =
    document.getElementById(
        "blocksContainer"
    );

const addButton =
    document.getElementById(
        "addButton"
    );


function getRandomColor() {

    const letters =
        "0123456789ABCDEF";

    let color = "#";


    for (
        let i = 0;
        i < 6;
        i++
    ) {

        color +=

            letters[
                Math.floor(
                    Math.random() * 16
                )
            ];
    }

    return color;
}

function createBlock() {

    const block =
        document.createElement("div");

    block.classList.add("block");


    block.style.backgroundColor =
        getRandomColor();


    block.addEventListener(
        "click",
        function () {

            block.remove();

            console.log(
                "Block removed"
            );
        }
    );


    blocksContainer.append(block);

    console.log(
        "Block added"
    );
}


addButton.addEventListener(
    "click",
    createBlock
);


for (
    let i = 0;
    i < 15;
    i++
) {

    createBlock();
}