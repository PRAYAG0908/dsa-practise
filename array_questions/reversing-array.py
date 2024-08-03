def reverse_array(A):
    n = len(A)
    start = 0
    end = n-1
    while start < end:
        temp = A[start]
        A[start] = A[end]
        A[end] = temp
        start += 1
        end -= 1


n = int(input())
A = []
for i in range(0,n):
    A.append(int(input()))
reverse_array(A)
print(A)