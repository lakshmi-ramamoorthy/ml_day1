# -*- coding: utf-8 -*-
"""
Created on Mon Jan 27 02:28:34 2020

@author: RPS
"""

import os
import requests
response=requests.get("https://jsonplaceholder.typicode.com/users")

path="C:/Users/RPS/Desktop/Training/day1"

header=["Name","Email","phone"]

if(os.path.exists(path+"/backup")):
    print("Dir exists")
    if(os.path.exists(path+"/backup/user2.csv")):
        print("File exists")
        fileRef=open(path+"/backup/user2.csv",'w')
        fileRef.write("$$$".join(header))
        for res in response.json():
            fileRef.write("\n")
            data =res['name']+","+res['email']+","+res['phone']
            print(data)
            fileRef.write(data)
            fileRef.close
    else:
        print("File not exists")
        fileRef=open(path+"/backup/user2.csv",'w')
        fileRef.close
      
        
else:
    print("Not exists")
    dir=os.mkdir(path+"/backup")
    print("dir created %s" %(dir))
    
    


'''
        for res in response.json():
            data =res['name']+ ","+res['email']+","+res['phone']
            print(data)
            fileRef.write(data)
            fileRef.write("\n")
            fileRef.close
 ''' 
    