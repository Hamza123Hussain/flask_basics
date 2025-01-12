from flask import jsonify  # For formatting responses
from DB.MongoConnection import get_db  # Database connection
from bson import ObjectId  # To handle MongoDB ObjectId

# Access the database
db = get_db()
items_collection = db["items"]

# Function to get all items
def get_all_items():
    try:
        # Retrieve all documents from the items collection
        items = list(items_collection.find({}, {"_id": 1, "name": 1, "description": 1}))

        # Convert ObjectId to string for JSON compatibility
        for item in items:
            item["_id"] = str(item["_id"])

        return jsonify(items), 200  # Return the items as a JSON response
    except Exception as e:
        return jsonify({"error": str(e)}), 500  # Handle any errors

# Function to get a single item by ID
def get_item_by_id(item_id):
    try:
        # Find a single document by its ObjectId
        item = items_collection.find_one({"_id": ObjectId(item_id)})

        if not item:  # If no item is found, return a 404 error
            return jsonify({"error": "Item not found"}), 404

        # Convert ObjectId to string for JSON compatibility
        item["_id"] = str(item["_id"])

        return jsonify(item), 200  # Return the item as a JSON response
    except Exception as e:
        return jsonify({"error": str(e)}), 500  # Handle any errors
