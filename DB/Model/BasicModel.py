from bson import ObjectId  # This helps handle MongoDB's ObjectId for unique IDs

class Item:
    def __init__(self, name, description, _id=None):
        """
        Constructor to initialize the Item object.
        
        :param name: The name of the item (string)
        :param description: The description of the item (string)
        :param _id: The unique ID of the item (optional)
        """
        self.name = name  # Item's name
        self.description = description  # Item's description
        self._id = _id if _id else str(ObjectId())  # Generate a new ObjectId if not provided

    def to_dict(self):
        """
        Convert the Item object into a dictionary format that can be used in MongoDB.
        
        :return: Dictionary representation of the Item.
        """
        return {
            "_id": self._id,  # The unique ID of the item
            "name": self.name,  # The name of the item
            "description": self.description  # The description of the item
        }

    @classmethod
    def from_dict(cls, data):
        """
        Convert a dictionary (from MongoDB) back into an Item object.
        
        :param data: The dictionary representation of the item (from MongoDB)
        :return: An instance of the Item class.
        """
        return cls(
            name=data["name"],  # Assign the name from the dictionary
            description=data["description"],  # Assign the description from the dictionary
            _id=data.get("_id")  # Use the _id if present (from MongoDB)
        )
