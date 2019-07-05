# Given a pattern to follow represented by characters, see if the given string follows the patter


class WordPattern:
    def followsPattern(self, pattern, words):
        patternSet = set(pattern)
        wordSet = set(words.split(" "))
        if len(patternSet) != len(wordSet):
            return False

        patternDict = dict(zip(list(pattern), list(words.split(" "))))
        patternCheck = [patternDict[c] for c in pattern]

        return " ".join(patternCheck) == words


print(WordPattern().followsPattern('abc', "b c a"))
