class Node:
    def __init__(self, val, left=None, right=None):
        self.v = val
        self.left = left
        self.right = right


class Tree:
    def __init__(self):
        self.root = None


t1 = Tree()
t1.root = Node(1, Node(2, Node(4, Node(6), Node(7)), Node(
    5, Node(8, Node(10), Node(11)), Node(9))), Node(3, None, Node(12)))

t2 = Tree()
t2.root = Node(1, Node(2, Node(3), Node(4)), Node(3))


def count(root, out):
    if not root:
        return 0
    else:
        l, r = count(root.left, out), count(root.right, out)

        if not out or l + r > out[0]:
            out[0] = l + r

        return max(l, r) + 1


def diameter(root):
    out = [0]
    count(root, out)
    return out[0]


print(diameter(t1.root))
