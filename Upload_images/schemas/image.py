from marshmallow import Schema, fields
from werkzeug.datastructures import FileStorage

"""
All it does is that get a required FileStorageField,
which has to be called image,
checks it exists, and checks it is a FileStorage.
"""
class FileStorageField(fields.Field):
    default_error_messages = {
        "invalid": "Not a valid image."
    }

    # ImageSchema.load() will run this method
    def _deserialize(self, value, attr, data) -> FileStorage:
        if value is None:
            return None

        if not isinstance(value, FileStorage):
            # fail() is method of fields.Field super class
            # fail() is a helper method that simply raises a `ValidationError`
            self.fail("invalid") # raises VaildationError "Not a valid image."

        return value



class ImageSchema(Schema):
    """
    if that dictionary of request does not have an image key,
    this will fail because you won't have this field as required."""
    image = FileStorageField(required=True)
    """Then it will deserialize
    and it will check that the image is not None
    and it will check that it is indeed a FileStorage.
    """


