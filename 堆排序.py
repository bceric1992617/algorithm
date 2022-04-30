def heapSort(arr,arrLength):
    length = arrLength
    for j in range(int(arrLength ** 0.5) + 1): #二叉树层数
        length = arrLength // 2#等于多少个节点要操作
        for i in range(length):
            try: #有两个子节点
                if arr[i*2+2] > arr[i*2+1]:
                    if arr[i] < arr[i*2+2]:
                        arr[i], arr[i*2+2] = arr[i*2+2], arr[i]
                else:              
                    if arr[i] < arr[i*2+1]:
                        arr[i], arr[i*2+1] = arr[i*2+1], arr[i]  
            except: #只有一个子节点
                if arr[i] < arr[i*2+1]:
                    arr[i], arr[i*2+1] = arr[i*2+1], arr[i]  
    return arr


    


arr = [11,72,63,4,51,6,37,18,29,10,100,111]
arr = heapSort(arr,len(arr)) #生成大顶堆
for x in range(len(arr)-1,0,-1):
    arr[0],arr[x] = arr[x],arr[0] #再头尾兑换
    arr = heapSort(arr,x-1) #再重组大顶堆
print(arr)



