
# Given an array of integers that is already sorted in ascending order, 
# find two numbers such that they add up to a specific target number.

# The function twoSum should return indices of the two numbers such that 
# they add up to the target, where index1 must be less than index2.

# Note:

# Your returned answers (both index1 and index2) are not zero-based.
# You may assume that each input would have exactly one solution and you 
# may not use the same element twice.
# Example:

# Input: numbers = [2,7,11,15], target = 9
# Output: [1,2]
# Explanation: The sum of 2 and 7 is 9. Therefore index1 = 1, index2 = 2.


class Solution(object):
    def twoSum(self, numbers, target):
        """
        :type numbers: List[int]
        :type target: int
        :rtype: List[int]
        """
        if not numbers:
            return
        numMap = dict()
        numIndex = dict()
        for i in range(len(numbers)):
            if numbers[i] in numMap:
                numMap[numbers[i]] += 1
                numIndex[numbers[i]].append(i + 1)
            else:
                numMap[numbers[i]] = 1
                numIndex[numbers[i]] = [i + 1]
        result = []
        for num in numbers:
            remain = target - num
            numMap[num] -= 1
            if remain in numMap and numMap[remain] > 0:
                if remain == num:
                    return numIndex[num]
                else:
                    result.append(numIndex[num][0])
                    result.append(numIndex[remain][0])
                return result
            numMap[num] += 1

s = Solution()
print(s.twoSum([0, 0, 3, 4], 0))
        


