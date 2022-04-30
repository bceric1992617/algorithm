arr = [11,72,63,4,51,6,37,18,29,10]
gap = len(arr) // 2
while gap >= 1:
    for i in range(len(arr) - gap):
        if arr[i + gap] < arr[i]:
            arr[i], arr[i + gap] = arr[i + gap], arr[i]
    gap = gap // 2
        
print(arr)
