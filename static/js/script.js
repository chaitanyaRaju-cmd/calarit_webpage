/*====================================================

                CALARIT WEBPAGE
        Authentication Module v1.0

====================================================*/

document.addEventListener("DOMContentLoaded", function () {

    let isPasswordResetFlow = false;

    let resetEmail = "";

    /*====================================================

                    ELEMENTS

    ====================================================*/

    const flipCard = document.getElementById("flipCard");

    const showLogin =
        document.getElementById("showLogin");

    const showSignup =
        document.getElementById("showSignup");

    const signupButton =
        document.getElementById("signupButton");

    const loginButton =
        document.getElementById("loginButton");

    const verifyOtp =
        document.getElementById("verifyOtp");

    const sendResetOtp =
    document.getElementById(
        "sendResetOtp"
    );

const resetEmailInput =
    document.getElementById(
        "resetEmailInput"
    );

    const otpModalElement =
        document.getElementById("otpModal");

    const otpModal =
        new bootstrap.Modal(otpModalElement);

    const newPasswordModal =
    new bootstrap.Modal(
        document.getElementById(
            "newPasswordModal"
        )
    );

const resetPasswordBtn =
    document.getElementById(
        "resetPasswordBtn"
    );

const newPassword =
    document.getElementById(
        "newPassword"
    );

const confirmNewPassword =
    document.getElementById(
        "confirmNewPassword"
    );

    /*====================================================

                    SIGNUP INPUTS

    ====================================================*/

    const signupUsername =
        document.getElementById("signupUsername");

    const signupEmail =
        document.getElementById("signupEmail");

    const signupPassword =
        document.getElementById("signupPassword");

    const signupConfirmPassword =
        document.getElementById("signupConfirmPassword");

    /*====================================================

                    LOGIN INPUTS

    ====================================================*/

    const loginUsername =
        document.getElementById("loginUsername");

    const loginPassword =
        document.getElementById("loginPassword");

    /*====================================================

                    OTP INPUT

    ====================================================*/

    const otpInput =
        document.getElementById("otpInput");

    /*====================================================

                    PASSWORD TOGGLES

    ====================================================*/

    const toggleSignupPassword =
        document.getElementById(
            "toggleSignupPassword"
        );

    const toggleSignupConfirmPassword =
        document.getElementById(
            "toggleSignupConfirmPassword"
        );

    const toggleLoginPassword =
        document.getElementById(
            "toggleLoginPassword"
        );

    /*====================================================

                    UTILITY FUNCTIONS

    ====================================================*/

    function trimValue(element) {

        return element.value.trim();

    }

    function clearState(element) {

        element.classList.remove(
            "input-error",
            "input-success"
        );

    }

    function setError(element) {

        element.classList.remove(
            "input-success"
        );

        element.classList.add(
            "input-error"
        );

    }

    function setSuccess(element) {

        element.classList.remove(
            "input-error"
        );

        element.classList.add(
            "input-success"
        );

    }

    function isValidEmail(email) {

        const pattern =
            /^[^\s@]+@[^\s@]+\.[^\s@]+$/;

        return pattern.test(email);

    }

    function focusError(element, message) {

        setError(element);

        element.focus();

        alert(message);

    }
        /*====================================================

            PASSWORD TOGGLE ENGINE

    ====================================================*/

    function togglePasswordVisibility(
        inputElement,
        toggleElement
    ) {

        const icon =
            toggleElement.querySelector(".material-icons");

        if (inputElement.type === "password") {

            inputElement.type = "text";

            if (icon) {

                icon.textContent = "visibility_off";

            }

        }

        else {

            inputElement.type = "password";

            if (icon) {

                icon.textContent = "visibility";

            }

        }

    }

    /*====================================================

            PASSWORD TOGGLE EVENTS

    ====================================================*/

    if (toggleSignupPassword) {

        toggleSignupPassword.addEventListener(

            "click",

            function () {

                togglePasswordVisibility(

                    signupPassword,

                    toggleSignupPassword

                );

            }

        );

    }

    if (toggleSignupConfirmPassword) {

        toggleSignupConfirmPassword.addEventListener(

            "click",

            function () {

                togglePasswordVisibility(

                    signupConfirmPassword,

                    toggleSignupConfirmPassword

                );

            }

        );

    }

    if (toggleLoginPassword) {

        toggleLoginPassword.addEventListener(

            "click",

            function () {

                togglePasswordVisibility(

                    loginPassword,

                    toggleLoginPassword

                );

            }

        );

    }

    /*====================================================

                FLIP CARD SUPPORT

    ====================================================*/

    if (showLogin) {

        showLogin.addEventListener(

            "click",

            function () {

                flipCard.classList.add("flip");

            }

        );

    }

    if (showSignup) {

        showSignup.addEventListener(

            "click",

            function () {

                flipCard.classList.remove("flip");

            }

        );

    }

/*====================================================

            forget password link

====================================================*/

    const forgotPasswordLink =
    document.getElementById(
        "forgotPasswordLink"
    );

if (forgotPasswordLink) {

    forgotPasswordLink.addEventListener(

        "click",

        function (event) {

            event.preventDefault();

           const resetEmailModal =
    new bootstrap.Modal(
        document.getElementById(
            "resetEmailModal"
        )
    );

resetEmailModal.show();

        }

    );

}

/*====================================================

            RESET PASSWORD OTP

====================================================*/

if (sendResetOtp) {

    sendResetOtp.addEventListener(

        "click",

        async function () {

            const email =
                resetEmailInput.value.trim();

            if (!email) {

                alert(
                    "Please enter your email."
                );

                resetEmailInput.focus();

                return;

            }

            try {

                const response =
                    await fetch(

                        `/forgot-password-otp/?email=${encodeURIComponent(email)}`

                    );

                const result =
                    await response.json();

                if (!result.success) {

                    alert(
                        result.message
                    );

                    return;

                }

                alert(
                    "OTP sent successfully."
                );

                bootstrap.Modal
                    .getInstance(
                        document.getElementById(
                            "resetEmailModal"
                        )
                    )
                    .hide();

                resetEmail = email;

                isPasswordResetFlow = true;

                otpModal.show();

            }

            catch (error) {

                console.error(error);

                alert(
                    "Unable to send OTP."
                );

            }

        }

    );

}

    /*====================================================

                RESET INPUT STATES

    ====================================================*/

    function resetSignupState() {

        clearState(signupUsername);

        clearState(signupEmail);

        clearState(signupPassword);

        clearState(signupConfirmPassword);

    }

    function resetLoginState() {

        clearState(loginUsername);

        clearState(loginPassword);

    }

    /*====================================================

                PASSWORD VALIDATION

    ====================================================*/

    function isStrongPassword(password) {

        if (password.length < 8) {

            return false;

        }

        return true;

    }

    /*====================================================

                USERNAME VALIDATION

    ====================================================*/

    function isValidUsername(username) {

        if (username.length < 3) {

            return false;

        }

        return true;

    }
        /*====================================================

                SIGNUP VALIDATION

    ====================================================*/

    function validateSignup() {

        resetSignupState();

        const username =
            trimValue(signupUsername);

        const email =
            trimValue(signupEmail);

        const password =
            trimValue(signupPassword);

        const confirmPassword =
            trimValue(signupConfirmPassword);

        /*==============================
                Username
        ==============================*/

        if (username === "") {

            focusError(

                signupUsername,

                "Username is required."

            );

            return false;

        }

        if (!isValidUsername(username)) {

            focusError(

                signupUsername,

                "Username must contain at least 3 characters."

            );

            return false;

        }

        setSuccess(signupUsername);

        /*==============================
                    Email
        ==============================*/

        if (email === "") {

            focusError(

                signupEmail,

                "Email is required."

            );

            return false;

        }

        if (!isValidEmail(email)) {

            focusError(

                signupEmail,

                "Please enter a valid email address."

            );

            return false;

        }

        setSuccess(signupEmail);

        /*==============================
                Password
        ==============================*/

        if (password === "") {

            focusError(

                signupPassword,

                "Password is required."

            );

            return false;

        }

        if (!isStrongPassword(password)) {

            focusError(

                signupPassword,

                "Password must contain at least 8 characters."

            );

            return false;

        }

        setSuccess(signupPassword);

        /*==============================
            Confirm Password
        ==============================*/

        if (confirmPassword === "") {

            focusError(

                signupConfirmPassword,

                "Please confirm your password."

            );

            return false;

        }

        if (password !== confirmPassword) {

            setError(signupPassword);

            setError(signupConfirmPassword);

            signupConfirmPassword.focus();

            alert("Passwords do not match.");

            return false;

        }

        setSuccess(signupConfirmPassword);

        return true;

    }

/*====================================================

            SIGNUP BUTTON

====================================================*/

if (signupButton) {

    signupButton.addEventListener(

        "click",

        async function () {

            if (

                !validateSignup()

            ) {

                return;

            }

            try {

                const username =
                    signupUsername.value.trim();

                const email =
                    signupEmail.value.trim();

                const password =
                    signupPassword.value.trim();

                const response =
                    await fetch(

                        `/generate-otp/?username=${encodeURIComponent(username)}&email=${encodeURIComponent(email)}&password=${encodeURIComponent(password)}`

                    );

                const result =
                    await response.text();

                console.log(result);

                if (

                    result.includes(
                        "Email already registered"
                    )

                ) {

                    alert(
                        "Email already registered."
                    );

                    return;

                }

                if (

                    result.includes(
                        "Username already exists"
                    )

                ) {

                    alert(
                        "Username already exists."
                    );

                    return;

                }

                otpModal.show();

            }

            catch (error) {

                console.error(error);

                alert(

                    "Unable to send OTP. Please try again."

                );

            }

        }

    );

}
        /*====================================================

                LOGIN VALIDATION

    ====================================================*/

    function validateLogin() {

        resetLoginState();

        const username =
            trimValue(loginUsername);

        const password =
            trimValue(loginPassword);

        /*==============================
                Username
        ==============================*/

        if (username === "") {

            focusError(

                loginUsername,

                "Please enter your username."

            );

            return false;

        }

        setSuccess(loginUsername);

        /*==============================
                Password
        ==============================*/

        if (password === "") {

            focusError(

                loginPassword,

                "Please enter your password."

            );

            return false;

        }

        setSuccess(loginPassword);

        return true;

    }

    /*====================================================

                LOGIN BUTTON

    ====================================================*/

    if (loginButton) {

        loginButton.addEventListener(

            "click",

             async function () {

                if (!validateLogin()) {

                    return;

                }

              try {

    const username =
        loginUsername.value.trim();

    const password =
        loginPassword.value.trim();

    const response =
        await fetch(

            `/login-user/?username=${encodeURIComponent(username)}&password=${encodeURIComponent(password)}`

        );

    const result =
        await response.json();

    console.log(result);
    if (result.success) {

    window.location.href =

        result.redirect;

}

    else {

        alert(

            result.message

        );

    }

}

catch (error) {

    console.error(error);

    alert(

        "Login failed."

    );

}
            }

        );

    }

    /*====================================================

                OTP VERIFICATION

    ====================================================*/

   if (verifyOtp) {

    verifyOtp.addEventListener(

        "click",

        async function () {

            const otp =
                trimValue(otpInput);

            if (otp === "") {

                alert(
                    "Please enter OTP."
                );

                otpInput.focus();

                return;

            }

            try {

                const response =
                    await fetch(

                        `/verify-otp/?otp=${encodeURIComponent(otp)}`

                    );

                const result =
                    await response.json();

                if (!result.success) {

                    alert(
                        result.message
                    );

                    return;

                }

               otpModal.hide();

otpInput.value = "";

if (isPasswordResetFlow) {

    newPasswordModal.show();

}

else {

    flipCard.classList.add("flip");

    setTimeout(function () {

        alert(

            "OTP Verified Successfully!\nPlease Login to Continue."

        );

    }, 500);

}

            }

            catch (error) {

                console.error(error);

                alert(

                    "Verification failed."

                );

            }

        }

    );

}

/*====================================================

            RESET PASSWORD

====================================================*/

if (resetPasswordBtn) {

    resetPasswordBtn.addEventListener(

        "click",

        async function () {

            const password =
                newPassword.value.trim();

            const confirmPassword =
                confirmNewPassword.value.trim();

            if (!password) {

                alert(
                    "Please enter a new password."
                );

                return;

            }

            if (password.length < 8) {

                alert(
                    "Password must contain at least 8 characters."
                );

                return;

            }

            if (password !== confirmPassword) {

                alert(
                    "Passwords do not match."
                );

                return;

            }

            try {

    const response =
        await fetch(

            `/reset-password/?email=${encodeURIComponent(resetEmail)}&password=${encodeURIComponent(password)}`

        );

    const result =
        await response.json();

    if (!result.success) {

        alert(
            result.message
        );

        return;

    }

    newPasswordModal.hide();

    isPasswordResetFlow = false;

    resetEmail = "";

    newPassword.value = "";

    confirmNewPassword.value = "";

    flipCard.classList.add("flip");

    newPasswordModal.hide();

    newPassword.value = "";

    confirmNewPassword.value = "";

    alert(

        "Password Reset Successful!\nPlease login with your new password."

    );

}

catch (error) {

    console.error(error);

    alert(

        "Password reset failed."

    );

}

        }

    );

}

    /*====================================================

                ENTER KEY SUPPORT

    ====================================================*/

    if (otpInput) {

        otpInput.addEventListener(

            "keypress",

            function (event) {

                if (event.key === "Enter") {

                    event.preventDefault();

                    verifyOtp.click();

                }

            }

        );

    }

    /*====================================================

            PREVENT FORM SUBMISSION

    ====================================================*/

    document

        .querySelectorAll("form")

        .forEach(function (form) {

            form.addEventListener(

                "submit",

                function (event) {

                    event.preventDefault();

                }

            );

        });

    /*====================================================

                INITIALIZATION

    ====================================================*/

    console.log(

        "===================================="

    );

    console.log(

        "CALARIT Authentication Module v1.0"

    );

    console.log(

        "Initialization Successful."

    );

    console.log(

        "===================================="

    );

});