"""
    File: wish_birthday.py
    Author: Ashish Chopra
    Date: 13 Jan,2016
    
    A user will enter his date of birth as dd-mm-yyyy format,
    the computer will wish him Happy Birthday based on the time reference.
    if it's today, then Wish him; 
    if it's in future, then wish him in advance;
    if it's in past, then wish him belated birthday.

"""
import time

def wish_user():
    date_current = input('Enter you DOb as dd-mm-yyyy')
    date_components = date_current.split("-")
    current_month = time.localtime().tm_mon
    current_day = time.localtime().tm_mday

    if (int(date_components[1]) >= current_month ):
        if (int(date_components[0]) > current_day):
            print("Wish you advanced happy birthday")
        elif (int(date_components[0]) == current_day):
            print("Wish you a happy birthday")
        else:
            print("Wish you a belated happy birthday")
    else:
        print("wish you belated happy birthday")


#running the script

wish_user()
                 
