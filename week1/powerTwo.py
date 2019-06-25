# Given non-negative int, find out if it is a power of two


class PowerTwo:
    def powerTwo(self, n):
        power = 0
        out = 0

        while out <= n:
            if 2 ** power == n:
                return True
            else:
                out = 2 ** power
                power += 1

        return False


print(PowerTwo().powerTwo(3))
