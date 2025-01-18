def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr) // 2]
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    return quick_sort(left) + middle + quick_sort(right)

user_input = input("Enter a list of integers separated by space: ")
arr = list(map(int, user_input.split()))
sorted_arr = quick_sort(arr)
print("Sorted array:", sorted_arr)

