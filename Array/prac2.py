# Reversing the array

# Initializing the array

A = input("Enter the array elements (separated by space): ")
A = [int(x) for x in A.split()]

def reverse(A):
    rev = A[::-1]
    print(rev)

reverse(A)
