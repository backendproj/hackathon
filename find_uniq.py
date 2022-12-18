def find_uniq(arr):
    arr.sort()

    if(arr[0] < arr[len(arr)-1] and arr[0] < arr[len(arr)-2]):
        n = arr[0]
    else:
        n = arr[len(arr)-1]


    return n   
print(find_uniq([1,1,1,1,2,1]))