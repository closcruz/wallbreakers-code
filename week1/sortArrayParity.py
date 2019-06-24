# Sorts an array with non-negative integers by returning all the even numbers and then the odd numbers in another array


class SortParity:
    def sortParity(self, A):
        return [x for x in A if x % 2 == 0] + [y for y in A if y % 2 != 0]


print(SortParity().sortParity([2, 3, 1, 6]))
