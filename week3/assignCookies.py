class SplitCookies:
    def findContentChildren(self, g, s):
        s.sort(reverse=True)
        g.sort(reverse=True)

        i = 0
        while s and g:
            if s[0] >= g[0]:
                i += 1
                del s[0]
                del g[0]
            else:
                del g[0]

        return i


print(SplitCookies().findContentChildren([10, 9, 8, 7], [5, 6, 7, 8]))
