def merge_sort(lists):
    # 递归结束条件
    if len(lists) <= 1:
        return lists 
    # 分治进行递归
    middle = len(lists)//2
    left = merge_sort(lists[:middle])
    right = merge_sort(lists[middle:])    
    # 将两个有序数组进行合并
    result = []
    i = j = 0
    while i < len(left) and j < len(right):
        # 将较小值放入到result中
        if left[i] < right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    # 将未被扫描到的直接追加到result后面
    if i == len(left): 
        result.extend(right[j:])
    else: 
        result.extend(left[i:])
    return result   

arr = [11,72,63,4,51,6,37,18,29,10]
print(merge_sort(arr))
# print(10 % 2)