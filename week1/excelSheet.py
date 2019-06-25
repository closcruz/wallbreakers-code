class ExcelSheet:
    def charToNum(self,c):
        return ord(c) - 64
 
    def excelSheet(self, s):
        # out = list(s)[::-1]
        # num = [self.charToNum(x) * 26 ** i for i, x in enumerate(out)]

        return sum(self.charToNum(x) * 26 ** i for i, x in enumerate(list(s)[::-1]))

print(ExcelSheet().excelSheet('ZY'))