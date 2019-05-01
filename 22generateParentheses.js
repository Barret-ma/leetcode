/**
 * @param {number} n
 * @return {string[]}
 */
var generateParenthesis = function(n) {
    const map = {
        '(': 1,
        ')': -1
    }
    let result = [];
    let tempArr = [];
    function backtracking(parenthesis, tempArr, count) {
        tempArr.push(parenthesis);
        if(count < 0 || (count + map[parenthesis]) > n) {
            return;
        }
        else {
            count = count + map[parenthesis];
        }
        
        if(tempArr.length === (2 * n) && count === 0) {
            result.push(tempArr.join(''));
            return;
        }
        else if(tempArr.length === (2 * n) && count !== 0) {
            return;
        }
        backtracking('(', tempArr, count);
        tempArr.pop();
        backtracking(')', tempArr, count);
        tempArr.pop();
    }

    backtracking('(', tempArr, 0);
    return result;
};

generateParenthesis(1);
generateParenthesis(2);
generateParenthesis(3);