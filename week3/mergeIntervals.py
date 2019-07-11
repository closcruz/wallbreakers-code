class MergeIntervals:
    def mergeIntervals(self, intervals):
        starts = [intervals[i][0] for i in range(1, len(intervals))]
        ends = [intervals[i-1][1] for i in range(1, len(intervals) + 1)]
