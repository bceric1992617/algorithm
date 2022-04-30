arr = [11,72,63,4,51,6,37,18,29,10]
n = 1

for i in range(len(arr) - 1):
    for j in range(n):
        if arr[n] > arr[j]:
            arr[j], arr[n] = arr[n], arr[j]
    n += 1 

