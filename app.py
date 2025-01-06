# Import the Flask class from the flask module
from flask import Flask

# Create an instance of the Flask class.
# The __name__ variable is used to determine the root path of the application.
app = Flask(__name__)

# Define a route for the root URL ('/').
# When a user visits 'http://127.0.0.1:8000/', this function will be triggered.
@app.route('/')
def hell0():
    # Return a simple string as the response.
    return 'I am running on flask'

# Define another route for the '/product' URL.
# When a user visits 'http://127.0.0.1:8000/product', this function will be triggered.
@app.route('/product')
def products():
    # Return a string describing the products.
    return 'We are selling some product here'

# This block ensures the application runs only when executed directly.
# It prevents the code from running if the file is imported as a module elsewhere.
if __name__ == '__main__':
    # Run the Flask application.
    # - `debug=True` enables debug mode, which provides detailed error messages and auto-reloads the server when changes are made to the code.
    # - `port=8000` specifies the port the server should run on (default is 5000 if not specified).
    app.run(debug=True, port=8000)
