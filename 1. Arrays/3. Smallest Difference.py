# Smallest Difference
# Given two arrays of size M and size N
# Calculate a pair of numbers out of which one is from first arraya and other is from second array which yields minimum Difference
# 2 Approaches
# Approach 1: Naive using 2 for loops
# Approach 2: O(n*log(n))+O(m*log(m))T and O(1)S

# Steps
# 1. Sort both arrays
# 2. Make the pointers point to the first element of each array
# 3. Check their difference. if num in arr1 < arr2. consider num in (arr2-arr1) as smallest difference and increment 1st pointer
# 4. Check their difference. if num in arr2 < arr1. consider  num in (arr1-arr2)  as smallest difference and increment 2nd pointer
# 5. If difference is zero return the pair
# 6. Go on until the arrays reach their last index or stops becoz of condition
# 7. return the final updated pair

arr1 = [-1, 5, 10, 20, 28, 3]
arr2 = [26, 134, 135, 15, 17]


def smallest_difference(arr1, arr2):
    arr1.sort()
    arr2.sort()
    index1 = 0
    index2 = 0
    smallest = float("inf")
    smallest_pair = []
    current = float("inf")
    while index1 < len(arr1) and index2 < len(arr2):
        first_number = arr1[index1]
        second_number = arr2[index2]
        if first_number < second_number:
            current = second_number-first_number
            index1 += 1

        elif second_number < first_number:
            current = first_number-second_number
            index2 += 1

        else:
            # If difference is zero that is the pair
            return [first_number, second_number]

        if smallest > current:
            smallest = current
            smallest_pair = [first_number, second_number]
    return smallest_pair


print(smallest_difference(arr1, arr2))
