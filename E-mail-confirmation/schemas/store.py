from ma import ma
from models.store import StoreModel
from models.item import ItemModel
from schemas.item import ItemSchema


class StoreSchema(ma.ModelSchema):
    # store contain many items
    # ma is our Flask-Marshmallow app. 
    # which is linked to our Flask app,
    items = ma.Nested(ItemSchema, many=True)

    class Meta:
        model = StoreModel
        dump_only = ("id",)
        include_fk = True
