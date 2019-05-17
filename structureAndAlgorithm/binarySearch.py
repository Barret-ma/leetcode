def binarySearch(nums, target):

    def findMid(nums, left, right, target):
        mid = left + (right - left) / 2
        if nums[mid] > target:
            return findMid(nums, left, mid - 1, target)
        elif nums[mid] < target:
            return findMid(nums, mid + 1, right, target)
        else:
            return mid
    return findMid(nums, 0, len(nums) - 1, target)

print binarySearch([1,2,3,4,88,99,102,150], 99)

