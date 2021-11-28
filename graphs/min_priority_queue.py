class MIN_HEAP:
    A = None
    size = 0

    def __init__(self, array=None):
        if array is not None:
            self.A = array
            self.size = len(array)

            # we don't need to apply max-heapify to leaves because they are heaps of size 1 so by default already max-heaps
            # we work our way from the level just before leaves up to root
            for i in range(int(self.size / 2), -1, -1):
                self.min_heapify(i)
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

    def min_heapify(self, i):
        left_child_index = self.left(i)
        right_child_index = self.right(i)

        # we need to make sure that the parent is bigger than both children
        # so we only perform action if the parent is less than either children
        # if the parent is less than at least of children, then we swap it with largest child

        smallest = i

        if left_child_index is not None and self.A[i].d > self.A[left_child_index].d:
            smallest = left_child_index

        # else largest = i (already implied from initially assigning largest to i)

        if right_child_index is not None and self.A[smallest].d > self.A[right_child_index].d:
            # if right child is the biggest between element at i and element at left
            smallest = right_child_index

        if smallest != i:
            # swap between parent and max child
            temp = self.A[smallest]
            self.A[smallest] = self.A[i]
            self.A[i] = temp

            self.min_heapify(smallest)

    def extract_min(self):
        if self.size > 0:
            min = self.A[0]

            self.A[0] = self.A[self.size - 1]
            self.size = self.size - 1
            self.min_heapify(0)

            return min

        return None

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
