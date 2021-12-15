# TWO NUMBER SUM

# Given an array with N elements and Target sum value
# Aim: To find a pair of numbers from the array that adds up to the target sum

# Approach 1
# O(n^2) Time complexity and O(1) space complexity
# Not a good approach
nums=[3,5,-4,8,11,1,-1,6]
target_sum=10

def two_sum_1(nums,target):
  for i in range(len(nums)):
    for j in range(i+1,len(nums)):
      if nums[i]+nums[j]==target:
        return [nums[i],nums[j]]
  return []

# print(two_sum(nums,target_sum))

# Approach 2
# O(n) Time and Space
# Using Hash tables and having more space complexity to reduce time
# So that the elements of arrays can be accessed faster
# Go on iterating the array and check whether (target - num) is in the hash table 
# if it exists return the number and the other number in the hashtable as list 
# Else add the number into hashtable with value True

def two_sum_2(nums,target):
  hash_table=dict()
  for num in nums:
    if (target-num) in hash_table:
      return [num,target-num]
    else:
      hash_table[num]=True 
  return []

# print(two_sum_2(nums,target_sum))

# Approach 3
# O(n*logn) time and O(1) space complexity
# Sorting the array first . Sorting algo usually takes (nlog(n)) time complexity
# Python sort() uses Timsort algorithm which is derived from merge sort and insertion sort
# Use two pointers left and right and check their sum. If their sum equals to target return the numbers.
# If sum < target increase left pointer
# If sum > target decrease the right pointer
# Do it until left<right

def two_sum_3(nums,target):
  nums.sort()
  left=0
  right=len(nums)-1
  while left<right:
    if nums[left] + nums[right] == target:
      return [nums[left], nums[right]]
    elif nums[left] + nums[right] < target:
      left+=1
    else:
      right-=1
  return []

print(two_sum_3(nums,target_sum))


