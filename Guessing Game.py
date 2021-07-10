# -*- coding: utf-8 -*-
"""
Created on Mon Jun 14 19:46:38 2021

@author: Lenovo
"""


"""
Guess the Number

A simple game in which the user/player has to guess the number that is randomly 
picked by the computer.
"""

'''
import randoom module to generate a random number from the range set by user.
'''
import random
'''
Define a function called guess with argument 'x'.
'''
def guess(x):
    '''
    By using random.radint() method create a random number in range (1,x) and 
    assign it to the variable random_num.
    '''
    random_num = random.randint(1,x)
    #Create a variable guess which stores the guess value and initalize it with 0. 
    guess = 0
    #Create an empty list guesslist
    guesslist = []
    '''
    Use conditional statements to check if the guess is equal to the random number and
    also to print an statement if the guess is less than or greater than the random number
    '''
    while guess != random_num:
        guess = int(input(f"Please enter a number in range 1 to {x}: "))
        guesslist.append(guess)
        b = len(guesslist)
        if guess < random_num:
            print("The guess is less than random number.")
            
        elif guess > random_num:
            print("The guess is more than random number.")
            
    print(f"Congrats your guess is correct and the random number is {x}")
    print(f"It took you {b} guesses")
    #print(guesslist)
a= int(input("Enter the end value of the range : "))
guess(a)

     