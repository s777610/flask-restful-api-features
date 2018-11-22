from marshmallow import Schema, fields

class BookSchema(Schema):
    title = fields.Str()
    author= fields.Str()

class Book:
    def __init__(self, title, author, description):
        self.title = title
        self.author = author
        self.description = description


book = Book("Clean Cide", "Bob Martin", "A book about writing clean code.")

book_schema = BookSchema()
book_dict = book_schema.dump(book)

print(book_dict)