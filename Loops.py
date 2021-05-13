# -*- coding: utf-8 -*-
"""
Created on Thu May  6 23:02:40 2021

@author: Lenovo

Assignment 5: Basic Loop 

Write a program that prints the numbers from 1 to 100.

But for multiples of three print "Fizz" instead of the number and for the multiples of five
print "Buzz".

For numbers which are multiples of both three and five print "FizzBuzz".
"""

'''
 Created a list using range function with elemnts as numbers from 1 to 100
'''

Numbers = list(range(1,101)) 

''' 
Created a for loop with nested if statements
'''
for i in Numbers:
    if i%3 == 0:
       '''
       if the number is the divisible by 3 then replace the number with 'Fizz' 
       by subracting the number with 1 and using it as index
       '''
       Numbers[i-1] = "Fizz"
    if i%5 == 0:
        '''
        if the number is the divisible by 5 then replace the number with 'Buzz' 
        by subracting the number with 1 and using it as index
        '''
        Numbers[i-1] = "Buzz"
    if i%3 == 0 and i%5 == 0:
        '''
        if the number is the divisible by 3 and 5 then replace the number with 'FizzBuzz' 
        by subracting the number with 1 and using it as index
        '''
        Numbers[i-1] = "FizzBuzz" 
'''
Use a for loop to go through all the elements of the List and print them
'''
for n in Numbers:
    print(n)
