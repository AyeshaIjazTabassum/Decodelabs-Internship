const imageInput =
document.getElementById("imageInput");

const preview =
document.getElementById("preview");

imageInput.addEventListener("change", function(){

    const file = this.files[0];

    if(file){

        const reader =
        new FileReader();

        reader.onload = function(e){

            preview.src =
            e.target.result;

            preview.style.display =
            "block";
        };

        reader.readAsDataURL(file);
    }
});

async function predictWaste(){

    const file =
    imageInput.files[0];

    if(!file){

        alert("Please upload an image first.");

        return;
    }

    document
    .getElementById("loader")
    .style.display = "block";

    const formData =
    new FormData();

    formData.append(
        "image",
        file
    );

    try{

        const response =
        await fetch(
            "/predict",
            {
                method:"POST",
                body:formData
            }
        );

        const data =
        await response.json();

        document
        .getElementById("loader")
        .style.display = "none";

        document
        .getElementById("result-card")
        .style.display = "block";

        document
        .getElementById("waste-name")
        .innerText =
        data.class.toUpperCase();

        document
        .getElementById("confidence")
        .innerText =
        data.confidence + "%";

        document
        .getElementById("recyclable")
        .innerText =
        data.recyclable;

        document
        .getElementById("bin")
        .innerText =
        data.bin;

        document
        .getElementById("impact")
        .innerText =
        data.impact;

        document
        .getElementById("result-card")
        .scrollIntoView({
            behavior:"smooth"
        });

    }catch(error){

        document
        .getElementById("loader")
        .style.display = "none";

        alert("Prediction failed.");

        console.error(error);
    }
}