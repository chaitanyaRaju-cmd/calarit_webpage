const steps = [

    { percent: 5, task: "🔍 Website Availability Analysis" },

    { percent: 10, task: "🔒 HTTPS Configuration Analysis" },

    { percent: 15, task: "🛡️ SSL Certificate Analysis" },

    { percent: 20, task: "🍪 Cookie Security Analysis" },

    { percent: 25, task: "🔗 Broken Link Analysis" },

    { percent: 30, task: "🤖 Robots.txt Analysis" },

    { percent: 35, task: "🗺️ Sitemap.xml Validation" },

    { percent: 40, task: "📱 Mobile Friendly Analysis" },

    { percent: 45, task: "📂 Sensitive Files Detection" },

    { percent: 50, task: "💻 Technology Detection" },

    { percent: 55, task: "📁 Directory Listing Analysis" },

    { percent: 60, task: "⚡ Performance Analysis" },

    { percent: 65, task: "♿ Accessibility Analysis" },

    { percent: 70, task: "🌐 Domain Information Analysis" },

    { percent: 75, task: "📧 Email Security Analysis" },

    { percent: 80, task: "🚪 Open Ports Analysis" },

    { percent: 85, task: "📊 Calculating Website Health Score" },

    { percent: 90, task: "📝 Generating Executive Summary" },

    { percent: 95, task: "📄 Building Detailed Report" },

    { percent: 98, task: "📥 Preparing Professional PDF Report" },

    { percent: 100, task: "✅ Finalizing Results Dashboard" }

];

const progressBar =
document.getElementById("progress-bar");

const progressPercent =
document.getElementById("progress-percent");

const currentStep =
document.getElementById("current-step");

let index = 0;

function updateProgress(){

   const percent = steps[index].percent;

    progressBar.style.width =
    percent + "%";

    progressPercent.innerText =
    Math.floor(percent) + "%";

    currentStep.innerText =
    steps[index].task;

    index++;

    if(index >= steps.length){

    clearInterval(interval);

    currentStep.innerText =
    "✅ Testing Completed";

    setTimeout(function(){

        currentStep.innerText =
        "📊 Opening Results Dashboard...";

    }, 1000);

    setTimeout(function(){

        window.location.href =
        "/results/";

    }, 2500);
}
}

const interval =
setInterval(updateProgress, 1500);
document
.getElementById(
    "cancelTesting"
)
.addEventListener(
    "click",
    function(){

        clearInterval(
            interval
        );

        window.location.href =
        "/dashboard/";

    }
);