from flask import request, jsonify  # Import necessary modules for routes and JSON handling
from DB.MongoConnection import get_db  # Import the function to get a database connection

# Access the database using the get_db function
db = get_db()

# Define the collection (table) in the database where items will be stored
items_collection = db["items"]

# Function to handle item creation
def create_item():
    try:
        # Parse JSON data sent in the request body
        data = request.json

        # Validate the data to ensure required fields are present
        if not data or "name" not in data or "description" not in data:
            # Return an error response if data is missing required fields
            return jsonify({"error": "Name and description are required"}), 400

        # Insert the validated data into the MongoDB collection
        item_id = items_collection.insert_one({
            "name": data["name"],  # Extract and store the name
            "description": data["description"]  # Extract and store the description
        }).inserted_id  # Get the ID of the newly inserted item

        # Return a success message along with the ID of the created item
        return jsonify({"message": "Item created", "id": str(item_id)}), 201
    except Exception as e:
        # Handle any unexpected errors and return an error response
        return jsonify({"error": str(e)}), 500
