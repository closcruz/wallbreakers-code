# Flip a given 'image' first by reversing each row and then inverting its contents (1 -> 0 / 0 -> 1)


class FlipImage:
    def flipImage(self, A):
        # s = [x[::-1] for x in A]
        # p = [[int(not z) for z in y] for y in s]

        return [[int(not z) for z in y] for y in [x[::-1] for x in A]]


print(FlipImage().flipImage([[1, 1, 0], [1, 0, 1], [0, 0, 0]]))
