class Product:
    """This class defines product
    members:
      id
      name
      price
      quantity
    methods:
      describe
      purchase
      sale    
    """
    
    def __init__(self, id, name, price, quantity):
        self.id = id
        self.name = name
        self.price = price
        self.quantity = quantity

    def sale(self, count):
        self.quantity -= count

    def purchase(self, count):
        self.quantity += count



