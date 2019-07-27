class Node:
    def __init__(self, val, left=None, right=None):
        self.v = val
        self.left = left
        self.right = right


class Tree:
    def __init__(self):
        self.root = None


t1 = Tree()
t1.root = Node(5, Node(4, Node(1), Node(1)), Node(5, None, Node(5)))
t2 = Tree()
t2.root = Node(1, Node(4, Node(4), Node(4)), Node(5, None, Node(5)))


def uniCount(root, out):
    if not root:
        return 0
    else:
        l, r = uniCount(root.left, out), uniCount(root.right, out)
        lCount, rCount = 0, 0

        if (root.left and root.right) and root.left.v == root.v and root.right.v == root.v:
            lCount = l + 1
            rCount = r + 1
        elif root.left and root.left.v == root.v:
            lCount = l + 1
        elif root.right and root.right.v == root.v:
            rCount = r + 1

        out[0] = max(out[0], lCount + rCount)
        return max(lCount, rCount)


def longUniPath(root):
    out = [0]
    uniCount(root, out)
    return out[0]


print(longUniPath(t2.root))
