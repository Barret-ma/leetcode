/**
 * @param {number[]} nums
 * @param {number} target
 * @return {number}
 */
var threeSumClosest = function(nums, target) {
    let result = null;
    let min = Infinity;
    nums = nums.sort(function (a, b) {
        return a - b;
    });

    let start = 0;
    for(start = 0; start <= nums.length - 3; start ++) {
        let left = start + 1;
        let right = nums.length - 1;
        // if(nums[start] > 0) break;
        if(nums[start] == nums[start - 1]) continue;
        let remain = target - nums[start];
        while(right > left) {
            let total = nums[left] + nums[right];
            if(total == remain) {
                min = 0;
                result = target;
                break;
            } else if(total > remain) {
                right --;
            } else {
                left ++;
            }
            if(Math.abs(total - remain) < min) {
                min = Math.abs(total - remain);
                result = nums[start] + total;
            }
        }
        
    }
    return result;
};

// console.log(threeSumClosest([-1, 2, 1, -4], 1));
// console.log(threeSumClosest([-1, 2, 1, -4], 3));
console.log(threeSumClosest([-1, 2, 1, -4], 0));
console.log(threeSumClosest([0, 0, 0], 0));