# Given an integer array nums, return true if any value appears at least twice in the array, and return false if every element is distinct.

# defined array 

nums = input("Enter the elements of the array (separated by spaces): ").split()
nums = [int(num) for num in nums]

def contains_duplicates_element(nums):
    if len(nums) != len(set(nums)):
        return True
    else:
        return False

print(contains_duplicates_element(nums))