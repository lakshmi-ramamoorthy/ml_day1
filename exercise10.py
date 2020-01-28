# -*- coding: utf-8 -*-
"""
Created on Mon Jan 27 03:07:05 2020

@author: RPS
"""

import os
dir=os.walk("C:/Users/RPS/Desktop/Training")
print(type(dir))
for _ in dir:
    print(_)