const form =
document.querySelector("form");

const urlInput =
document.getElementById("websiteUrl");

const errorBox =
document.getElementById("urlError");

form.addEventListener(
    "submit",
    function(event){

        const url =
        urlInput.value.trim();

        if(url === ""){

            event.preventDefault();

            urlInput.classList.add(
                "input-error"
            );

            errorBox.style.display =
            "block";

            errorBox.innerText =
            "Please enter a website URL.";

            urlInput.focus();

            return;
        }

        const websitePattern =
        /^(https?:\/\/)([a-zA-Z0-9-]+\.)+[a-zA-Z]{2,}(\/.*)?$/;

        if(!websitePattern.test(url)){

            event.preventDefault();

            urlInput.classList.add(
                "input-error"
            );

            errorBox.style.display =
            "block";

            errorBox.innerText =
            "Please enter a valid website URL (Example: https://example.com)";

            urlInput.focus();

            return;
        }

        urlInput.classList.remove(
            "input-error"
        );

        errorBox.style.display =
        "none";
    }
);