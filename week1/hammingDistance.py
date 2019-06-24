# Returns Hamming Distance, which is the number of positions at which the corresponding bits are different


class HammingDistance:
    def hammingDistance(self, x, y):
        # Check if bin representations are equal length, if not fix that
        if (len(bin(x)[2:]) == len(bin(y)[2:])):
            return sum(map(lambda x, y: x != y, bin(x)[2:], bin(y)[2:]))
        else:
            # Will store longest binary represantion
            binX = max(bin(x)[2:], bin(y)[2:], key=len)
            # Will store shortest binary represantion
            binY = min(bin(x)[2:], bin(y)[2:], key=len)

            tail = len(binX) - len(binY)
            # Add tail end 0 to make both bin reps equal length
            binY = (tail * '0') + binY

            # Iterates over both strings and checks each element to see if there are differences
            return sum(map(lambda x, y: x != y, binX, binY))


t1 = HammingDistance().hammingDistance(3, 5)
print(t1)
