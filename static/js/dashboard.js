const services = {

   website: {
    title: "🌐 Website Testing",
    content: `
        <h3>What is Website Testing?</h3>

        <p>
            Website Testing is the process of evaluating a website to ensure it is secure,
            reliable, accessible, high-performing, and functions correctly across different
            browsers and devices. It helps identify issues before they affect users or
            business operations.
        </p>

        <h3>Why is it Important?</h3>

        <ul>
            <li>Detects security vulnerabilities before attackers exploit them.</li>
            <li>Improves website performance and loading speed.</li>
            <li>Ensures compatibility across browsers and devices.</li>
            <li>Enhances accessibility for all users.</li>
            <li>Builds user trust and improves website quality.</li>
        </ul>

        <h3>What CALARIT Offers</h3>

        <p>
            CALARIT provides an automated Website Testing platform that performs
            comprehensive security, performance, and quality assessments.
            Our testing engine generates detailed reports with actionable
            recommendations to improve website health.
        </p>

        <h3>What Gets Tested?</h3>

        <ul>
            <li>✓ Website Availability</li>
            <li>✓ HTTPS Configuration</li>
            <li>✓ SSL Certificate Analysis</li>
            <li>✓ Security Headers</li>
            <li>✓ Cookie Security</li>
            <li>✓ Broken Links</li>
            <li>✓ Robots.txt Analysis</li>
            <li>✓ Sitemap.xml Analysis</li>
            <li>✓ Mobile Friendliness</li>
            <li>✓ Sensitive Files Detection</li>
            <li>✓ Technology Detection</li>
            <li>✓ Directory Listing Analysis</li>
            <li>✓ Performance Analysis</li>
            <li>✓ Accessibility Analysis</li>
            <li>✓ Domain Information</li>
            <li>✓ Email Security</li>
            <li>✓ Open Ports Analysis</li>
            <li>✓ Overall Website Health Score</li>
        </ul>
    `
},

    mobile: {

    title: "📱 Mobile Testing",

    content: `
        <h3>What is CALARIT Mobile Testing?</h3>

        <p>
            CALARIT Mobile Testing is an intelligent automated mobile assessment platform
            designed to analyze Android applications, mobile devices, operating systems,
            communication layers, and SIM-related functionality through a unified testing workflow.
            Rather than testing only an application, CALARIT evaluates the complete mobile ecosystem
            to improve security, reliability, compatibility, and performance.
        </p>

        <h3>Why is it Important?</h3>

        <ul>
            <li>Detects mobile application vulnerabilities before deployment.</li>
            <li>Validates compatibility across Android devices and OS versions.</li>
            <li>Analyzes application performance and stability.</li>
            <li>Evaluates communication and network behaviour.</li>
            <li>Improves user experience, reliability and application quality.</li>
        </ul>

        <h3>What CALARIT Offers</h3>

        <p>
            CALARIT provides an intelligent Mobile Testing Engine capable of performing
            comprehensive automated analysis across the complete Android ecosystem.
            The platform generates professional reports, health scores, intelligent
            recommendations, and detailed technical findings to help developers deliver
            secure, reliable, and high-quality mobile applications.
        </p>

        <h3>What Gets Tested?</h3>

        <ul>
            <li>✓ Mobile Application Analysis</li>
            <li>✓ Mobile Communication Analysis</li>
            <li>✓ Mobile Device Analysis</li>
            <li>✓ Mobile Operating System Analysis</li>
            <li>✓ Mobile SIM Analysis</li>
            <li>✓ APK Integrity Validation</li>
            <li>✓ Permission Analysis</li>
            <li>✓ Device Compatibility Assessment</li>
            <li>✓ Android Version Compatibility</li>
            <li>✓ Network Behaviour Analysis</li>
            <li>✓ Installation Validation</li>
            <li>✓ Mobile Security Assessment</li>
            <li>✓ Performance Analysis</li>
            <li>✓ Health Score Generation</li>
            <li>✓ Executive Summary</li>
            <li>✓ Intelligent Recommendations</li>
            <li>✓ Professional CALARIT PDF Report</li>
        </ul>
    `
},

    api: {

        title: "🔌 API Testing",

        description:
        `
        REST API Testing

        SOAP API Testing

        Endpoint Validation

        Integration Testing

        Verify reliability, performance
        and security of backend services.
        `
    },

    security: {

        title: "🛡️ Security Testing",

        description:
        `
        Vulnerability Assessment

        Penetration Testing

        Risk Analysis

        Security Auditing

        Protect your applications from
        threats through comprehensive
        security evaluation.
        `
    }

};


const cards =
document.querySelectorAll(".service-card");

const title =
document.getElementById("service-title");

const description =
document.getElementById("service-description");


cards.forEach(card => {

    card.addEventListener("mouseenter", () => {

        const service =
        card.dataset.service;

        title.innerHTML =
        services[service].title;

        description.innerHTML =
        services[service].content || services[service].description;

    });

});