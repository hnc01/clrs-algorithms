def partition(A, p, r, x):
    i = p - 1

    pivot_index = -1

    for j in range(p, r + 1):
        if A[j] <= x:
            i += 1
            temp = A[j]
            A[j] = A[i]
            A[i] = temp

            if A[i] == x:
                pivot_index = i

    # we need to put the pivot_index in its right place
    temp = A[pivot_index]
    A[pivot_index] = A[i]
    A[i] = temp

    return i


def insertion_sort(a):
    for j in range(1, len(a)):
        key = a[j]

        i = j - 1

        while i >= 0 and key < a[i]:
            a[i + 1] = a[i]

            i = i - 1

        a[i + 1] = key


def chunks(lst, p, r, n):
    """Yield successive n-sized chunks from lst."""
    for i in range(p, r + 1, n):
        limit = i + n

        if limit > r:
            limit = r + 1

        yield lst[i:limit]


def linear_select(A, p, r, i):
    # if array of 1 element then return the element
    if p == r:
        return A[p]

    # the array has more than one element
    # STEP 1: divide the n elements of the input array into floor(n/5) groups of 5 elements
    # each and at more one group made up of the remaining n % 5 elements
    groups = list(chunks(A, p, r, 5))

    # STEP 2: find the median of each of the groups by first insertion-sorting the elements
    # of each group (each has size maximum 5) and then picking the median from the sorted list of elements
    medians = []

    for group in groups:
        insertion_sort(group)
        median = group[int(len(group) / 2)]

        medians.append(median)

    # STEP 3: use linear_select recursively to find the median x of the medians found in step 2.
    # if there is an even number of medians, we stick to our convention by choosing x as the lower median.
    x = linear_select(medians, 0, len(medians) - 1, int(len(medians) / 2))

    # STEP 4: partition the input array around the median-of-medians x using a modified version of partition (we give it the pivot).
    # Let k be one more than the number of elements on the low side of the partition, so that x is the kth smallest element and there are
    # n-k elements on the high side of the partition.
    q = partition(A, p, r, x)

    k = q - p + 1

    # STEP 5:
    if i == k:
        return x
    elif i < k:
        return linear_select(A, p, q - 1, i)
    else:
        return linear_select(A, q + 1, r, i - k)


A = [5, 1, 7, 3, 2, 9, 0]

i = 7

print(linear_select(A, 0, len(A) - 1, i))

A.sort()

print(A[i - 1])
