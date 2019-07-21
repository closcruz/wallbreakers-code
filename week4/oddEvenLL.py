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
    eCurr, oCurr = head.next, head
    eStart = eCurr
    while eCurr.next != None and eCurr != None:
        oCurr.next = eCurr.next
        oCurr = eCurr.next
        eCurr.next = oCurr.next
        eCurr = oCurr.next

    oCurr.next = eStart

    return head


oddEven(testL.head)
