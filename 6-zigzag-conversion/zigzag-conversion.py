class Solution:
    def convert(self, s: str, numRows: int) -> str:
        l = len(s)
        o =''
        step = max(1, 2*numRows - 2)
        for i in range(numRows):
            for j in range(i, l, step):
                o += s[j]
                if j+2*(numRows-i-1) < l and i != 0 and i != numRows-1:
                    o += s[j+2*(numRows-i-1)]

        return o
