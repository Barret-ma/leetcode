/**
 * @param {number[]} nums
 * @return {number}
 */
var jump = function(nums) {
    let curr = 0;
    let jumps = 0;
    let last = 0;
    for(let i = 0; i < nums.length; i ++) {
        
        if(i > last) {
            last = curr;
            jumps ++;
        }
        curr = Math.max(curr, i + nums[i]);
    }
    return jumps;
};

console.log(jump([2,3,1,1,4]));