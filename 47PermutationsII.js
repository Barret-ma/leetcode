/**
 * @param {number[]} nums
 * @return {number[][]}
 */
var permuteUnique = function(nums) {
    const result = [];
    const hashMap = new Set();
    const len = nums.length;

    function backtracking(list, copyList, num) {
        if(num != undefined) list.push(num);
        if(list.length === len) {
            if(!hashMap.has(list.join(''))) {
                hashMap.add(list.join(''));
                result.push(Object.assign([], list));
            }
            return;
        }
        
        for(let i = 0; i < copyList.length; i ++) {
            if(copyList[i] == copyList[i - 1]) continue;
            let remainList = Object.assign([], copyList);
            let pushNum = copyList[i];
            remainList.splice(i, 1);
            backtracking(list, remainList, pushNum);
            list.pop();
        }
    }
    backtracking([], nums);
    return result;
};

console.log(permuteUnique([1,1,2]));
console.log(permuteUnique([1,1]));
console.log(permuteUnique([1]));
console.log(permuteUnique([1,2,2]));
console.log(permuteUnique([0]));
