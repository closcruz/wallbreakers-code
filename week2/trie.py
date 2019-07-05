# Implemantation of Trie


class Node:
    def __init__(self):
        self.chars = [None] * 26
        self.isEnd = False


class Trie:
    def __init__(self):
        self.root = Node()

    def insert(self, word):
        stream = self.root

        for c in range(len(word)):
            i = ord(word[c]) - ord('a')  # Normalize index

            if not stream.chars[i]:
                stream.chars[i] = Node()
            stream = stream.chars[i]

        stream.isEnd = True

    def search(self, word):
        stream = self.root
        for c in range(len(word)):
            i = ord(word[c]) - ord('a')

            if not stream.chars[i]:
                return False

            stream = stream.chars[i]

        return stream != None and stream.isEnd

    def startsWith(self, prefix):
        stream = self.root
        isPrefix = True
        for c in prefix:
            if isPrefix:
                i = ord(c) - ord('a')

                if stream.chars[i]:
                    isPrefix = isPrefix and True
                else:
                    isPrefix = isPrefix and False

                stream = stream.chars[i]

        return isPrefix


words = ["the", "a", "there", "anaswe", "any", "by", "their"]

t1 = Trie()

for w in words:
    t1.insert(w)

print(t1.startsWith('car'))
