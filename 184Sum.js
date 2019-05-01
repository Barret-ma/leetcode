/**
 * @param {number[]} nums
 * @param {number} target
 * @return {number[][]}
 */
var fourSum = function(nums, target) {
    nums = nums.sort((a, b) => {
        return a - b;
    });
    console.log(nums);
    const resultArr = [];
    let result = target;
    const length = nums.length;
    for(let i = 0; i < length - 3; i ++) {
        if(nums[i] === nums[i - 1]) {
            continue;
        }
        result = target - nums[i];
        for(let j = i + 1; j < length - 2; j ++) {
            if(nums[j] === nums[j - 1] && j != i + 1) {
                continue;
            }
            let temp = result - nums[j]; 
            let right = length - 1;
            let left = j + 1;
            
            while(right > left) {
                total = nums[right] + nums[left];
                if(total === temp) {
                    resultArr.push([nums[i], nums[j], nums[left], nums[right]]);
                    while(right > left && nums[right] == nums[right - 1]) right --;
                    while(left < right && nums[left] == nums[left + 1]) left ++
                    right --;
                    left ++;
                    continue;
                }
                else if(total > temp) {
                    right --;
                }
                else {
                    left ++;
                }
                
            }
        }
    }
    return resultArr;
};

// console.log(fourSum([-1,2,2,-5,0,-1,4], 3));

// console.log(fourSum([-1,-5,-5,-3,2,5,0,4], -7));
// console.log(fourSum([-1,0,1,2,-1,-4], -1));

// console.log(fourSum([0,0,0,0], 0));
// console.log(fourSum([1,0,-1,0,-2,2], 0));

// console.log(fourSum([-3,-2,-1,0,0,1,2,3], 0));
console.log(fourSum([-1,0,-5,-2,-2,-4,0,1,-2], -9));