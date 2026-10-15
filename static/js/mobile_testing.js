document.addEventListener("DOMContentLoaded", function () {

    initializeModeSelection();

});

function sleep(ms){

    return new Promise(resolve => setTimeout(resolve, ms));

}

function initializeModeSelection() {

    const cards = document.querySelectorAll(".mode-card");

    cards.forEach(card => {

        card.addEventListener("click", function () {

            cards.forEach(c => c.classList.remove("selected"));

            this.classList.add("selected");

            const mode = this.dataset.mode;

            if (mode === "apk") {

                showApkConfiguration();

            }

            else if (mode === "device") {

                showDeviceConfiguration();

            }

            else {

                showEmulatorConfiguration();

            }

        });

    });

}

function showApkConfiguration(){

    const testingMode = document.getElementById("testing-mode");
    const targetConfiguration = document.getElementById("target-configuration");
    const analysisSummary = document.getElementById("analysis-summary");
    const launchButton = document.getElementById("launch-analysis");

    testingMode.textContent = "APK Static Analysis";

    launchButton.disabled = true;

    targetConfiguration.innerHTML = `

<div class="upload-zone" id="upload-zone">

    <div class="upload-icon">

        📦

    </div>

    <div class="upload-title">

        Drop APK Here

    </div>

    <div class="upload-subtitle">

        or Click to Browse APK

    </div>

    <div class="upload-format">

        Supported Format : .apk

    </div>

    <input
        type="file"
        id="apk-file"
        accept=".apk"
        class="hidden-input">

</div>

`;

    const uploadZone = document.getElementById("upload-zone");
    const apkInput = document.getElementById("apk-file");

    uploadZone.onclick = function(){

        apkInput.click();

    };

    apkInput.onchange = function(){

        if(this.files.length > 0){

            const file = this.files[0];
            window.selectedAPK = file;
            const fileSize = (file.size/(1024*1024)).toFixed(2);

            targetConfiguration.innerHTML = `

<div class="apk-info-card">

    <div class="apk-info-header">

        <div class="apk-icon">

            📦

        </div>

        <div class="apk-info-title">

            Android Application Ready

        </div>

    </div>

    <div class="apk-details">

        <div class="detail-label">

            File Name

        </div>

        <div class="detail-value">

            ${file.name}

        </div>

        <div class="detail-label">

            File Size

        </div>

        <div class="detail-value">

            ${fileSize} MB

        </div>

        <div class="detail-label">

            Target

        </div>

        <div class="detail-value">

            Android Application (APK)

        </div>

        <div class="detail-label">

            Status

        </div>

        <div class="detail-value status-ready">

            ✓ Ready for Analysis

        </div>

    </div>

</div>

`;

            launchButton.disabled = false;

        }

    };

    analysisSummary.innerHTML = `

<div class="validation-card">

    <div class="validation-item">

        <span class="validation-title">

            Android Application Loaded

        </span>

        <span class="validation-status">

            ✓ READY

        </span>

    </div>

    <div class="validation-item">

        <span class="validation-title">

            Mobile Application Engine

        </span>

        <span class="validation-status">

            ✓ READY

        </span>

    </div>

    <div class="validation-item">

        <span class="validation-title">

            Mobile Communication Engine

        </span>

        <span class="validation-status">

            ✓ READY

        </span>

    </div>

    <div class="validation-item">

        <span class="validation-title">

            Mobile Device Engine

        </span>

        <span class="validation-status">

            ✓ READY

        </span>

    </div>

    <div class="validation-item">

        <span class="validation-title">

            Mobile OS Engine

        </span>

        <span class="validation-status">

            ✓ READY

        </span>

    </div>

    <div class="validation-item">

        <span class="validation-title">

            Mobile SIM Engine

        </span>

        <span class="validation-status">

            ✓ READY

        </span>

    </div>

    <div class="validation-item">

        <span class="validation-title">

            Report Engine

        </span>

        <span class="validation-status">

            ✓ READY

        </span>

    </div>

    <div class="validation-item">

        <span class="validation-title">

            PDF Generator

        </span>

        <span class="validation-status">

            ✓ READY

        </span>

    </div>

    <div class="validation-overall">

        <h3>

            READY FOR ANALYSIS

        </h3>

        <p>

            All required CALARIT intelligent engines have been initialized successfully.

        </p>

    </div>

</div>

`;

    initializeLaunchButton();

}


