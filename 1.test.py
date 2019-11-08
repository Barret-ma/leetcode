import copy
class Solution():
    def countSmaller(self, nums):
        # l = len(nums)
        # v = copy.deepcopy(nums)
        # v.sort()
        # bit = [0] * (l + 1)
        # print(v)
        # m = dict()
        # res = 0
        # for i in range(l):
        #     m[nums[i]] = i
        
        # for j in range(l - 1, -1, -1):
        #     pass
        def lower_bound(arr, target):
            low, high = 0, len(arr) - 1
            pos = len(arr)
            while low < high:
                mid = (low+high)/2 
                if arr[mid] <= target:
                    low = mid+1
                else:
                    high = mid
                    #pos = high
            if arr[low]>=target:
                pos = low
            return pos
        print(lower_bound([1,2,3,4], 2))
        

    def update(self, i, j, bit):
        while i < len(bit):
            bit[i] += j
            i += (i & -i)

    def search(self, i, bit):
        total = 0
        while i > 0:
            total += bit[i]
            i -= (i & -i)
        return total



s = Solution()
s.countSmaller([5,2,6,1])

