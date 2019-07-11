class ValidAnagram:
    def isValid(self, s, t):
        if len(s) != len(t):
            return False

        sArr, tArr = list(s), list(t)
        sArr.sort()
        tArr.sort()
        i = 0
        isValid = True
        while i < len(s):
            if not isValid:
                break

            if sArr[i] == tArr[i]:
                isValid = isValid and True
                i += 1
            else:
                isValid = isValid and False

        return isValid


print(ValidAnagram().isValid("cafr", "frat"))
