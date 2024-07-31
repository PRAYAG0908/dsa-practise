def max_element(A):
    n = len(A)
    max_ele = A[0]
    for i in range(0,n):
        if max_ele < A[i]:
            max_ele = A[i]
    print(max_ele)

A = [212,35,453,324,2]
max_element(A)