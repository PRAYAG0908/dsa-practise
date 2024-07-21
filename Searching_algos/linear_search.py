#linear or sequential search. Here we basically search for an element in an array.

def linearsearch(A,key):
    index = 0
    while index < len(A):
        if A[index] == key:
            return "Element Found at index :", index
        index = index+1
    return "Element Not Found!"

A = [21,27,45,87,63]
element = linearsearch(A,45)
print(element)

# Time complexity : O(n)