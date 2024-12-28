// Wait for the DOM to load
document.addEventListener("DOMContentLoaded", function () {
    const projectLinks = document.querySelectorAll(".project-link");

    // Handle project navigation
    projectLinks.forEach(link => {
        link.addEventListener("click", function (event) {
            event.preventDefault(); // Prevent default link behavior
            const projectUrl = this.getAttribute("data-project");

            if (projectUrl) {
                // Load content dynamically using AJAX
                loadContent(projectUrl, "main-content");
            } else {
                alert("No project linked!"); // Show alert if no project URL is linked
            }
        });
    });

    // Handle form validation
    const form = document.getElementById("example-form");
    form.addEventListener("submit", function (event) {
        let isValid = true;

        // Check all required inputs
        const inputs = form.querySelectorAll("input[required]");
        inputs.forEach(input => {
            const errorMessage = input.nextElementSibling;
            if (!input.value.trim()) {
                errorMessage.textContent = "This field is required.";
                input.classList.add("error");
                isValid = false;
            } else {
                errorMessage.textContent = "";
                input.classList.remove("error");
            }
        });

        // Prevent form submission if invalid
        if (!isValid) {
            event.preventDefault();
        } else {
            alert("Form submitted successfully!");
        }
    });
});

// AJAX function to load content dynamically
function loadContent(url, targetElementId) {
    const targetElement = document.getElementById(targetElementId);

    // Display a loading indicator
    targetElement.innerHTML = "<p>Loading content...</p>";

    // Perform the AJAX request using Fetch API
    fetch(url)
        .then(response => {
            if (!response.ok) {
                throw new Error("Network response was not ok: " + response.statusText);
            }
            return response.text();
        })
        .then(data => {
            targetElement.innerHTML = data; // Inject the fetched content into the target element
        })
        .catch(error => {
            console.error("Error during fetch operation:", error);
            targetElement.innerHTML = "<p>Error loading content. Please try again later.</p>";
        });
}
