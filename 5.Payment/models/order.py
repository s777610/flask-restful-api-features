import stripe

from db import db
from typing import List
import os

# """
# This is helper table for many to many relationship
# It will be created by create_all() in app.py"""
# items_to_orders = db.Table(
#     "items_to_orders",
#     db.Column("item_id", db.Integer, db.ForeignKey("items.id")),
#     db.Column("order_id", db.Integer, db.ForeignKey("orders.id"))
# ) # but we don't need this in this case

CURRENCY = "usd"

class ItemsInOrder(db.Model):
    __tablename__ = "items_in_order"

    id = db.Column(db.Integer, primary_key=True)
    item_id = db.Column(db.Integer, db.ForeignKey("items.id"))
    order_id = db.Column(db.Integer, db.ForeignKey("orders.id")) # order_id will be set when items is passed into OrderModel
    quantity = db.Column(db.Integer)

    item = db.relationship("ItemModel") # item is corresponding ItemModel
    order = db.relationship("OrderModel", back_populates="items") # order is corresponding OrderModel, which has list of ItemsInOrder


class OrderModel(db.Model):
    __tablename__ = "orders"

    
    id = db.Column(db.Integer, primary_key=True) # id will be generated after we fill status and items
    status = db.Column(db.String(20), nullable=False) # pending, failed, completed
    """items is a list of ItemsInOrder object
    back populates makes changes to one reflect on the other"""
    items = db.relationship("ItemsInOrder", back_populates="order") # items is a list of ItemsInOrder


    @property
    def description(self) -> str:
        """Generates a simple string representing this order, in the format of 5x chair, 2x table"""
        item_counts = [f"{item_data.quantity}x {item_data.item.name}" for item_data in self.items]
        return ",".join(item_counts)

    @property
    def amount(self) -> int:
        """Calculates the total amount to charge for this order.
        Assumes item price is in USD–multi-currency becomes much tricker!
        :return int: total amount of cents to be charged in this order.x`"""
        return int(sum([item_data.item.price * item_data.quantity for item_data in self.items]) * 100)
    

    @classmethod
    def find_all(cls) -> List["OrderModel"]:
        return cls.query.all()

    @classmethod
    def find_by_id(cls, _id: int) -> "OrderModel":
        return cls.query.filter_by(id=_id).first()

    # makes an API request to Stripe 
    def charge_with_stripe(self, token: str) -> stripe.Charge:
        stripe.api_key = os.getenv("STRIPE_API_KEY")

        return stripe.Charge.create(
            amount=self.amount, # amount of cents
            currency=CURRENCY,
            description=self.description,
            source=token
        )

    # atomic operation
    def set_status(self, new_status: str) -> None:
        """Sets the new status for the order and saves to the database—so that an order is never not committed to disk.
        :param new_status: the new status for this order to be saved."""
        self.status = new_status
        self.save_to_db()

    def save_to_db(self) -> None:
        db.session.add(self)
        db.session.commit()

    def delete_from_db(self) -> None:
        db.session.delete(self)
        db.session.commit()