def partition(A, p, r):
    x = A[r]

    i = p - 1

    for j in range(p, r):
        if A[j] <= x:
            i += 1
            temp = A[j]
            A[j] = A[i]
            A[i] = temp

    temp = A[r]
    A[r] = A[i + 1]
    A[i + 1] = temp

    return i + 1


def select(A, p, r, i):
    if p == r:
        # we have one element in the subarray
        return A[p]

    q = partition(A, p, r)

    # k = number of elements in the first part of the partition (i.e. elements less than q)
    k = q - p  + 1

    # k is the number of elements less than or equal to pivot and pivot is the largest among them
    # so if we're looking for the ith smallest element with i = k, then we're looking the kth smallest element
    # which is the pivot since the smallest numbers out of the all the array are from p to q and the pivot is the largest
    # among them making it the kth smallest element of the entire array
    if i == k:
        # it means that we need the k'th element which is A[q] [since indexing starts at 0]
        return A[q]
    elif i < k:
        # it means the element we're looking for is in the first partition
        return select(A, p, q-1, i)
    else:
        # it means the element we're looking for is in the second partition
        # i = i - k (because we want the index with respect to second partition only => minus the whole first partition)
        return select(A, q+1, r, i-k)

A = [1,2,8,9,4]

ith_element = select(A, 0, len(A)-1, 3)

print(ith_element)