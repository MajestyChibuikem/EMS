// Target containers and form fields
const regContainer = document.querySelector('.reg-container'); // Class selector for container
const registrationForm = document.querySelector('#registration-form'); //target the form
const displayMsg = document.querySelector('#message'); //target the message 
const registerButton = document.querySelector('#register-button'); //target the registerbutton

// Validate form fields
function ValidateForm() {
    // Get the fullname and reg number and trim out white spaces
    const fullName = document.getElementById('full-name').value.trim();
    const regNumber = document.getElementById('registration-number').value.trim();

    // If fullname is empty
    //this method checks if full name field is empty and outputs an error message if true
    //the message is given a color of red
    if (!fullName) {
        displayMsg.textContent = "Full Name is required!";
        displayMsg.style.color = "red";
        return false;
    }

    // If reg number is empty
    //this method checks if regnumber field is empty and outputs an error message if true
    //the message is given a color of red
    if (!regNumber) {
        displayMsg.textContent = "Registration Number is required!";
        displayMsg.style.color = "red";
        return false;
    }
    return true;
}

// Event listener for the register button
//this method listens for when the register button is clicked to run
registerButton.addEventListener('click', async (event) => {
    event.preventDefault(); //this prevents the form from acting on the default submission

    // this methos uses the validateform method from app.py
    //validate form method checks for empty fields and appends when succesful
    //if validateform is false, return, else append the values of the fullname and regnumber to the array

    if (!ValidateForm()) return;

    // Collect form data
    const formData = {
        'full_name': document.getElementById('full-name').value,
        'reg_number': document.getElementById('registration-number').value
    };

    //send the formdata as a string to the submitregistration route and await the response
    try {
        const response = await fetch('/submit-registration', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify(formData),
        });
        
        const result = await response.json(); //result is converted back to json

        //given the response, print out the message for true or one for false
        if (response.ok) {
            displayMsg.textContent = result.message;
            displayMsg.style.color = "green";
            registrationForm.reset(); // Reset form on success
        } else {
            displayMsg.textContent = result.message;
            displayMsg.style.color = "red";
        }
    } catch (error) {
        displayMsg.textContent = "Application encountered an error, please try again.";
        displayMsg.style.color = "red";
    }
});