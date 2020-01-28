# -*- coding: utf-8 -*-
"""
Created on Mon Jan 27 03:31:00 2020

@author: RPS
"""

import pymysql
import os
path="C://Users//RPS//Desktop//Training//day1//backup//user3.txt"

def createConnection():
    connection=pymysql.connect(host="localhost",user="root",passwd="rps@1",db="test")
    return connection


collection=[]
def getData():
    if(os.path.exists(path)):
        print("File exists")
        fileRef=open(path,'r')
        for line in fileRef:
            print(line)
            collection.append(line.split(","))
    else:
        print("File not exists")
    return collection

def addUser(data):
    conn=createConnection()
    cursor=conn.cursor()
    try:
        cursor.execute("insert into usertab values('%s','%s','%s')" %(data[0],data[1],data[2]))
        conn.commit()
    except pymysql.Error as err:
        print("Exception occured " ,err)
        conn.rollback()
    finally:
        conn.close()
        
for user in getData():
    addUser(user)

