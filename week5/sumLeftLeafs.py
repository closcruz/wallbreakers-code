class Node:
    def __init__(self, val, left=None, right=None):
        self.v = val
        self.left = left
        self.right = right


class Tree:
    def __init__(self):
        self.root = None


t1 = Tree()
t1.root = Node(1, Node(2, Node(4), Node(5)), Node(3, Node(6), Node(7)))
t2 = Tree()
t2.root = Node(1, None, Node(2))


def checkLeftLeaf(root):
    if root.left:
        return not root.left.left and not root.left.right
    else:
        return False


def checkRightLeaf(root):
    if root.right:
        return not root.right.left and not root.right.right
    else:
        return False


def sumLeftLeafs(root):
    if not root or (root.left == None and root.right == None):
        return 0
    if checkLeftLeaf(root) and checkRightLeaf(root):
        return root.left.v
    else:
        if checkLeftLeaf(root) and not checkRightLeaf(root):
            return sumLeftLeafs(root.right) + root.left.v
        elif not checkLeftLeaf(root) and checkRightLeaf(root):
            return sumLeftLeafs(root.left)
        else:
            return sumLeftLeafs(root.left) + sumLeftLeafs(root.right)


print(sumLeftLeafs(t2.root))
