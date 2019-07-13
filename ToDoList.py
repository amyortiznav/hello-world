#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jul 12 22:07:08 2019

@author: amyortiz
"""
name = input("What's your name?")

toDoList = []

toDoList.append(input ("Okay" + name + " what's on your to do list?"))


option = input("Is that it," + name + "? ")

while option.lower() == "no":
    toDoList.append(input("What else we doing?"))
    optionRepeat = input("is that it now? ")
    option=optionRepeat
print(toDoList)
print("Mickey Is a fucking code god")


    



