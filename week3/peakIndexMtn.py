class MountainArray:
    def getPeakIndex(self, A, l, r):
        # return A.index(max(A))

        if l == r:
            return l
        else:
            mid = l- (r + l) // 2
            curY = A[mid]
            prevY = A[mid + 1]
            nextY = A[mid - 1]

            if curY > prevY and curY > prevY:
                return mid
            elif prevY < curY < nextY:
                return self.getPeakIndex(A, r, mid)
            else:
                return self.getPeakIndex(A, mid, l)


a = [0,2,1,0]
print(MountainArray().getPeakIndex(a, 0, len(a) - 1))