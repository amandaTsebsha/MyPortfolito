document.addEventListener("DOMContentLoaded", () => {
    //Contact Form submission handler
    const contactForm = document.getElementById("contactForm");
    contactForm.addEventListener("submit", async (event) => {
        event.preventDefault();

        //Get form data

        const formData = new FormData(contactForm);
        const data = {
            name: formData.get("name"),
            email: formData.get("email"),
            message: formData.get("message"),
        };

        try {
            //Send form data to Server

            const response = await fetch("/contact", {
                method: "POST",
                headers: { "Contect-Type": "application/json"},
                body: JSON.stringify(data),
            });

            //Parse Response

            const result = await response.json();
            const responseMessage = document.getElementById("responseMessage");

            if (result.success) {
                responseMessage.textContent = "Message sent successfully!";
                responseMessage.style.color = "green";
                contactForm.reset();

            }
            else {
                responseMessage.textContent = "There was an issue sending your message.";
                responseMessage.style.color = "red";
            }
        }
        catch (error) {
            console.error("Error submitting form: ", error);
        }
    });
});