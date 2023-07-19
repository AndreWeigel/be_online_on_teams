# -*- coding: utf-8 -*-
"""
Created on Wed Jul 19 13:09:51 2023

@author: AndreWeigel
"""

from time import sleep
import math
from clicknium import clicknium as cc
import keyboard
import sys

def circle():
    a,b = cc.mouse.position()
    w = 20  
    m = (2*math.pi)/w 
    r = 200      

    while True:    
        for i in range(0, w+1):
            x = int(a+r*math.sin(m*i))  
            y = int(b+r*math.cos(m*i))
            cc.mouse.move(x,y)
            sleep(0.2)
            if keyboard.is_pressed('q'):
                sys.exit()

if __name__ == "__main__":
    print('Click -q- to quit te programm.')
    circle()
