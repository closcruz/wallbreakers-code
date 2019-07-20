from collections import deque


class MyStack:
    def __init__(self):
        self.stack = deque()

    def push(self, x):
        self.stack.appendleft(x)

    def pop(self):
        return self.stack.popleft()

    def top(self):
        return self.stack[0]

    def empty(self):
        return not self.stack


t1 = MyStack()

t1.push(2)
t1.push(1)
t1.push(3)

print(t1.pop())
