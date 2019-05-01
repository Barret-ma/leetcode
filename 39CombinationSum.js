/**
 * @param {number[]} candidates
 * @param {number} target
 * @return {number[][]}
 */
var combinationSum = function(candidates, target) {
    candidates = candidates.sort((a, b) => {
        return a - b;
    })

    const resArr = [];
    const combinationSumRe = (candidatesNum, target, start, res) => {
        for(let i = start, len = candidatesNum.length; i < len; i ++) {
            if(target == 0) {
                resArr.push(Object.assign([], res));
                return;
            }
            if(candidatesNum[i] > target) {
                break;
            }

            res.push(candidatesNum[i]);
            combinationSumRe(candidatesNum, target - candidatesNum[i], i, res);
            res.pop();
        }
    };
    combinationSumRe(candidates, target, 0, []);
    return resArr;
};

combinationSum([2,3,6,7], 7);
combinationSum([2,3,5], 8);
combinationSum([1], 1);
combinationSum([10,11,12], 8);
