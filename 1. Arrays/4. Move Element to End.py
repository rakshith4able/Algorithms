# Given 1) Array with n elements 2) A Number
# Aim: Move all occurances of array to the last of the array
# 2 Approaches
# Approach 1: Sorting and moving all occurances of the number to the end and all at the end to starting index range of the number. O(n*log(n))T and O(1)S
# Approach 2: Using pointers O(n)T and O(1)s
# Steps:
# 1. Create 2 pointers pointing to first and last element in an array
# 2. Do until the pointers cross each other:
# 3. Check if the ptr2 is pointing to the given number if yes move pointer to left and if no stay there
# 4. Check if the ptr1 is pointing to the given number if yes swap else move ptr1 to right

def move_to_end(nums, k):
    left = 0
    right = len(nums)-1
    while left < right:
        if nums[right] == k:
            right -= 1
        else:
            if nums[left] == k:
                nums[left] = nums[right]
                nums[right] = k
                left += 1
            else:
                left += 1
    return nums


nums = [1, 2, 2, 2, 3, 4, 2, 5, 2, 2, 6, 2]
k = 2
print(move_to_end(nums, k))
