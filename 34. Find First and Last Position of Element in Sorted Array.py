class Solution(object):
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        if not nums:
            return [-1, -1]
        
        left = 0
        right = len(nums) - 1
        index = -1
        while left <= right:
            mid = left + (right - left) / 2
            if nums[mid] == target:
                global index
                index = mid
                break
            if nums[mid] > target:
                right = mid - 1
            else:
                left = mid + 1
        if index == -1:
            return [-1, -1]
        else:
            lp = rp = index
            lv = nums[lp]
            rv = nums[rp]
            while lv == target or rv == target:
                    if lv == target: 
                        lp -= 1
                        if lp>= 0: lv = nums[lp]
                        else: lv = None
                    if rv == target:
                        rp += 1
                        if rp< len(nums): rv = nums[rp]
                        else: rv = None
                
            return [lp + 1, rp - 1] if rp != lp + 1 else [lp + 1, rp]
t = Solution()
# test = [1, 2, 3, 4, 4, 4, 5, 6, 7, 8, 9]
# print t.searchRange(test, 4)

# test1 = [1, 2, 3, 4, 4, 4, 5, 6, 7, 8, 9]
# print t.searchRange(test1, 0)

test2 = [2, 2]
print t.searchRange(test2, 2)

# test3 = [1,2,3,4,6]
# print t.searchRange(test3, 6)

# test4 = [1,1,2,3,4,6,6]
# print t.searchRange(test4, 1)