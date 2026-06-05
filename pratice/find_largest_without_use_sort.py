nums = [10, 20, 4, 45, 99]

largest = nums[0]
second_largest = nums[0]

for num in nums:
    if num > largest:
        second_largest = largest
        largest = num
    elif num > second_largest and num != largest:
        second_largest = num

print("Second Largest Number:", second_largest)