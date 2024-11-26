
#import all flask methods to be used from flask
import pprint
from flask import (
    Flask,
    render_template,
    request,
    jsonify
)

app = Flask(__name__)

# defined the user array
user_arrays = []


#app route : home is the registration page
@app.route('/')
def home():
    return render_template('registration.html')  # Correct template path


"""
    this route gets the info from the form, checks if the user doesnt exist
    to save it to the user array
"""
# Submit the registration form
@app.route('/submit-registration', methods=['POST'])
def submit_registration():
    data = request.json # get the data in json format
    full_name = data.get('full_name') #target the fullname value
    reg_number = data.get('reg_number') #target the reg_number value


    # Log the user_arrays before adding a new user
    print("Before adding:", user_arrays) #debugging

    # Check if user exists
    existing_user = next((user for user in user_arrays if user['reg_number'] == reg_number), None)
    if existing_user:
        return jsonify({"success": False, "message": "User already exists"}), 400

    # Append new user model
    user_arrays.append({
        'full_name': full_name,
        'reg_number': reg_number
    })

    #return message
    return jsonify({"success": True, "message": "User registered successfully"})

"""
    the login route 
    this renders the login page
"""
@app.route('/login')
def login():
    return render_template('login.html')

# Validate user login route
"""
    the validate_login method gets the data from the login form in a json format 
    the first if checks the fullname or regnumber field is empty and returns an error message if true
    the values are assigned based on the user model
    the last if statement checks if any value in user is empty, if true, return login succesful, else return invalid credentials
"""
@app.route('/validate-login', methods=['POST'])
def validate_login():
    data = request.json #get the data in json format
    full_name = data.get('full_name') #get the fullname value
    reg_number = data.get('reg_number') #get the reg number value

    if not full_name or not reg_number:
        return jsonify({'success': False, 'message': 'Missing required fields'}), 400

    user = next(
        (user for user in user_arrays if user.get('reg_number') == reg_number and user.get('full_name') == full_name),
        None
    )
    if user:
        return jsonify({'success': True, 'message': 'Login successful'})
    return jsonify({'success': False, 'message': 'Invalid credentials'}), 401


"""
    for development purposes only
    this route has a method that helps me check the values stored in the array on the web
    this route will be removed before distribution
"""
@app.route('/debug-user-arrays', methods=['GET'])
def debug_user_arrays():
    return jsonify(user_arrays)

#run the python-flask application
if __name__ == '__main__':
    app.run(debug=True)
