def partition(A, p, r):
    # choosing the last element as pivot
    x = A[r]

    # index of the last element to be put in its place
    # => before q if it's less than q and after q if it's greater than q
    i = p - 1

    # we loop over all elements from p to r-1 (because at r we have the pivot)
    for j in range(p, r):
        # in this loop we only replace the elements that are less than the pivot
        # automatically after the loop is done, the only elements that are to the
        # right of the pivot are the ones greater than it
        if A[j] <= x:
            # we swap A[j] with the current index of elements less than pivot
            i += 1
            temp = A[j]
            A[j] = A[i]
            A[i] = temp

            # now at the index i we have an element in its place

    # we're done and we need to put the pivot in its place (after the elements less than it and before the elements greater than it)
    # since i is now index of the last elements less than the pivot, then i+1 is the right location of pivot
    # we then swap the pivot with element at i+1 which we know is greater than pivot
    temp = A[r]
    A[r] = A[i + 1]
    A[i + 1] = temp

    # return index of pivot
    return i + 1

# Runtime Average-case (when we partition same ratio every level): Theta(n lgn)
# Runtime Best-case (when we always partition in half): Theta(n lgn)
# Runtime Worst-case: Theta(n^2)
# In Place: No
# Stable: No
def quicksort(A, p, r):
    if p < r:
        q = partition(A, p, r)

        quicksort(A, p, q - 1)
        quicksort(A, q + 1, r)


from numpy import random

for i in range(0, 100):
    a = random.randint(100, size=100)
    b = a.copy()

    a = sorted(a)
    quicksort(b, 0, len(b) - 1)

    identical = True

    for j in range(0, len(a)):
        if a[j] != b[j]:
            identical = False
            break

    if identical:
        print("Arrays are identical")
    else:
        print("Arrays are not identical")