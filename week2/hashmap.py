# Hashmap simple design


class Node:
    def __init__(self, key, val):
        self.data = (key, val)
        self.next = None


class HashMap:
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.list = [None] * 1000000

    def put(self, key: int, value: int) -> None:
        """
        value will always be non-negative.
        """
        i = key % 1000000

        if not self.list[i]:
            self.list[i] = Node(key, value)
        else:
            cur = self.list[i]
            while True:
                if cur.data[0] == key:
                    cur.data = (key, value)
                    return

                if not cur.next:
                    break

                cur = cur.next

            cur.next = Node(key, value)|

    def get(self, key: int) -> int:
        """
        Returns the value to which the specified key is mapped, or -1 if this map contains no mapping for the key
        """
        i = key % 1000000
        cur = self.list[i]

        while cur:
            if cur.data[0] == key:
                return cur.data[1]
            else:
                cur = cur.next

        return -1

    def remove(self, key: int) -> None:
        """
        Removes the mapping of the specified value key if this map contains a mapping for the key
        """
        i = key % 1000000
        cur = last = self.list[i]

        if not cur:
            return
        if cur.data[0] == key:
            self.list[i] = cur.next
        else:
            cur = cur.next
            while cur:
                if cur.data[0] == key:
                    last.next = cur.next
                    break
                else:
                    cur, last = cur.next, last.next


t1 = HashMap()
t1.put(1, 1)
t1.put(2, 2)
t1.get(1)
t1.get(3)
t1.put(2, 1)
t1.get(2)
t1.remove(2)
t1.get(2)
