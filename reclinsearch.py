elements=list(int(x) for x in input("Enter the elements : ").split())
key=int(input("Enter the key : "))

def rec(element,key,i):
    if i>=len(elements):             #If element isnt found
        return -1
    elif elements[i]==key:          #If element is found
        return i
    else:
        return rec(elements,key,i+1) #Calling recursive function

index=rec(elements,key,0)
if index==-1:
    print("Element not present")
else:
    print("Element found in index :",str(index))
