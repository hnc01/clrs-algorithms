# Bubble Sort is the simplest sorting algorithm that works by repeatedly swapping the adjacent elements if they are in wrong order.
# In Place: Yes
# Stable: Yes

# Runtime: theta(n^2)
def bubble_sort(a):
    # we don't need to pass through the elements len(a) times because when we are placing the element before last in its place
    # automatically the last element would be in its place so we need to pass number_of_elements - 1
    for i in range(0, len(a) - 1):
        # because we are comparing current element with next element, we need to stop at last_element - 1
        for j in range(0, len(a) - 1):
            if a[j] > a[j + 1]:
                # swap them
                temp = a[j]
                a[j] = a[j + 1]
                a[j + 1] = temp


# Runtime Worst-case: O(n^2)
# Runtime Best-case (already sorted): O(n)
def optimized_bubble_sort(a):
    for i in range(0, len(a) - 1):
        swapped = False

        for j in range(0, len(a) - 1):
            if a[j] > a[j + 1]:
                # swap them
                temp = a[j]
                a[j] = a[j + 1]
                a[j + 1] = temp

                swapped = True

        # stop when array is sorted (no need for the extra passes)
        if not swapped:
            break


a = [4, 6, 8, 9, 3, 5, 1]

bubble_sort(a)

print(a)

a = [4, 6, 8, 9, 3, 5, 1]

optimized_bubble_sort(a)

print(a)
