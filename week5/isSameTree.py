class Node:
    def __init__(self, val, left=None, right=None):
        self.v = val
        self.left = left
        self.right = right


class Tree:
    def __init__(self):
        self.root = None


t1, t2 = Tree(), Tree()
t1.root = Node(1, Node(3))
t2.root = Node(1, Node(3), Node(2))


def check(r, l):
    if not r:
        l.append(None)
        return
    if not r.left and not r.right:
        l.append(r.v)
        return
    else:
        l.append(r.v)
        check(r.left, l)
        check(r.right, l)


def isSame(p, q):
    l1, l2 = [], []
    check(p.root, l1)
    check(q.root, l2)
    return l1 == l2


print(isSame(t1, t2))
