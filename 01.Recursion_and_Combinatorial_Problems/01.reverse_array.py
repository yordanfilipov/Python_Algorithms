def reverse_array(idx, arr):
    print(arr[idx], end=" ")
    if idx == 0:
        return
    else:
        reverse_array(idx - 1, arr)


array = input().split(" ")
reverse_array(len(array) - 1, array)