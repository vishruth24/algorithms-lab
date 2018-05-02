

def mergersort(arr):

    if len(arr)>1:
        mid=len(arr)//2;
        lefthalf=arr[:mid]
        righthalf=arr[mid:]

        mergersort(lefthalf)
        mergersort(righthalf)

        i,j,k=0,0,0

        while i<len(lefthalf) and j<len(righthalf):
            if lefthalf[i]<righthalf[j]:
                arr[k]=lefthalf[i]
                i+=1
            else:
                arr[k]=righthalf[j]
                j+=1
            k+=1

        if i<len(lefthalf):
            arr[k]=lefthalf[i]
            i+=1
            k+=1
        if j<len(righthalf):
            arr[k]=righthalf[j]
            j+=1
            k+=1

arr=list(int(x) for x in input("Enter elements ").split())
mergersort(arr)
print(arr)
