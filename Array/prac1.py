# Initializing the array

A = [4, 9, 6, 5, 2, 3]


# Doing minmax via for loop

def setminimax(A):
    mini = maxi = A[0]

    for i in A[1:]:
        if i < mini:
            mini = i
        if i > maxi:
            maxi = i

    return mini, maxi



min_num, max_num = setminimax(A)
print("Minimum and maximum numbers are:", min_num, max_num)

# Doing minmax via sorting

def minmaxhere(A):
    A.sort()
    print("Min:", A[0], "Max:", A[-1])

minmaxhere(A)

# Doing minmax via built-in functions
def minmaxbuilt(A):
    print("Min:", min(A), "Max:", max(A))

minmaxbuilt(A)

# Doing minmax via numpy
import numpy as np
def minmaxnumpy(A):
    print("Min:", np.min(A), "Max:", np.max(A))

minmaxnumpy(A)

# Doing minmax via pandas
import pandas as pd
def minmaxpandas(A):
    print("Min:", pd.Series(A).min(), "Max:", pd.Series(A).max())

minmaxpandas(A)

# Doing minmax via list comperehension
def minmaxlist(A):
    mini = min(A)
    
    maxi = max(A)

    return mini, maxi

min_num, max_num = minmaxlist(A)

print("Minimum and maximum numbers are:", min_num, max_num)

