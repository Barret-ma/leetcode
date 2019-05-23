/**
 * @param {number[]} nums
 * @return {number[][]}
 */
var threeSum = function(nums) {
    const result = [];
    nums = nums.sort(function (a, b) {
        return a - b;
    });
    let start = 0;
    for(start = 0; start <= nums.length - 3; start ++) {
        let left = start + 1;
        let right = nums.length - 1;
        if(nums[start] > 0) break;
        if(nums[start] == nums[start - 1]) continue;
        let target = 0 - nums[start];
        while(right > left) {
            let total = nums[left] + nums[right];
            
            if(total == target) {
                result.push([nums[start], nums[left], nums[right]]);
                while(nums[right] == nums[right - 1] && right > left) right --;
                while(nums[left] == nums[left + 1] && left < right) left ++;
                right --;
                left ++
            } else if(total > target) {
                right --;
            } else {
                left ++;
            }
        }
        
    }
    return result;
};

threeSum([-4,-2,-2,-2,0,1,2,2,2,3,3,4,4,6,6]);