class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        tlen = len(nums1) + len(nums2) 
        med = tlen / 2
        medval1 = 0
        medval2 = 0
        i = 0
        j = 0
        resind = 0
        res = 0
        while (med + 2) != resind:
            resind += 1
            if nums1 and (not nums2 or nums1[i] <= nums2[j]):
                if med == resind:
                    medval1 = nums1[i]
                if med + 1 == resind:
                    medval2 = nums1[i]
                i += 1
                if i == len(nums1):
                    nums1.append('')
            else:
                if med == resind:
                    medval1 = nums2[j]
                if med + 1 == resind:
                    medval2 = nums2[j]
                j += 1
                if j == len(nums2):
                    nums2.append('')
                
            
        if tlen % 2 == 0:
            res = (medval1 + medval2) / 2.0
        else:
            res = medval2
        
        return res