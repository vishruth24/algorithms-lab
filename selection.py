elements=list(int(x) for x in input("Enter the elements : ").split())

for i in range(len(elements)):
    for j in range(i+1,len(elements)):
        if elements[i]>elements[j]:
            elements[i],elements[j]=elements[j],elements[i]
print("Sorted list is",elements)    
