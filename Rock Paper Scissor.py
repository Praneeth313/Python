# -*- coding: utf-8 -*-
"""
Created on Thu Jul  8 09:25:02 2021

@author: Lenovo

Rock Paper Scissors
A program to play rock paper scissor with the computer
"""


'''
Import random module to use choice method to slect between rock,paper & scissor.
'''
import random

'''
Create a function called play which asks for the input form user in selecting rock,paper or scissor
and assign it variable called user.
By using random.choice method the computer picks a choice among rock,paper or scissor and assign 
it to a variable called computer.
Write a if statment where if the user is equal to computer then its a tie and another if statment 
which uses a function that checks the game rule.
'''

def play():
    user = input("What\'s your choice? 'r' for rock, 'p' for paper, 's' for scissor\n")
    computer = random.choice(['r','p','s'])
    if user == computer:
        return "It\'s a tie!"
    '''
    use a if statment with is_win functon as condition and using variables user and computer as 
    arguments.
    '''
    if is_win(user,computer):
        return "You WON!"
    return "You LOST"

'''
Create a function called is_win with arguments player and opponent and write a condition to 
check the winner of the round returns true if player wins.
'''
def is_win(player,opponent):
    #r>s s>p p>r
    if (player == 'r' and opponent == 's') or (player == 's' and opponent == 'p') or (player == 'p' and opponent == 'r'):
        return True

'''
Call the play function and print the output
'''    
print(play())
    


