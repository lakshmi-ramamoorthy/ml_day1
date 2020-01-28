# -*- coding: utf-8 -*-
"""
Created on Mon Jan 27 01:43:30 2020

@author: RPS
"""

import sys
sys.path.append("C:/Users/RPS/Desktop/Training/day1/")
from exercise6 import Customer

class GoodsCustomer(Customer):
    def __init__(self,custId,email,productType):
        Customer.__init__(self,custId,email)
        self.__type=productType

customer2=GoodsCustomer(34,"bala@gmail.com","dairy")
print(customer2.getId())
        