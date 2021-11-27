def find_min_index(A, p, r):
    min = float("+inf")
    min_index = -1

    for i in range(p, r):
        if A[i] < min:
            min_index = i
            min = A[i]

    return min_index

'''
Since the selection sort does a lot of comparisons, but relatively few copies, this sort of situation will favor it.
The insertion sort does a lot more copies, so in a situation like this, the slower copies will slow it down quite a bit.
'''
def selection_sort(A):
    # index of last element in sorted position
    i = 0

    for j in range(0, len(A)):
        minimum_index = find_min_index(A, j, len(A))

        if minimum_index != -1:
            # swap element at minimum index with i
            temp = A[minimum_index]
            A[minimum_index] = A[i]
            A[i] = temp

            i += 1


A = [0, 6, 8, 9, 3, 5, 1]

selection_sort(A)

print(A)
