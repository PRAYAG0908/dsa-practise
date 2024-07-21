#Better search technique than linear search. Array must be in a sorted order. #Time complexity : O(log n)

def iterative_binarysearch(A,key):
    l = 0
    r = len(A)-1
    while l <= r:
        mid = (l+r)//2 #executes for n/2 times as only the half portion of array is taken
        if key == A[mid]:
            return "Element found at index" , mid
        elif key < A[mid]:
            r = mid-1
        elif key > A[mid]:
            l = mid+1
    return "Element not found"

A = [3,9,27,55,91] #if array not sorted use A.sort()
Search = iterative_binarysearch(A,55)
print(Search)