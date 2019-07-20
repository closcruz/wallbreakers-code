class Node:
    def __init__(self, x):
        self.data = x
        self.next = None


class NewList:
    def __init__(self):
        self.head = None

    def getNums(self):
        curr = self.head
        while curr:
            print(curr.data)
            curr = curr.next


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


def reverse(head):
    prev, curr = None, head
    while curr:
        temp = curr.next
        curr.next = prev
        prev = curr
        curr = temp

    return prev


def reverseKGroups(head, k):
    kCheck = 1
    last = newHead = None
    curr = temp = head
    while curr:
        if kCheck == k:
            # Reverse from temp to last
            last = curr.next
            curr.next = None
            newHead = reverse(temp)
            temp.next = last
            curr = temp
            temp = temp.next
            kCheck = 0
        else:
            # Traverse list
            curr = curr.next
            kCheck += 1


reverseKGroups(testL.head, 3)
testL.getNums()
