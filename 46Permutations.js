/**
 * @param {number[]} nums
 * @return {number[][]}
 */
var permute = function(nums) {
    const result = [];
    function generatePermute(currentNums, n) {
        if(!currentNums) currentNums = [];
        if(n !== undefined) currentNums.push(n);
        if(currentNums && currentNums.length == nums.length) {
            result.push(Object.assign([], currentNums));
        }
        for(let i = 0; i < nums.length; i ++) {
            if(currentNums.indexOf(nums[i]) == -1) {
                generatePermute(currentNums, nums[i]);
                currentNums.pop();
                // currentNums.pop();
            }
        }
    };
    generatePermute();
    return result;
};

// console.log(permute([1,2, 3]));
// console.log(permute([1]));
console.log(permute([1,1,2]));