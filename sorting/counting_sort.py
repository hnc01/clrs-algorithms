# In practice, we only use counting sort when we have k = O(n) [where k is the range of the numbers],
# in which case the running time is Theta(n)

def get_max(A):
    max = float("-inf")

    for i in range(0, len(A)):
        if A[i] > max:
            max = A[i]

    return max

# Runtime Average-case, Best-case, Worst-case: Theta(k+n)
# In Place: No
# Stable: Yes

# k is range of numbers [max element]
def counting_sort(A, B, k):
    C = [0] * (k + 1)

    for j in range(0, len(A)):
        # we are adding 1 to the index equal to current element
        # we're counting how many times each element occurs
        C[A[j]] += 1

    # now we need to accumulate at each index the number of elements less than it
    for i in range(1, len(C)):
        C[i] = C[i] + C[i - 1]

    # now C[i] contains the number of elements less than or equal to i
    # now we need to put in B the sorted A
    # Note: we are starting with biggest element first and then placing them in their place => this means the algorithm is stable
    # but we do from 0 to len(A) it works correctly too
    for j in range(len(A) - 1, -1, -1):
        B[C[A[j]]] = A[j]

        C[A[j]] -= 1


A = [2, 5, 3, 0, 2, 3, 0, 3]
B = [None] * (len(A) + 1)
k = get_max(A)

counting_sort(A, B, k)

B.pop(0)

print(B)
