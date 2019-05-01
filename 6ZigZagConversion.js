/**
 * @param {string} s
 * @param {number} numRows
 * @return {string}
 */
var convert = function(s, numRows) {
    let resultArr = [];
    let size = 2 * numRows - 2;

    for(let i = 0; i < numRows; i ++) {
        for(let j = i; j < s.length; j+= size) {
            resultArr.push(s[j]);
            console.log(j);
            if(i != 0 && i != numRows - 1) {
                let temp = j + size - 2 * i;
                if(temp < s.length) {
                    resultArr.push(s[temp]);
                }
            }
        }
    }
    return resultArr.join('');
};

console.log(convert('PAYPALISHIRING', 3));