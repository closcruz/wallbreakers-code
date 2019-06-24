# Reverse words in a string while preserving spaces and word order


class ReverseWords:
    def reverseWords(self, s):
        reversedSentence = " ".join(list(map(lambda x: x[::-1], s.split())))
        return reversedSentence


t1 = ReverseWords().reverseWords("Let's take LeetCode contest")
print(t1)
