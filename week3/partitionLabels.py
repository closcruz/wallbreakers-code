class PartitionLabels:
    def partition(self, S):
        # Table to check last occurance of characters in string
        places = {i: c for c, i in enumerate(S)}

        # Start with the last occurence of the first character in string
        start = lastOcc = 0
        partLen = []    # What will be outputed
        for x in range(len(S)):
            lastOcc = max(lastOcc, places[S[x]])
            if x == lastOcc:
                partLen.append(x - start + 1)
                start = x + 1

        return partLen


print(PartitionLabels().partition("vhaagbqkaq"))
