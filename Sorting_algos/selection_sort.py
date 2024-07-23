#This is a Comparison Based Sorting Algorithm. Sorting is a process of rearranging the elements, the goal is to rearrange the elements in sorted order, either ascending or descending order. Time Complexity for Rearranging O(n^2) [n(n-1)/2] and for swapping is A[n]

def selectionsort(A):
    n = len(A)
    for i in range(n-1):
        position = i
        for j in range(i+1,n):
            if A[j] < A[position]:
                position = j

        temp = A[i]
        A[i] = A[position]
        A[position] = temp

A = [5,34,65,9,20]
print("Original Array:",A)

selectionsort(A)
print("Sorted Array:",A)