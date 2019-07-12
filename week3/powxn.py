class Power:
    def powHelper(self, x, n, val, neg):
        if(n == 0):
            return val
        else:
            nval = val
            if neg:
                nval = nval / x
            else:
                nval = nval * x
            return self.powHelper(x, n-1, nval, neg)

    def pown(self, x, n):
        return self.powHelper(x, n, 1, n<0)
    

        
    

print(Power().pown(10, 3))
