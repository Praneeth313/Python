# -*- coding: utf-8 -*-
"""
Created on Wed May 12 12:23:16 2021

@author: Lenovo

Assigbmennt 6

Create a function that takes in two parameters: rows, and columns, both of which are integers. 
The function should then proceed to draw a playing board (as in the examples from the lectures) 
the same number of rows and columns as specified. After drawing the board, your function should 
return True.
"""
"""
Define a function which takes two parameters rows & cols
"""
def tictactoe(rows,cols):
    """ 
    Using for loop and if statments write a program to create a tic-tac-toe board with 
    same number of rows and columns.
    """
    """ 
    Set the max number of columns to 93 to avoid wrapping
    """
    if cols<=93:
        
        for row in range(rows):
            if row%2 == 0:
                for col in range(cols):
                    if col%2 == 0:
                        if col != (cols-1):
                            print(" ",end = "")
                        else:
                            print(" ")
                    else:
                        if col != (cols-1):
                            print("|",end = "")
                        else:
                            print("|")
            else:
                print("-"*cols)
        return True
    else:
        return False
            

print(tictactoe(20,20))

