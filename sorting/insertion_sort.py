# Runtime Average-case: Theta(n^2)
# Runtime Best-case (already sorted): O(n)
# Runtime Worst-case (reserve sorted): Theta(n^2)
# In Place: Yes
# Stable: Yes

def insertion_sort(a):
    for j in range(1, len(a)):
        key = a[j]

        # start with element before and keep going back
        i = j - 1

        while i >= 0 and key < a[i]:
            # keep shifting the elements to the right
            a[i+1] = a[i]

            i  = i - 1

        # place the current element in the right place
        # we need to add i + 1 because when we break the loop it would be after an extra i - 1
        a[i+1] = key


a = [4,6,8,9,3,5,1]

insertion_sort(a)

print(a)