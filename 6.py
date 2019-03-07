class Solution(object):
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        length = len(s)
        left = 0
        interval = 2*numRows-2
        current_interval = 0
        newval = ''
        
        if length <= numRows or numRows == 1:
            return s
        for i in range (numRows):
            currenti = i
            newval += s[currenti]
            current_interval = interval - 2 * i
            if current_interval == 0:
                current_interval = interval
            currenti += current_interval
            while(length > currenti):
                newval += s[currenti]
                if current_interval < interval:
                    current_interval = interval - current_interval
                elif current_interval == 0:
                    current_interval = interval
                currenti += current_interval
                
        return newval