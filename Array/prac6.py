#  Search in Rotated Sorted Array


# Method for sorting the array

def bSearch(nums, target):
    left, right = 0, len(nums) - 1

    while left <= right:
        mid = (left + right) // 2

        # Check if the middle element is the target
        if nums[mid] == target:
            return mid
        
        # Determine which part is sorted
        if nums[left] <= nums[mid]:  # Left part is sorted
            if nums[left] <= target < nums[mid]:  # Target is in the left part
                right = mid - 1
            else:  # Target is in the right part
                left = mid + 1
        else:  # Right part is sorted
            if nums[mid] < target <= nums[right]:  # Target is in the right part
                left = mid + 1
            else:  # Target is in the left part
                right = mid - 1

    # Target not found
    return -1


# Taking the user input for array and target value

nums = input("Enter the array of numbers: ").split()
nums = [int(num) for num in nums]
target = int(input("Enter the target number: "))
result = bSearch(nums, target)
print("Element found at index", result)



