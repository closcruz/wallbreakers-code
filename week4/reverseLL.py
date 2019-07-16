class Node:
    def __init__(self, x):
        self.data = x
        self.next = None


class ReverseList:
    def __init__(self):
        self.head = None


l1 = [4, 3, 6, 2, 1]


def makeLL(nums):
    ll = ReverseList()
    ll.head = Node(0)
    curr = ll.head
    for n in nums:
        curr.next = Node(n)
        curr = curr.next

    return ll


testL = makeLL(l1)


def reverseList(head):
    prev, curr = None, head
    while curr:
        temp = curr.next
        curr.next = prev
        prev = curr
        curr = temp

    return prev


print(reverseList(testL.head))
