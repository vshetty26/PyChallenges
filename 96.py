def binary_search(sorted_list, target):
    low = 0
    high = len(sorted_list) - 1

    while low <= high:
        mid = (low + high) // 2
        if sorted_list[mid] == target:
            return mid
        elif sorted_list[mid] < target:
            low = mid + 1
        else:
            high = mid - 1

    return -1  


sorted_list = [int(x) for x in input("Enter a sorted list of numbers (space-separated): ").split()]
target = int(input("Enter the target number to search for: "))

result = binary_search(sorted_list, target)

if result != -1:
    print(f"Target {target} found at index {result}.")
else:
    print(f"Target {target} not found in the list.")



