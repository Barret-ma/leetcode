/**
 * @param {string} digits
 * @return {string[]}
 */
var letterCombinations = function(digits) {
    const result = [];
    const digitsLetterMap = {
        2: 'abc',
        3: 'def',
        4: 'ghi',
        5: 'jkl',
        6: 'mno',
        7: 'pqrs',
        8: 'tuv',
        9: 'wxyz'
    };
    const digitsArr = digits.split('');

    function combine(letter, m) {
        let str = digitsLetterMap[digitsArr[m]];
        let strArr = str && str.split('') || [];
        if(m == (digitsArr.length - 1)) {
            strArr.forEach((l) => {
                result.push(letter + l);
            })
        }
        
        if(m === digitsArr.length - 1) {
            return null;
        }
        
        for(let i = 0; i < strArr.length; i ++) {
            combine(letter + strArr[i], m + 1);
        }
    }

    combine('', 0);

    return result;
};

// console.log(letterCombinations('23'));
// console.log(letterCombinations('2'));
console.log(letterCombinations('234'));