def removeDuplicates(arr):
    x = 0
    for i in range(len(arr)):
        if arr[i] > arr[x]:
            x = x+1
            arr[x] = arr[i]
    return x+1

arr = [0,0,1,1,1,2,2,3,3,4]
print(removeDuplicates(arr))