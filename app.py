from flask import Flask
from Mongo  import item_routes

app = Flask(__name__)

# Register the Blueprint for item routes
app.register_blueprint(item_routes)

# Define the home route for basic testing
@app.route('/')
def home():
    return "Flask app deployed on Vercel!", 200


# This block ensures the application runs only when executed directly.
# It prevents the code from running if the file is imported as a module elsewhere.
if __name__ == '__main__':
    # Run the Flask application.
    # - `debug=True` enables debug mode, which provides detailed error messages and auto-reloads the server when changes are made to the code.
    # - `port=8000` specifies the port the server should run on (default is 5000 if not specified).
    app.run(debug=True, port=8000)