function showDeviceConfiguration() {

    const testingMode = document.getElementById("testing-mode");
    const targetConfiguration = document.getElementById("target-configuration");
    const analysisSummary = document.getElementById("analysis-summary");
    const launchButton = document.getElementById("launch-analysis");

    launchButton.disabled = true;

    testingMode.textContent = "Connected Android Device Assessment";

    targetConfiguration.innerHTML = `

        <div class="apk-info-card">

            <div class="apk-info-header">

                <div class="apk-icon">
                    📲
                </div>

                <div class="apk-info-title">
                    Android Device
                </div>

            </div>

            <div class="apk-details">

                <div class="detail-label">
                    Connection Status
                </div>

                <div class="detail-value">
                    No Device Connected
                </div>

                <div class="detail-label">
                    USB Connection
                </div>

                <div class="detail-value">
                    Waiting for Device
                </div>

                <div class="detail-label">
                    USB Debugging
                </div>

                <div class="detail-value">
                    Unknown
                </div>

                <div class="detail-label">
                    Status
                </div>

                <div class="detail-value">
                    Waiting for Detection
                </div>

            </div>

            <button
                class="detect-btn"
                id="detect-device">

                📲 Detect Connected Device

            </button>

        </div>

    `;

    analysisSummary.innerHTML = `

        <div class="validation-card">

            <div class="validation-item">

                <span class="validation-title">

                    Android Device

                </span>

                <span class="validation-status">

                    WAITING

                </span>

            </div>

            <div class="validation-item">

                <span class="validation-title">

                    Mobile Engines

                </span>

                <span class="validation-status">

                    WAITING

                </span>

            </div>

            <div class="validation-overall">

                <h3>

                    WAITING FOR DEVICE

                </h3>

                <p>

                    Connect an Android device to continue.

                </p>

            </div>

        </div>

    `;

    initializeDeviceDetection();

}

function initializeDeviceDetection() {

    const detectButton = document.getElementById("detect-device");

    const targetConfiguration = document.getElementById("target-configuration");

    const analysisSummary = document.getElementById("analysis-summary");

    const launchButton = document.getElementById("launch-analysis");

    detectButton.addEventListener("click", function () {

        const deviceInfo = {

    name: "Samsung Galaxy S24",

    android_version: "Android 15",

    battery: "82%",

    usb_connection: "Connected",

    usb_debugging: "Enabled",

    status: "Ready for Analysis"

};

        targetConfiguration.innerHTML = `

            <div class="apk-info-card">

                <div class="apk-info-header">

                    <div class="apk-icon">

                        📲

                    </div>

                    <div class="apk-info-title">

                        Connected Android Device

                    </div>

                </div>

                <div class="apk-details">

                    <div class="detail-label">
                        Device
                    </div>

                    <div class="detail-value">
                       ${deviceInfo.name}
                    </div>

                    <div class="detail-label">
                        Android Version
                    </div>

                    <div class="detail-value">
                        ${deviceInfo.android_version}
                    </div>

                    <div class="detail-label">
                        USB Connection
                    </div>

                    <div class="detail-value status-ready">
                        ${deviceInfo.usb_connection}
                    </div>

                    <div class="detail-label">
                        USB Debugging
                    </div>

                    <div class="detail-value status-ready">
                       ${deviceInfo.usb_debugging}
                    </div>

                    <div class="detail-label">
                        Battery
                    </div>

                    <div class="detail-value">
                        ${deviceInfo.battery}
                    </div>

                    <div class="detail-label">
                        Status
                    </div>

                    <div class="detail-value status-ready">
                        ✓ ${deviceInfo.status}
                    </div>

                </div>

            </div>

        `;

        analysisSummary.innerHTML = `

            <div class="validation-card">

                <div class="validation-item">

                    <span class="validation-title">

                        Android Device Connected

                    </span>

                    <span class="validation-status">

                        ✓ READY

                    </span>

                </div>

                <div class="validation-item">

                    <span class="validation-title">

                        Mobile Application Engine

                    </span>

                    <span class="validation-status">

                        ✓ READY

                    </span>

                </div>

                <div class="validation-item">

                    <span class="validation-title">

                        Mobile Communication Engine

                    </span>

                    <span class="validation-status">

                        ✓ READY

                    </span>

                </div>

                <div class="validation-item">

                    <span class="validation-title">

                        Mobile Device Engine

                    </span>

                    <span class="validation-status">

                        ✓ READY

                    </span>

                </div>

                <div class="validation-item">

                    <span class="validation-title">

                        Mobile OS Engine

                    </span>

                    <span class="validation-status">

                        ✓ READY

                    </span>

                </div>

                <div class="validation-item">

                    <span class="validation-title">

                        Mobile SIM Engine

                    </span>

                    <span class="validation-status">

                        ✓ READY

                    </span>

                </div>

                <div class="validation-item">

                    <span class="validation-title">

                        Report Engine

                    </span>

                    <span class="validation-status">

                        ✓ READY

                    </span>

                </div>

                <div class="validation-item">

                    <span class="validation-title">

                        PDF Generator

                    </span>

                    <span class="validation-status">

                        ✓ READY

                    </span>

                </div>

                <div class="validation-overall">

                    <h3>

                        READY FOR ANALYSIS

                    </h3>

                    <p>

                        Android device connected successfully.

                    </p>

                </div>

            </div>

        `;

        launchButton.disabled = false;
        initializeLaunchButton();

    });

}

