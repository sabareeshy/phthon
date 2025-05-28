class Seat:
    def __init__(self, id, price, category, is_empty):
        self.__id = id
        self.price = price
        self.category = category
        self.__is_empty = is_empty

    def book(self, price):
        self.is_empty = False
        self.price = price
   
    def get_seat_number(self):
        return self.__id
    