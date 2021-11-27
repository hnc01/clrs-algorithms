class Node:
    key = None
    right = None
    left = None
    parent = None

    def __init__(self, key):
        self.key = key


class BinaryTree:
    root = None

    def __init__(self, root):
        # root is Node
        self.root = root

    def insert(self, z):
        # z is Node
        y = None  # to keep track of parent
        x = self.root  # we will walk this pointer down the tree until we find a place for z

        while x is not None:
            y = x

            if z.key < x.key:
                x = x.left
            else:
                x = x.right

        z.parent = y

        if y == None:
            self.root = z  # case of empty tree
        elif z.key <= y.key:
            y.left = z
        else:
            y.right = z

    def delete(self, z):
        if z.left is None:
            # if z has only one child and it's right
            # we replace z by its right child
            self.transplant(z, z.right)
        elif z.right is None:
            # if z has only one child and it's left
            # we replace z by its left child
            self.transplant(z, z.left)
        else:
            # z has both children
            # replace it by its successor y who, by definition, doesn't have a left child
            # (otherwise it would have been the successor instead of y)

            # y is z's successor in right subtree
            y = self.minimum(z.right)

            # we replace y but its right child
            if y.parent != z:
                # y is not a direct child of z
                self.transplant(y, y.right)
                y.right = z.right
                y.right.parent = y

            # we replace z by floating y
            self.transplant(z, y)
            # update y's left child
            y.left = z.left
            y.left.parent = y

    # search for a key in tree rooted at x
    def search(self, x, k):
        if x is None or x.key == k:
            return x

        if k <= x.key:
            return self.search(x.left, k)
        else:
            return self.search(x.right, k)

    def to_string(self):
        self.to_string_helper(self.root, "")

    def to_string_helper(self, x, spacer):
        if x.right is not None:
            self.to_string_helper(x.right, spacer + "\t")

        print(spacer + str(x.key))

        if x.left is not None:
            self.to_string_helper(x.left, spacer + "\t")


    # replace u by v
    def transplant(self, u, v):
        if u.parent is None:
            self.root = v
        elif u == u.parent.left:
            # is a left child of its parent
            u.parent.left = v
        else:
            u.parent.right = v

        # we need to check the v is not null so we can call its parent attribute
        if v is not None:
            v.parent = u.parent

    # returns the minimum node rooted at node x
    def minimum(self, x):
        while x.left is not None:
            x = x.left

        return x

    # returns the maximum node rooted at node x
    def maximum(self, x):
        while x.right is not None:
            x = x.right

        return x

    # successor of node x
    def successor(self, x):
        # it's either x's minimum node in its right subtree or first left child on path from parent to root
        if x.right is not None:
            return self.minimum(x)
        else:
            # y is the lowest ancestor (closest to x in tree than root) of x whose left child is also an ancestor of x
            y = x.parent

            while y is not None and x == y.right:
                x = y
                y = y.parent

            # we break when y is None or x is a left child
            return y

    def predecessor(self, x):
        # it's either x's maximum node in its left subtree or first right child on path from parent to root
        if x.left is not None:
            return self.maximum(x)
        else:
            # y is the lowest ancestor (closest to x in tree than root) of x whose right child is also an ancestor of x
            y = x.parent

            while y is not None and x == y.left:
                x = y
                y = y.parent

            # we break when y is None or x is a left child
            return y


root = Node(8)

T = BinaryTree(root)

node_3 = Node(3)
T.insert(node_3)
T.insert(Node(6))
T.insert(Node(10))
T.insert(Node(13))
T.insert(Node(14))
T.insert(Node(4))
T.insert(Node(7))
T.insert(Node(1))

T.to_string()

T.delete(node_3)

result = T.search(T.root, 18)

if result is not None:
    print("The key was found in tree! " + str(result.key))
else:
    print("Could not find key in tree")