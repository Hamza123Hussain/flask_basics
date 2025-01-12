from flask import request, jsonify  # For request handling and JSON responses
from DB.MongoConnection import get_db  # Database connection
from bson import ObjectId  # To handle MongoDB ObjectId

# Access the database
db = get_db()
items_collection = db["items"]

# Function to update an item by ID
def update_item(item_id):
    try:
        # Parse the JSON data sent in the request body
        data = request.json

        # Validate the data to ensure at least one field is provided
        if not data or ("name" not in data and "description" not in data):
            return jsonify({"error": "At least one of 'name' or 'description' is required"}), 400

        # Build the update document
        update_data = {}
        if "name" in data:
            update_data["name"] = data["name"]
        if "description" in data:
            update_data["description"] = data["description"]

        # Update the document in the collection
        result = items_collection.update_one(
            {"_id": ObjectId(item_id)},  # Find by ObjectId
            {"$set": update_data}  # Set the new values
        )

        if result.matched_count == 0:  # No item found to update
            return jsonify({"error": "Item not found"}), 404

        return jsonify({"message": "Item updated"}), 200
    except Exception as e:
        # Handle any unexpected errors
        return jsonify({"error": str(e)}), 500
