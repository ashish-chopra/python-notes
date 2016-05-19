"""
    File: string_print.py
    Author: Ashish Chopra
    Date: 13 jan, 2016
    
    This script is a collection of small programs written in python,
    during classroom training session to pickup the style of thinking
    in Python

"""


'''
    Given a string input, print the whole string back,
    with first and laster character in UPPERCASE.

'''
def something_simple():
    name = input('write a string')
    new_name = name[0] + name[1:-1].upper() + name[-1]
    print(new_name)


'''
    Given a string input, print the whole string back, 
    with first and last 4 characters into UPPERCASE 
    and also reverse the last 4 characters too.
'''
def first_four_upper():
    string = input('enter a string: ')
    # new_string = string[:4].upper() + string[4:-4] + string[-1:-5:-1].upper()
    new_string = string[:4].upper() + string[4:-4] + string[-4:][::-1].upper()
    print('new string: ', new_string)


'''
    Play with split function for strings
'''
def split_strings():
   print("hello world of unix".rsplit(" ", 1))


    

#run the program here
something_simple()
first_four_upper()
split_strings()
