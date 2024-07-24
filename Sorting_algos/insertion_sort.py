#This is a Comparison Based Sorting Algorithm. It is a Stable ALgorithm. Comparison : O(n^2) & Swapping : O(n^2)

def insertionsort(A):
    n = len(A)
    for i in range(1,n):
        cvalue  = A[i]
        position = i
        while position > 0 and A[position - 1] > cvalue:
            A[position] = A[position - 1]
            position = position - 1
            A[position] = cvalue

A = [5,34,65,9,20]
insertionsort(A)
print(A)