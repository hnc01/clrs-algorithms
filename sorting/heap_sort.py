class MAX_HEAP:
    A = None
    size = 0

    def __init__(self, array=None):
        if array is not None:
            self.A = array
            self.size = len(array)

            # we don't need to apply max-heapify to leaves because they are heaps of size 1 so by default already max-heaps
            # we work our way from the level just before leaves up to root
            for i in range(int(self.size / 2), -1, -1):
                self.max_heapify(i)
        else:
            self.A = []

    def parent(self, i):
        index = int(i / 2) + 1

        if index < self.size:
            return index

        return None

    def left(self, i):
        index = (2 * i) + 1

        if index < self.size:
            return index

        return None

    def right(self, i):
        index = (2 * i) + 2

        if index < self.size:
            return index

        return None

    def max_heapify(self, i):
        left_child_index = self.left(i)
        right_child_index = self.right(i)

        # we need to make sure that the parent is bigger than both children
        # so we only perform action if the parent is less than either children
        # if the parent is less than at least of children, then we swap it with largest child

        largest = i

        if left_child_index is not None and self.A[i] < self.A[left_child_index]:
            largest = left_child_index

        # else largest = i (already implied from initially assigning largest to i)

        if right_child_index is not None and self.A[largest] < self.A[right_child_index]:
            # if right child is the biggest between element at i and element at left
            largest = right_child_index

        if largest != i:
            # swap between parent and max child
            temp = self.A[largest]
            self.A[largest] = self.A[i]
            self.A[i] = temp

            self.max_heapify(largest)

    def to_string(self):
        self.to_string_helper(0, "")

    def to_string_helper(self, i, spacer):
        left_child = self.left(i)
        right_child = self.right(i)

        if left_child is not None:
            self.to_string_helper(left_child, spacer + "\t")

        print(spacer + str(self.A[i]))

        if right_child is not None:
            self.to_string_helper(right_child, spacer + "\t")


def heapsort(A):
    # build a max heap from the array
    max_heap = MAX_HEAP(A)

    # we would manipulate the array in the max heap to become in sorted order as opposed to maintaining the heap property
    for i in range(max_heap.size - 1, 0, -1):
        # we put the past first element last (root is largest)
        temp = max_heap.A[0]
        max_heap.A[0] = max_heap.A[i]
        max_heap.A[i] = temp

        # we decrement the size of the heap because we don't want to cater for last element anymore (already in its sorted place)
        max_heap.size -= 1

        # rearrange the heap with the root that we just swapped in
        max_heap.max_heapify(0)


from numpy import random

for i in range(0, 100):
    a = random.randint(100, size=100)
    b = a.copy()

    a = sorted(a)
    heapsort(b)

    identical = True

    for j in range(0, len(a)):
        if a[j] != b[j]:
            identical = False
            break

    if identical:
        print("Arrays are identical")
    else:
        print("Arrays are not identical")