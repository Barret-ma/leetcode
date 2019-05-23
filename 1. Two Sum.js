/**
 * @param {number[]} nums
 * @param {number} target
 * @return {number[]}
 * Given nums = [2, 7, 11, 15], target = 9,

    Because nums[0] + nums[1] = 2 + 7 = 9,
    return [0, 1].
 */
var twoSum = function(nums, target) {
    const hashMap = {};
    let indexList = [];
    nums.forEach((k, index) => {
        hashMap[k] = index;
    });

    nums.forEach((k, index) => {
        let result = target - k;
        if(hashMap[result] != undefined && index != hashMap[result]) {
            indexList = [index, hashMap[result]];
        }
    });

    return indexList;
};

console.log(twoSum([3,3], 6));