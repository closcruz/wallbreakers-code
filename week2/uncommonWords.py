# Return the uncommon word in two sentences, which means the word that appears either in sentence one or two but not both

from collections import defaultdict


class UncommonWords:
    def findUncommonWords(self, A, B):
        wordCount = defaultdict(int)
        toCount = A.split(" ") + B.split(" ")

        for i in toCount:
            wordCount[i] += 1

        return list({k: v for (k, v) in wordCount.items() if v == 1}.keys())


print(UncommonWords().findUncommonWords(
    "this apple is sweet", "this apple is sour"))
