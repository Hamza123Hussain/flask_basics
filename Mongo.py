from flask import Blueprint  # Import Blueprint
from DB.CRUD.create import create_item  # Import the create_item function
from DB.CRUD.read import get_all_items,get_item_by_id
from DB.CRUD.update import update_item
from DB.CRUD.Delete import delete_item
# Create a Blueprint for item routes
item_routes = Blueprint("item_routes", __name__)
# Route to create an item (POST request)
# Use the function reference (no parentheses)
@item_routes.route("/items", methods=["POST"])
def create_item_route():
    return create_item()  # Call the function when the route is accessed
# Route to get all items (GET request)
@item_routes.route("/items", methods=["GET"])
def get_items_route():
    return get_all_items()  # Call the logic function for retrieving all items
# Route to get a single item by ID (GET request)
@item_routes.route("/items/<string:item_id>", methods=["GET"])
def get_item_route(item_id):
    return get_item_by_id(item_id)  # Call the logic function for retrieving a single item
# Route to update an item by ID (PUT request)
@item_routes.route("/items/<string:item_id>", methods=["PUT"])
def update_item_route(item_id):
    return update_item(item_id)  # Call the logic function for updating an item
# Route to delete an item by ID (DELETE request)
@item_routes.route("/items/<string:item_id>", methods=["DELETE"])
def delete_item_route(item_id):
    return delete_item(item_id)  # Call the logic function for deleting an item