def nextPermutation(nums):
    n = len(nums)
    i = n - 2

    # Step 1: Find the first decreasing element
    while i >= 0 and nums[i] >= nums[i + 1]:
        i -= 1
    
    if i >= 0:
        # Step 2: Find the element to swap with
        j = n - 1
        while nums[j] <= nums[i]:
            j -= 1
        # Step 3: Swap elements
        nums[i], nums[j] = nums[j], nums[i]
    
    # Step 4: Reverse the subarray from i + 1 to end
    left, right = i + 1, n - 1
    while left < right:
        nums[left], nums[right] = nums[right], nums[left]
        left += 1
        right -= 1

nums = input("Enter a list of numbers: ").split()
nums = [int(num) for num in nums]
nextPermutation(nums)
print(nums)