function showEmulatorConfiguration() {

    const testingMode = document.getElementById("testing-mode");
    const targetConfiguration = document.getElementById("target-configuration");
    const analysisSummary = document.getElementById("analysis-summary");
    const launchButton = document.getElementById("launch-analysis");

    launchButton.disabled = true;

    testingMode.textContent = "Android Emulator Assessment";

    targetConfiguration.innerHTML = `

        <div class="apk-info-card">

            <div class="apk-info-header">

                <div class="apk-icon">

                    💻

                </div>

                <div class="apk-info-title">

                    Android Emulator

                </div>

            </div>

            <div class="apk-details">

                <div class="detail-label">

                    Emulator Status

                </div>

                <div class="detail-value">

                    No Emulator Running

                </div>

                <div class="detail-label">

                    AVD Name

                </div>

                <div class="detail-value">

                    Not Detected

                </div>

                <div class="detail-label">

                    Android Version

                </div>

                <div class="detail-value">

                    Unknown

                </div>

                <div class="detail-label">

                    ADB Connection

                </div>

                <div class="detail-value">

                    Waiting

                </div>

                <div class="detail-label">

                    Status

                </div>

                <div class="detail-value">

                    Waiting for Detection

                </div>

            </div>

            <button
                class="detect-btn"
                id="detect-emulator">

                💻 Detect Emulator

            </button>

        </div>

    `;

    analysisSummary.innerHTML = `

        <div class="validation-card">

            <div class="validation-item">

                <span class="validation-title">

                    Emulator Detection

                </span>

                <span class="validation-status">

                    WAITING

                </span>

            </div>

            <div class="validation-item">

                <span class="validation-title">

                    CALARIT Engines

                </span>

                <span class="validation-status">

                    WAITING

                </span>

            </div>

            <div class="validation-overall">

                <h3>

                    WAITING FOR EMULATOR

                </h3>

                <p>

                    Launch an Android Emulator to continue.

                </p>

            </div>

        </div>

    `;

    initializeEmulatorDetection();

}
function initializeEmulatorDetection() {

    const detectButton = document.getElementById("detect-emulator");

    const targetConfiguration = document.getElementById("target-configuration");

    const analysisSummary = document.getElementById("analysis-summary");

    const launchButton = document.getElementById("launch-analysis");

    detectButton.addEventListener("click", function () {

        const emulatorInfo = {

            avd_name: "Pixel_8_API_35",

            android_version: "Android 15",

            architecture: "x86_64",

            adb_status: "Connected",

            status: "Ready for Analysis"

        };

        targetConfiguration.innerHTML = `

            <div class="apk-info-card">

                <div class="apk-info-header">

                    <div class="apk-icon">

                        💻

                    </div>

                    <div class="apk-info-title">

                        Android Emulator

                    </div>

                </div>

                <div class="apk-details">

                    <div class="detail-label">

                        AVD Name

                    </div>

                    <div class="detail-value">

                        ${emulatorInfo.avd_name}

                    </div>

                    <div class="detail-label">

                        Android Version

                    </div>

                    <div class="detail-value">

                        ${emulatorInfo.android_version}

                    </div>

                    <div class="detail-label">

                        Architecture

                    </div>

                    <div class="detail-value">

                        ${emulatorInfo.architecture}

                    </div>

                    <div class="detail-label">

                        ADB Connection

                    </div>

                    <div class="detail-value status-ready">

                        ${emulatorInfo.adb_status}

                    </div>

                    <div class="detail-label">

                        Status

                    </div>

                    <div class="detail-value status-ready">

                        ✓ ${emulatorInfo.status}

                    </div>

                </div>

            </div>

        `;

        analysisSummary.innerHTML = `

            <div class="validation-card">

                <div class="validation-item">

                    <span class="validation-title">

                        Android Emulator Connected

                    </span>

                    <span class="validation-status">

                        ✓ READY

                    </span>

                </div>

                <div class="validation-item">

                    <span class="validation-title">

                        Emulator Environment

                    </span>

                    <span class="validation-status">

                        ✓ READY

                    </span>

                </div>

                <div class="validation-item">

                    <span class="validation-title">

                        Mobile Application Engine

                    </span>

                    <span class="validation-status">

                        ✓ READY

                    </span>

                </div>

                <div class="validation-item">

                    <span class="validation-title">

                        Mobile Communication Engine

                    </span>

                    <span class="validation-status">

                        ✓ READY

                    </span>

                </div>

                <div class="validation-item">

                    <span class="validation-title">

                        Mobile Device Engine

                    </span>

                    <span class="validation-status">

                        ✓ READY

                    </span>

                </div>

                <div class="validation-item">

                    <span class="validation-title">

                        Mobile OS Engine

                    </span>

                    <span class="validation-status">

                        ✓ READY

                    </span>

                </div>

                <div class="validation-item">

                    <span class="validation-title">

                        Mobile SIM Engine

                    </span>

                    <span class="validation-status">

                        ✓ READY

                    </span>

                </div>

                <div class="validation-item">

                    <span class="validation-title">

                        Report Engine

                    </span>

                    <span class="validation-status">

                        ✓ READY

                    </span>

                </div>

                <div class="validation-item">

                    <span class="validation-title">

                        PDF Generator

                    </span>

                    <span class="validation-status">

                        ✓ READY

                    </span>

                </div>

                <div class="validation-overall">

                    <h3>

                        READY FOR ANALYSIS

                    </h3>

                    <p>

                        Android Emulator detected successfully.

                    </p>

                </div>

            </div>

        `;

        launchButton.disabled = false;
        initializeLaunchButton();

    });

}

