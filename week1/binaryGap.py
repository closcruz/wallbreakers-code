# Returns the longest count of consecutive 1's in the binary representation of N


class BinaryGap:
    def binaryGap(self, n):
        steps = [0]

        start = 0
        binArr = bin(n)[2:]

        step = 0
        for x in range(len(binArr)):
            if start and binArr[x] == '1':
                steps.append(step)
                step = 1
                continue
            elif binArr[x] == '1':
                start = 1
                step += 1
                continue
            else:
                step += 1

        return max(steps)


print(BinaryGap().binaryGap(22))
