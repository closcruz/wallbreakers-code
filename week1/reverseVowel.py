# Reverses the vowels of a given string


class ReverseVowel:
    def reverseVowel(self, s):
        left, right = 0, len(s) - 1
        vowels = ['a', 'e', 'i', 'o', 'u']
        st = list(s)

        while left <= right:
            if st[left] in vowels and st[right] in vowels:
                st[left], st[right] = st[right], st[left]
                left += 1
                right -= 1
                continue
            elif st[left] in vowels and not st[right] in vowels:
                right -= 1
                continue
            elif not st[left] in vowels and st[right] in vowels:
                left += 1
                continue
            else:
                left += 1
                right -= 1

        return "".join(st)


print(ReverseVowel().reverseVowel("hello"))
