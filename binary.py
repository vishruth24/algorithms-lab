num=list(int(x) for x in input("Enter the elements: ").split())

key=int(input("Enter the key "))

def bin(num,key):
        if len(num)==0:
                return False
        else:
                mid=len(num)//2
                if(num[mid]==key):
                        return True
                elif(num[mid]>key):
                        return bin(num[:mid],key)
                else:
                        return bin(num[mid+1:],key)
                return False
if bin(num,key):
        print("Key found")
else:
        print("Key not found")
