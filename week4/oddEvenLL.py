class Node:
    def __init__(self, x):
        self.data = x
        self.next = None


class NewList:
    def __init__(self):
        self.head = None


l1 = [4, 3, 6, 2, 1]


def makeLL(nums):
    ll = NewList()
    ll.head = Node(0)
    curr = ll.head
    for n in nums:
        curr.next = Node(n)
        curr = curr.next

    return ll


testL = makeLL(l1)


def oddEven(head):
    o = oHead = Node(0)
    e = eHead = Node(0)
    isOdd = True
    while head:
        if isOdd:
            o.next = head
            o = o.next
        else:
            e.next = head
            e = e.next

        isOdd = not isOdd
        head = head.next

    e.next = None
    o.next = eHead

    return oHead


oddEven(testL.head)
