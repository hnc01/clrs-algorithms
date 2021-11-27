# transform numbers into 0. format
def transform_array(A):
    max_length = float("-inf")

    for i in range(0, len(A)):
        if len(str(A[i])) > max_length:
            max_length = len(str(A[i]))

    new_array = []

    for i in range(0, len(A)):
        new_array.append(A[i] / (10 ** max_length))

    return new_array


def insertion_sort(a):
    for j in range(1, len(a)):
        key = a[j]

        # start with element before and keep going back
        i = j - 1

        while i >= 0 and key < a[i]:
            # keep shifting the elements to the right
            a[i + 1] = a[i]

            i = i - 1

        # place the current element in the right place
        # we need to add i + 1 because when we break the loop it would be after an extra i - 1
        a[i + 1] = key


def bucket_sort(A):
    n = len(A)

    # we need to create an array with size n (to hold digit indices from 0 to n-1) and each element is an empty array
    B = [None] * n

    for j in range(0, len(B)):
        B[j] = []

    # now we go over the elements in A and insert each into the appropriate bucket
    # here the bucket index is decided based on the first integer after the decimal point
    for i in range(0, len(A)):
        index = int(n * A[i])
        bucket = B[index]

        bucket.append(A[i])

    # now we need to sort each bucket
    for j in range(0, len(B)):
        insertion_sort(B[j])

    sorted_array = []

    for j in range(0, len(B)):
        if len(B[j]) > 0:
            sorted_array.extend(B[j])

    return sorted_array


# A = [0.78, 0.17, 0.39, 0.26, 0.72, 0.94, 0.21, 0.12, 0.23, 0.68]
# A = bucket_sort(A)
# print(A)

A = [78, 17, 397, 26, 2, 94, 21, 12, 23, 68]
A = transform_array(A)
A = bucket_sort(A)
print(A)