function updateEngineStatus(engineId, statusId, text, cssClass){

    const card = document.getElementById(engineId);

    const status = document.getElementById(statusId);

    status.className = "engine-status";

    status.classList.add(cssClass);

    status.textContent = text;

    card.scrollIntoView({

        behavior:"smooth",

        block:"center"

    });

}

async function runApplicationEngine(){

    updateEngineStatus(
        "application-engine",
        "application-status",
        "INITIALIZING",
        "initializing"
    );

    await sleep(1000);

    updateEngineStatus(
        "application-engine",
        "application-status",
        "RUNNING",
        "running"
    );

    await sleep(2000);

    updateEngineStatus(
        "application-engine",
        "application-status",
        "COMPLETED",
        "completed"
    );

}

async function launchAnalysis(){

    const launchButton = document.getElementById("launch-analysis");

    launchButton.disabled = true;

    launchButton.innerHTML = "⬆ Uploading APK...";

    if(window.selectedAPK){

        const formData = new FormData();

        formData.append(
            "apk",
            window.selectedAPK
        );

        const response = await fetch(
            "/mobile-testing/upload-apk/",
            {

                method: "POST",

                headers:{

                    "X-CSRFToken": getCSRFToken()

                },

                body: formData

            }

        );

        const result = await response.json();

        console.log("CALARIT Response");

        console.log(result);

        console.log(result.application_engine);

    }

    launchButton.innerHTML = "⚙ Initializing CALARIT...";

    await sleep(1000);

    launchButton.innerHTML = "📱 Mobile Application Engine...";
    await runApplicationEngine();

    launchButton.innerHTML = "📡 Mobile Communication Engine...";
    await runCommunicationEngine();

    launchButton.innerHTML = "📲 Mobile Device Engine...";
    await runDeviceEngine();

    launchButton.innerHTML = "⚙ Mobile OS Engine...";
    await runOSEngine();

    launchButton.innerHTML = "📶 Mobile SIM Engine...";
    await runSIMEngine();

    launchButton.innerHTML = "📝 Report Engine...";
    await runReportEngine();

    launchButton.innerHTML = "📄 PDF Generator...";
    await runPDFEngine();

    launchButton.innerHTML = "✅ Analysis Completed";

}

