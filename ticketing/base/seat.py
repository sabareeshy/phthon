"""This module will have seat information
"""
class Seat:
   """ This represents seat in any booking system
   This could be a movie theatre seat, bus or train seat berth
   """
   def  __init__(self, id, price=0.0, category='standard', is_empty = True):
      """This is initializer for seat
      """
      self.__id = id
      self.price = price
      self.category = category
      self.__is_empty = is_empty
      
   def book(self, price):
      self.__is_empty = False
      self.price = price

   def get_seat_number(self):
      return self.__id
   

