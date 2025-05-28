from .seat import Seat

class Bookable:
    """This is parent class where booking seats is involved
    """
    """This represents bus during bus booking
    """
    def __init__(self, operator, name, registration_number):

        self.operator = operator
        self.name = name
        self.registration_number = registration_number
        self.seats = dict()

    def set_seats(self, count, rows, columns):

        """This creates default seat structure
        """
        for row_index in range(1, rows+1):
           for column_index in range(1, columns+1):
               seat = Seat(
                   id=f"{row_index}_{column_index}"
               )
               self.seats.update({seat.get_seat_number,seat})
            
    def book_ticket(self, seat_number, price):

        self.seats.get(seat_number).book(price)
