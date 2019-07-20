class ValidParenthesis:
    def checkParenthesis(self, s):
        if not s:
            return True

        check = list(s)
        out = []

        while check:
            out.append(check.pop())
            if len(out) > 1:
                if (out[-1] == '(' and out[-2] == ')') or (out[-1] == '[' and out[-2] == ']') or (out[-1] == '{' and out[-2] == '}'):
                    del out[-1], out[-1]

        return True if not out else False


print(ValidParenthesis().checkParenthesis('()'))
