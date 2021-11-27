def get_max(A, index):
    max = float("-inf")

    for i in range(0, len(A)):
        if A[i] // 10 ** index % 10 > max:
            max = A[i] // 10 ** index % 10

    return max


def counting_sort(A, B, k, index):
    C = [0] * (k + 1)

    for j in range(0, len(A)):
        C[A[j] // 10 ** index % 10] += 1

    for i in range(1, len(C)):
        C[i] = C[i] + C[i - 1]

    for j in range(len(A) - 1, -1, -1):
        B[C[A[j] // 10 ** index % 10]] = A[j]

        C[A[j] // 10 ** index % 10] -= 1


def do_counting_sort(A, index):
    B = [None] * (len(A) + 1)
    k = get_max(A, index)

    counting_sort(A, B, k, index)

    B.pop(0)

    return B


# We can’t use counting sort because counting sort will take O(n2) which is worse than comparison-based sorting algorithms.
# Can we sort such an array in linear time? Yes, we use radix sort.

# Runtime Average-case, Best-case, Worst-case: Theta(d(n+k)) [if we're using counting sort as helper sorting algorithm]
# => if d is constant and the helper sorting algorithm is Theta(n) then radix sort is also Theta(n)
# In Place: No
# Stable: Yes (if we use a stable sorting algorithm as subroutine)
def radix_sort(A, d):
    for i in range(0, d):
        # do counting sort on array of
        A = do_counting_sort(A, i)

    return A


A = [29, 457, 657, 839, 19, 436, 720, 355, 101, 945, 288]
d = 3

A = radix_sort(A, d)

print(A)