async function runCommunicationEngine(){

    updateEngineStatus(
        "communication-engine",
        "communication-status",
        "INITIALIZING",
        "initializing"
    );

    await sleep(1000);

    updateEngineStatus(
        "communication-engine",
        "communication-status",
        "RUNNING",
        "running"
    );

    await sleep(2000);

    updateEngineStatus(
        "communication-engine",
        "communication-status",
        "COMPLETED",
        "completed"
    );

}


async function runDeviceEngine(){

    updateEngineStatus(
        "device-engine",
        "device-status",
        "INITIALIZING",
        "initializing"
    );

    await sleep(1000);

    updateEngineStatus(
        "device-engine",
        "device-status",
        "RUNNING",
        "running"
    );

    await sleep(2000);

    updateEngineStatus(
        "device-engine",
        "device-status",
        "COMPLETED",
        "completed"
    );

}


async function runOSEngine(){

    updateEngineStatus(
        "os-engine",
        "os-status",
        "INITIALIZING",
        "initializing"
    );

    await sleep(1000);

    updateEngineStatus(
        "os-engine",
        "os-status",
        "RUNNING",
        "running"
    );

    await sleep(2000);

    updateEngineStatus(
        "os-engine",
        "os-status",
        "COMPLETED",
        "completed"
    );

}


async function runSIMEngine(){

    updateEngineStatus(
        "sim-engine",
        "sim-status",
        "INITIALIZING",
        "initializing"
    );

    await sleep(1000);

    updateEngineStatus(
        "sim-engine",
        "sim-status",
        "RUNNING",
        "running"
    );

    await sleep(2000);

    updateEngineStatus(
        "sim-engine",
        "sim-status",
        "COMPLETED",
        "completed"
    );

}


async function runReportEngine(){

    await sleep(1000);

}

async function runPDFEngine(){

    await sleep(1000);

}



function initializeLaunchButton(){

    const launchButton = document.getElementById("launch-analysis");

    if(!launchButton){

        return;

    }

    launchButton.removeEventListener("click", launchAnalysis);

    launchButton.addEventListener("click", launchAnalysis);

}
function initializeLaunchButton(){

    const launchButton = document.getElementById("launch-analysis");

    if(!launchButton){

        return;

    }

    launchButton.removeEventListener("click", launchAnalysis);

    launchButton.addEventListener("click", launchAnalysis);


}

function getCSRFToken(){

    const cookie = document.cookie
        .split("; ")
        .find(row=>row.startsWith("csrftoken="));

    if(!cookie){

        return "";
    }

    return cookie.split("=")[1];

}