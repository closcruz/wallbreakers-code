# Take in an array of strings and return the longest common prefix of all them. Returning an empty string if one does not exist


class LongestPrefix:
    def longestPrefix(self, S):
        if S == None or len(S) == 0:
            return ""

        for i in range(len(S[0])):
            for j in range(1, len(S)):
                if i == len(S[j]) or S[j][i] != S[0][i]:
                    return S[0][0:i]

        return ""


print(LongestPrefix().longestPrefix(["flower", "flow", "flight"]))
