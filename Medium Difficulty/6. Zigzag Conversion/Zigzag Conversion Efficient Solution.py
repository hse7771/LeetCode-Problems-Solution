class Solution:
    def convert(self, s: str, numRows: int) -> str:
        result = ""
        if numRows == 1:
            return s
        begin = 0
        step = numRows * 2 - 2
        while begin < numRows:
            i = 0
            index = begin
            while index < len(s):
                result += s[index]
                if begin == 0 or begin == numRows-1:
                    index += step
                else:
                    if i % 2 == 0:
                        index += step
                    else:
                        index += (numRows * 2 - 2 - step)
                i += 1
            begin += 1
            step -= 2
            if step == 0:
                step = numRows * 2 - 2
        return result
