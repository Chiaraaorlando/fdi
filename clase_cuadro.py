class Cuadro:

    def __init__(self, id, title, author, price, creation, movement, material) -> None:
        self.id = id
        self.title = title
        self.author = author
        self.price = price
        self.creation = creation
        self.movement = movement
        self.material=material

    def serialize(self):
        return {
            'id': self.id,
            'title': self.title,
            'author': self.author,
            'price': self.price
        }

    def serialize_details(self):
        return {
            'id': self.id,
            'title': self.title,
            'author': self.author,
            'price': self.price,
            'creation': self.creation,
            'movement': self.movement,
            'material': self.material
        }