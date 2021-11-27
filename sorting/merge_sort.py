# merge parts of array a
# lower part: p to q
# upper part: q+1 to r
def merge(a, p, q, r):
    # number of elements in lower part
    n1 = q - p + 1
    # number of elements in upper part
    n2 = r - q

    # we now create new arrays and fill them with elements
    # from upper and lower parts of a
    L = [float('-inf')] * n1
    R = [float('-inf')] * n2

    l_index = 0
    for i in range(p, q + 1):
        L[l_index] = a[i]
        l_index += 1

    r_index = 0
    for i in range(q + 1, r + 1):
        R[r_index] = a[i]
        r_index += 1

    # to iterate over L
    i = 0
    # to iterate over R
    j = 0
    # to iterate over a
    k = p

    for k in range(p, r + 1):
        # break the loop if one the arrays no longer has elements
        # in which case we need to fill A with the elements remaining in the other array
        if i >= len(L) or j >= len(R):
            break

        if L[i] <= R[j]:
            a[k] = L[i]
            i += 1
        else:
            # R[j] > L[i]
            a[k] = R[j]
            j += 1

    # filling a with whatever elements are left in either arrays
    while i < len(L):
        a[k] = L[i]
        i += 1
        k += 1

    while j < len(R):
        a[k] = R[j]
        j += 1
        k += 1

# Runtime Average-case: Theta(n lgn)
# Runtime Best-case: Theta(n lgn)
# Runtime Worst-case: Theta(n lgn)
# In Place: No
# Stable: Yes
def merge_sort(a, p, r):
    # ie if array is not empty
    if p < r:
        # q is the middle element so we're splitting the array in half
        q = int((p + r) / 2)

        merge_sort(a, p, q)
        merge_sort(a, q + 1, r)

        merge(a, p, q, r)


a = [10, 4, 6, 8, 9, 3, 5, 1]

merge_sort(a, 0, len(a) - 1)

# from numpy import random
#
# for i in range(0, 100):
#     a = random.randint(100, size=100)
#     b = a.copy()
#
#     a = sorted(a)
#     merge_sort(b, 0, len(b) - 1)
#
#     identical = True
#
#     for j in range(0, len(a)):
#         if a[j] != b[j]:
#             identical = False
#             break
#
#     if identical:
#         print("Arrays are identical")
#     else:
#         print("Arrays are not identical")

