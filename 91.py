print("Bubble Sort Implementation")
print("---------------------------")
nums = list(map(int, input("Enter a list of integers separated by space: ").split()))
print("Original list:", nums)
for i in range(len(nums)):
    for j in range(len(nums) - 1):
        if nums[j] > nums[j + 1]:
            nums[j], nums[j + 1] = nums[j + 1], nums[j]
print("Sorted list:", nums)


