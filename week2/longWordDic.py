# Given a list of strings words representing an English Dictionary, find the longest word in words that can be built one character at a time by other words in words.


class LongestWord:
    def longWord(self, words):
        check = sorted(words, key=lambda x: (-len(x), x))
        for w in check:
            a = True
            if not a:
                continue
            for i in range(len(w) - 1):
                if w[:i + 1] not in check:
                    a = False
                    break

            if a:
                return w


print(LongestWord().longWord(
    ["w", "wo", "wor", "worl", "world"]))
