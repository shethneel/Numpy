# -*- coding: utf-8 -*-
"""Numpy2.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1aWZ4YNlZyclgrPMiOz0OBPTUhLUZt02h
"""

import numpy as np

"""***CONVERTING LIST INTO ARRAY***"""

lst = [1,2,3]
print(type(lst))
lst

n_ar = np.array(lst)
print(type(n_ar))
n_ar

lst1 = [[1,2,3],[4,5,6]]
print(type(lst1))
lst1

n_ar1 = np.array(lst1)
print(type(n_ar1))
n_ar1

# To create numpy array of some numbers
# Syntax : np.arange (start, end, interval)

np.arange(0,10,2)

# makes array of zeros
# Syntax : np.zeros ((rows, columns))

np.zeros((5,5))

# Gives equally spaced required numbers between two numbers
# Syntax : np.linspace (start, end, required_numbers)

np.linspace(0,10,5)

# Random.rand : Generates numbers between 0 and 1 where 0 is inclusive but 1 isn't
# Syntax : np.random.rand (rows, columns)

np.random.rand(3,5)

# Makes numbers on standard normal distribution
# Syntax : np.random.randn (rows, columns)
# If you want to understand the standard deviation, go to this link : https://www.youtube.com/watch?v=rzFX5NWojp0&ab_channel=StatQuestwithJoshStarmer
np.random.randn(3,5)

# Gives random integeres
# Syntax : np.random.randint (start, end, required_numbers)

np.random.randint(0,10,5)

# if you want to get it as 2D array, np.random.randint (start, end, (row, column))

'''
The seed function in NumPy is used to initialize the random number generator for reproducibility.
By setting the seed, you make your random number generation deterministic, meaning it will produce the same sequence of random numbers each time you run your code with the same seed.

Why Use a Seed?

Reproducibility: When you're developing or testing code, you often need to reproduce the same results to debug or verify your computations.

Consistency: When sharing your code with others or running it in different environments, setting a seed ensures everyone gets the same results.

Testing: Automated tests often require consistent results to verify the correctness of the code.

Syntax :

np.random.seed(Any random value you want to write)
np.random.rand(Total values you want)
'''

np.random.seed(1)
np.random.rand(5)

# I tried to run this sell for three times and everytime I got the same results

# Reshaping array
# Syntax : array_name.reshape (rows, columns)
# While converting into 2D, make sure that multiplication of row and column should come the total elements of array

ar = np.random.randint(0,11, 10)
print(ar)
ar.reshape(2,5)

# Max and min func

ar1 = np.arange(0,10)
print(ar1)
print(ar1.max())
print(ar1.min())

# argmax and arg min : returns index value of min and max array

ar1 = np.arange(0,10)
print(ar1)
print(ar1.argmax())
print(ar1.argmin())

"""***INDEXING AND SELECTION***"""

arr = np.arange(0,11)

arr

arr[0:5] # or you can also write arr [:5] as it eventually starts from the first element

arr [5:]

# when you mention start and end limit, it starts from the first element and goes upto end-1 element

arr[1:5]

# Broadcasting
# Assigning some value to whole group of value at one

# Syntax : array_name[start:end] = value

arr[0:5] = 100
arr

arr = np.arange(0,11)
arr

slice_of_arr = arr[0:5]
slice_of_arr

# Copying array

cpy = arr.copy()
cpy

slice_of_arr1 = cpy[0:5]
slice_of_arr1

slice_of_arr1[:] = 99
slice_of_arr1

cpy

arr

arr_2d = np.random.randint(0,9, (3,3))
arr_2d

arr_2d[0]

arr_2d[0][0]

dice_rolls = np.array([3, 1, 5, 2, 5, 1, 1, 5, 1, 4, 2, 1, 4, 5, 3, 4, 5, 2, 4, 2, 6, 6, 3, 6, 2, 3, 5, 6, 5])

temp = dice_rolls[dice_rolls>2]

temp

temp.size

"""***NUMPY OPERATIONS***"""

arr = np.arange(0,10)
arr

arr + 5

arr - 2

arr + 3

arr + arr

arr * arr

arr - arr

arr/arr

# Square root

np.sqrt(arr)

# find trignometric functions of array

np.sin(arr)

# find log of array

np.log(arr)

# sum : adds all elements of array

np.sum(arr)

# mean : finds average

np.mean(arr)

arr2 = np.arange(0,25).reshape(5,5)
arr2

arr2.sum()

arr2.sum(axis=0)

# axis = 0 is for rows, so when we do sum, it adds each element of row in their appearance manner
# such as addition of aa first element, then second then third etc, so sum of axis 0 goes column wise

arr2.sum(axis=1)

# axis = 1 is for columns, so when we do sum, it adds each element of column in their appearance manner
# such as addition of aa first element, then second then third etc, so sum of axis 1 goes row wise

