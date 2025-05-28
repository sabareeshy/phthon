from seat import Seat

class Bookable:
    def __init__(self, operator, name, registration_number):
        self.operator = operator
        self.name = name
        self.registration_number = registration_number
        self.seats = dict()

    def set_seats(self, rows, columns):

        for row_index in range(1, rows+1):
            for col_index in range(1, columns+1):
                seat = Seat(id=f"{row_index}_{col_index}")
            self.seats[seat.get_seat_number()] = seat
    
    def book_ticket(self, seat_number, price):

        self.seat.get(seat_number).book(price)


        

