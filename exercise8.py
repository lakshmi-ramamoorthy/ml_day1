# -*- coding: utf-8 -*-
"""
Created on Mon Jan 27 01:56:18 2020

@author: RPS
"""

class Booking():
    def book(self,amount):
        pass

class ForiegnExchangeBooking(Booking):
    def book(self,amount):
        print("Conver %d" %(amount))
foriegnExch=ForiegnExchangeBooking()
foriegnExch.book(456)