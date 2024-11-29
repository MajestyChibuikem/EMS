document.addEventListener('DOMContentLoaded', () => {
    const loginForm = document.getElementById('login-form');//target the login form although this not needed
    const loginButton = document.getElementById('login-button'); // target thr login button
    const displayMsg = document.getElementById('message'); //target the display message

    loginButton.addEventListener('click', async (event) => {
        event.preventDefault(); //prevent default form submission
    
        const regNumber = document.getElementById('registration-number').value.trim(); //get the trimmed regnumber value
        const full_name = document.getElementById('full-name').value.trim();
        //check if the input fields are empty
        if (!regNumber) {
            displayMsg.textContent = "Registration Number is required!";
            displayMsg.style.color = "red";
            return;
        }
        if(!full_name){
            displayMsg.textContent = "full name is required";
            displayMsg.style.color = "red";
        }

        //get values and assign them into the json format
        const formData = {
            full_name: document.getElementById('full-name').value.trim(),
            reg_number: document.getElementById('registration-number').value.trim(),
        };
        

        try {
            const response = await fetch('/validate-login', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json',
                },
                body: JSON.stringify(formData),
            });

            const result = await response.json();

            if (response.ok) {
                displayMsg.textContent = result.message;
                displayMsg.style.color = "green";
            } else {
                displayMsg.textContent = result.message;
                displayMsg.style.color = "red";
            }
        } catch (error) {
            displayMsg.textContent = "An error occurred, please try again.";
            displayMsg.style.color = "red";
        }
    });
});
