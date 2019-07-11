class PopBallons:
    def popBallons(self, points):
        if not points:
            return 0

        points.sort()   # Will sort so we have increasing start posistions which will help counting what will be popped

        # mX will keep track of the max width for each ballon in points and saves it to compare to see if we need to shoot another arrow at different position
        # mX is instiated with -float('inf') to accounr for possible negative starting width ballons
        shots, mX = 0, -float('inf')
        for s, e in points:
            if s > mX:
                shots += 1
                mX = e
            else:
                # If no new shot is needed we set new max width to smallest value between the last max width or the current end point of ballon
                mX = min(mX, e)

        return shots


print(PopBallons().popBallons([[10, 16], [2, 8], [1, 6], [7, 12]]))
