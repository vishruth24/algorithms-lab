def sort(arr,first,last):
    if first<last:
        split=partition(arr,first,last)
        sort(arr,first,split-1)
        sort(arr,split+1,last)

def partition(arr,first,last):
    pivot=arr[first]
    left=first+1
    right=last
    done=False

    while not done:
        while left<=right and arr[left]<pivot:
            left+=1
        while right>=left and arr[right]>pivot:
            right-=1
        if right<left:
            done=True
        else:
            temp=arr[left]
            arr[left]=arr[right]
            arr[right]=temp
    temp=arr[first]
    arr[first]=arr[right]
    arr[right]=temp
    return right
arr=[5,1,2,6,8,35]
sort(arr,0,len(arr)-1)
print(arr)
