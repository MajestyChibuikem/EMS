
#import all flask methods to be used from flask
from flask import (
    Flask,
    render_template,
    request,
    jsonify,
    url_for
)

app = Flask(__name__, static_folder='static', template_folder='templates')

# defined the user array
user_arrays = []


#app route : home is the registration page
@app.route('/')
def home():
    return render_template('registration.html')  # Correct template path


#registration route
@app.route('/register')
def registration():
    return render_template('registration.html')
"""
    this route gets the info from the form, checks if the user doesnt exist
    to save it to the user array
"""
# Submit the registration form
@app.route('/submit-registration', methods=['POST'])
def submit_registration():
    data = request.json # get the data in json format
    user_name = data.get('user_name') #target the fullname value
    password = data.get('password') #target the reg_number value
    email = data.get('email')


    # Log the user_arrays before adding a new user
    print("Before adding:", user_arrays) #debugging

    # Check if user exists
    existing_user = next((user for user in user_arrays if user['email'] == email), None)
    if existing_user:
        return jsonify({"success": False, "message": "User already exists"}), 400

    # Append new user model
    user_arrays.append({
        'user_name': user_name,
        'password': password,
        'email' : email
    })

    #return message
    return jsonify({
        "success": True,
        "message": "User registered successfully",
        "redirect_url": url_for('login')  # Dynamic URL for the login route
    })

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
    user_name = data.get('user_name') #get the fullname value
    password = data.get('password') #get the reg number value
    if not user_name or not password:
        return jsonify({'success': False, 'message': 'Missing required fields'}), 400

    user = next(
        (user for user in user_arrays if user.get('password') == password and user.get('full_name') == user_name),
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
