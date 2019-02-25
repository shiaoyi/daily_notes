class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
            :type s: str
            :rtype: int
            """
        maxlen = 0
        newlen = 0
        #使用dictionary就可同時記住已紀錄的index、char
        indexhash = {}
        left = 0
        #enumerate可用在for，每次循環可觀察字串的一組index和character
        for index, char in enumerate(s):
            #in可用來查看字串1是否存在於字串2中。第二個是為了避免很久以前的字元亂了從left開始要觀察的順序，避免倒退觀察
            if (char in indexhash) and left <= indexhash[char]:
                newlen = index - left
                left = indexhash[char] + 1
                if maxlen < newlen:
                    maxlen = newlen
                #計算重複字之間有幾個字，下一輪才能繼續計算
                newlen = index - indexhash[char]
            else:
                newlen += 1
            #每次循環更新字元index
            indexhash[char] = index
            if maxlen < newlen:
                maxlen = newlen
        
        return maxlen
