def knapSack(W , wt , val , n):
    if n == 0 or W == 0 :
        return 0
    if (wt[n-1] > W):
        return knapSack(W , wt , val , n-1)
    else:
        return max(val[n-1] + knapSack(W-wt[n-1] , wt , val , n-1),knapSack(W , wt , val , n-1))

val = list(int(x) for x in input("Enter the values :").split())
wt = list(int(x) for x in input("Enter the weights :").split())
W = int(input("Enter the max weight capacity :"))
n = len(val)
print ("The max value is ",knapSack(W , wt , val , n))

