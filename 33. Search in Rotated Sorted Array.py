class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        def findSplitPivot(nums):
            # length = len(nums)
            # if length == 2:
            #     return 0 if nums[0] > nums[-1] else 1
            # mid = length / 2
            # if nums[0] > nums[mid - 1]:
            #     return mid - (len(nums[:mid]) - findSplitPivot(nums[:mid]))
            # elif nums[mid] > nums[-1]:
            #     return mid + findSplitPivot(nums[mid:])
            # else:
            #     return mid
            length = len(nums)
            mid = length / 2
            if len(nums) == 1:
                return 0 if nums[0] == target else -float('Inf')
            if nums[mid - 1] >= nums[0]:
                if target <= nums[mid - 1] and target >= nums[0]:
                    return mid - (len(nums[:mid]) - findSplitPivot(nums[:mid]))
                else:
                    return mid + (findSplitPivot(nums[mid:]))

            elif nums[mid] <= nums[-1]:
                if target <= nums[-1] and target >= nums[mid]:
                    return mid + findSplitPivot(nums[mid:])
                else:
                    return mid - (len(nums[:mid]) - findSplitPivot(nums[:mid]))

        if not nums:
            return -1
        if len(nums) == 1:
            return 0 if nums[0] == target else -1
        index = findSplitPivot(nums)
        return index if index >= 0 else -1
        # def findIndex(nums, target):
        #     if len(nums) == 0:
        #         return -1
        #     if len(nums) == 1:
        #         return 0 if nums[0] == target else -float('Inf')
        #     mid = len(nums) / 2
        #     if nums[mid] > target:
        #         return mid - (len(nums[:mid]) - findIndex(nums[:mid], target))
        #     elif nums[mid] < target:
        #         return mid + findIndex(nums[mid:], target)
        #     else:
        #         return mid
        # if not nums:
        #     return  -1
        # if len(nums) == 1:
        #     return 0 if nums[0] == target else -1
        # if nums[0] < nums[-1]:
        #     index = findIndex(nums, target)
        # else:
        #     index = findSplitPivot(nums)
        #     if nums[index] > target:
        #         if target < nums[0]:
        #             index = index + findIndex(nums[index:], target)
        #         else:
        #             index = index - (len(nums[:index]) - findIndex(nums[:index], target))
        #     elif nums[index] < target:
        #         if target <= nums[-1]:
        #             index = index + findIndex(nums[index:], target)
        #         else:
        #             index = index - (len(nums[:index]) - findIndex(nums[:index], target))
        # return index if index >= 0 else -1

t = Solution()
# test = [3,5,1]
# print t.search(test, 1)

# test = []
# print t.search(test, 5)

# test1 = [1,3]
# print t.search(test1, 1)

# test1 = [1,3]
# print t.search(test1, 0)

test2 = [4,5,6,7,0,1,2]
print t.search(test2, 1)
# test2 = [1,3]
# print t.search(test2, 3)

# test3 = [5,1,3]
# print t.search(test3, 3)
