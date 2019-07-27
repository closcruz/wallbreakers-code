class Node:
    def __init__(self, val):
        self.v = val
        self.children = []


class Tree:
    def __init__(self):
        self.root = None

    def add(self, node):
        if self.root == None:
            self.root = node
        else:
            self.root.children.append(node)


def postOrder(root, out):
    if len(root.children) == 0:
        out.append(root.v)
        return
    else:
        for c in root.children:
            postOrder(c, out)

        out.append(root.v)


t1 = Tree()
t1.add(Node(1))
t1.add(Node(2))
t1.add(Node(3))

out = []
postOrder(t1.root, out)
print(out)
