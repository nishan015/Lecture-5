# -*- coding: utf-8 -*-
"""
Created on Mon Apr 15 10:21:27 2019

@author: Nihar G
"""
# function
x = 10

def my_func(a):                  # a is passed as the parameter/arguements of the function 
    return (a+x) * 2

result = my_func(10)
print(result)

# Function Programming

# Any function return under global variable can access these global variables. Variables defined within a function 
# can be accessed by lower levels ONLY

# Function requires a return value.
# Argument 'a' is local to the function. But X is global, hence whenever X changes anywhere the fucntion result too changes.

# Fixing the X global problem

def my_func(a, x):                  # x is passed as the local arguements of the function here. It does not overwrite the 
                                    # global variable x=10
    return (a+x) * 2

result = my_func(10, 2)
print(result)

print(x)                              # to check if global x is overwritten or not. Here it might be useful to rephrase 
#                                       elements and not use same variables.

def my_func(a, x, c): 
    result = (a + x) * 4             
    print('math!', c)
    return result

vals = [10, 3, 'me']
print(my_func(*vals))                 #unpacking using *


def my_func(a):
    x, y, z = a
    result = (x + y) *2.1
    print('math!', z)
    return result

vals = [10, 1, 'you']
my_func(vals)

#key word arguments

def my_func(a, user_name='Bob'):
    x, y, z = a
    result = (x + y) *2.1
    print('math!', z, user_name)
    return result

vals = [10, 1, 'you']
my_func(vals)

# overwriting bob.Check the code???

def my_func(a, user_name='Bob'):
    x, y, z = a
    result = (x + y) *2.1
    print('math!', z, user_name)
    return result

vals = [10, 1, 'Sue']
my_func(vals)

# using unpacking of a dictonary to pass the key word arguments and also look into global level arguments vs local level

def my_func(vals = [0,0, ''], user_name='Bob'):
    x, y, z = vals
    result = (x + y) *2.1
    print('math!', z, user_name)
    return result

vals = [10, 1, 'you']
params = {'vals':vals, 'user_name': 'Sue'}
my_func(**params)                               #unpacking the dictionary matches the arguments of the function


#Generators

def my_gen(stop):
    v = -1
    while True:
        v += 1
        yield v                #yield statement inside a loop makes the function as a generator








             
