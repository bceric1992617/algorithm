arr = [11,72,63,4,51,6,37,18,29,10]
n = 1
for i in range(len(arr)):
    for i in range(len(arr) - n):
        if arr[i] > arr[i + 1]:
            arr[i], arr[i + 1] = arr[i + 1], arr[i]
    n += 1

print(arr)