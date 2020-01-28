# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

class Customer(object):
    """
    def __new__(cls):
        print("new clas called")
        """
    message=""
    def __init__(self,custId,email):
        print("init method called")
        self.__custId=custId
        self.__email=email
        
    def getId(self):
        return self.__custId;
    
    def setId(self, custId):
        self.__custId=custId
        
    def getEmailId(self):
        return self.__email;
    
    def setEmailId(self, email):
        self.__email=email
        
    @staticmethod
    def validateemail(email):
        if(email.find("@") != -1):
            message="Valid"
        else:
            message="Invalid"
        return message

customer=Customer(12,"laksgmail.com")
customer.setId(45)
print(customer.getId())
print(Customer.validateemail(customer.getEmailId()))
