class Node:
    def __init__(self, val, left=None, right=None):
        self.v = val
        self.left = left
        self.right = right


class Tree:
    def __init__(self):
        self.root = None


t1 = Tree()
t1.root = Node(1, Node(2), Node(3))


def findBottomLeft(root, left, level):
    if not root:
        return
    else:
        if level > left[1]:
            left[0] = root.v
            left[1] = level
        # Do postorder to hit all the leftmost leafs first
        findBottomLeft(root.left, left, level + 1)
        findBottomLeft(root.right, left, level + 1)


l = [t1.root.v, 0]
findBottomLeft(t1.root, l, 0)
print(l)
