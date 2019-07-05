# Given a paragraph and a list of banned words, return the most common word that is not banned

from collections import Counter
from string import punctuation


class CommonWord:
    def mostCommonWord(self, paragraph, banned):
        cleanP = Counter([s.lower() for s in paragraph.translate(str.maketrans(
            punctuation, ' ' * len(punctuation))).split(' ') if s != ''])

        val = 0
        word = ""
        for k, v in cleanP.items():
            if k in banned:
                continue

            if val < v:
                val = v
                word = k

        return word


print(CommonWord().mostCommonWord(
    "Bob hit a ball, the hit BALL flew far after it was hit.",
    ["hit"]))
