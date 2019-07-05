# Implementation of a hashset in python


class Node:
    def __init__(self, val):
        self.data = val
        self.next = None


class HashSet:
    def __init__(self):
        self.list = [None] * 10000

    def add(self, key):
        i = key % 10000

        if not self.list[i]:
            self.list[i] = Node(key)
        else:
            cur = self.list[i]
            while True:
                if cur.data == key:
                    return

                if not cur.next:
                    break

                cur = cur.next

            cur.next = Node(key)

    def contains(self, key):
        i = key % 10000
        cur = self.list[i]

        while cur:
            if cur.data == key:
                return True
            else:
                cur = cur.next

        return False

    def remove(self, key):
        i = key % 1000000
        cur = last = self.list[i]

        if not cur:
            return
        if cur.data == key:
            self.list[i] = cur.next
        else:
            cur = cur.next
            while cur:
                if cur.data == key:
                    last.next = cur.next
                    break
                else:
                    cur, last = cur.next, last.next


t1 = HashSet()
t1.add(1)
t1.add(2)
t1.contains(1)
t1.contains(3)
t1.add(2)
t1.contains(2)
t1.remove(2)
t1.contains(2)
