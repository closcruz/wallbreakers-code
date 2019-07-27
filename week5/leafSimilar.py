class Node:
    def __init__(self, val, left=None, right=None):
        self.v = val
        self.left = left
        self.right = right


class Tree:
    def __init__(self):
        self.root = None


t1 = Tree()
t1.root = Node(1)
t1.root.left = Node(2, Node(4), Node(5))
t1.root.right = Node(3, Node(6, Node(8)), Node(7))

t2 = Tree()
t2.root = Node(1)
t2.root.left = Node(2, Node(4), Node(5))
t2.root.right = Node(3, Node(6, Node(8)), Node(7))


def getLeafSeq(root, l):
    if not root:
        return
    if not root.left and not root.right:
        l.append(root.v)
        return
    else:
        getLeafSeq(root.left, l)
        getLeafSeq(root.right, l)


def leafSimilar(r1, r2):
    l1, l2 = [], []
    getLeafSeq(r1, l1)
    getLeafSeq(r2, l2)
    return l1 == l2


print(leafSimilar(t1.root, t2.root))
