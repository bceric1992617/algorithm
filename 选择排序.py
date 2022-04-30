arr = [11,72,63,4,51,6,37,18,29,10]

for j in range(len(arr)):
    for i in range(j,len(arr) - 1):
        if arr[i + 1] < arr[j]:
            arr[j], arr[i + 1] = arr[i + 1], arr[j] 

print(arr)


