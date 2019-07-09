class SubsequentStrings:
    def isSubsequent(self, s, t):
        if s == "":
            return True

        if t == "":
            return False

        for c in s:
            if t.find(c) == -1:
                return False

            if len(s) == len(t):
                return True

            t = t[t.find(c) + 1:]

        return True


print(SubsequentStrings().isSubsequent("abc", "ahbgdc"))
