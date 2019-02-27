class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        length = len(s)
        maxindex = 0
        currentindex = 0
        res = ''
        for i,char in enumerate(s):
            if (i+1 < length) and (i-1 >= 0) and s[i+1] == s[i-1]:
                j = i + 1
                k = i - 1
                while j < length and k >= 0 and s[j] == s[k]:
                    j += 1
                    k -= 1
                j -= 1
                k += 1
                currentindex = j - k + 1
                if currentindex > maxindex:
                    maxindex = currentindex
                    res = s [k:j+1]
            if (i+1 < length and s[i+1] == char) or (i-1 >= 0 and s[i-1] == char):
                j = i + 1
                k = i - 1
                if j < length and s[j] == char:
                    while i >= 0 and j < length and s[i] == s[j]:
                        i -= 1
                        j += 1
                    j -= 1
                    i += 1
                    currentindex = j - i + 1
                    if currentindex > maxindex:
                        maxindex = currentindex
                        res = s [i:j+1]
                elif k >= 0 and s[k] == char:
                    while k >= 0 and i < length and s[k] == s[i]:
                        k -= 1
                        i += 1
                    i -= 1
                    k += 1
                    currentindex = i - k + 1
                    if currentindex > maxindex:
                        maxindex = currentindex
                        res = s [k:i+1]
            else:
                currentindex = 1
                if currentindex > maxindex:
                    maxindex = currentindex
                    res = char
                        
        return res

        # 還能改善的方法：過程中發現if裡的結構都差不多，可以寫成一個函式來呼叫，程式碼會更簡潔