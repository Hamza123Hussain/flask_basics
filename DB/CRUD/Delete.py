from flask import jsonify  # For JSON responses
from DB.MongoConnection import get_db  # Database connection
from bson import ObjectId  # To handle MongoDB ObjectId

# Access the database
db = get_db()
items_collection = db["items"]

# Function to delete an item by ID
def delete_item(item_id):
    try:
        # Attempt to delete the document with the given ObjectId
        result = items_collection.delete_one({"_id": ObjectId(item_id)})

        if result.deleted_count == 0:  # No item found to delete
            return jsonify({"error": "Item not found"}), 404

        return jsonify({"message": "Item deleted"}), 200
    except Exception as e:
        # Handle any unexpected errors
        return jsonify({"error": str(e)}), 500
