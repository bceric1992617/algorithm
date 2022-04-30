
def quickSort(data):
    if len(data) > 1:
        arrLeft, arrRight = [], []
        mid = data[len(data) // 2]
        data.remove(mid)
        for v in data:
            if v <= mid:
                arrLeft.append(v)
            else:
                arrRight.append(v)
        left = quickSort(arrLeft)
        right = quickSort(arrRight)
        return left + [mid] + right
    else:
        return data


arr = [11,72,63,4,51,6,37,18,29,10]
print(quickSort(arr))
