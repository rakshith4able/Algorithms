# THREE NUMBER SUM

# Given an array with N distinct elements and Target sum value
# Aim: To find all possible triplet of numbers from the array that adds up to the target sum
# 3 Approaches are there
# Approach 1: Using 3 for loops O(n^3)T
# Approach 2: Using hash map and 2 for loops. Takes more space, complex and produces duplicates
# Approach 3: (optimal) O(N^2)T and O(N) space.
# Steps:

# 1) Sort the array first
# 2) iterate over the sorted array
# 3) In each iteration use left pointer starting from right of the current number and right pointer pointing to end
# 4) current_sum=current_number+left+right
# 5) if current_sum==target then add triplet to list and move both right and left pointer right and left
# 6) elif <target  move left pointer right
# 7) >target move right pointer to left
# 8) continue until left<right
# 9) continue until all elements are iterated

def three_number_sum(nums, target):
    solution = list()
    nums.sort()
    for i in range(len(nums)-2):
        current_num = nums[i]
        left = i+1
        right = len(nums)-1
        while left < right:
            current_sum = current_num+nums[left]+nums[right]
            if current_sum == target:
                solution.append([current_num, nums[left], nums[right]])
                left += 1
                right -= 1
            elif current_sum < target:
                left += 1
            else:
                right -= 1
    return solution


nums = [-8, -6, 1, 2, 3, 5, 6, 12]
target = 0
print(three_number_sum(nums, target))
