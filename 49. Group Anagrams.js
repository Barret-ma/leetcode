/**
 * @param {string[]} strs
 * @return {string[][]}
 */
var groupAnagrams = function(strs) {

    const m = new Map();
    for(let i = 0, len = strs.length; i < len; i ++) {
        let temp = strs[i].split('');
        temp = temp.sort((x, y) => {
            return x.charCodeAt(0) - y.charCodeAt(0);
        })
        let key = temp.join('');
        if(m.has(key)) {
            m.get(key).push(strs[i]);
        }
        else {
            m.set(key, [strs[i]]);
        }
    }
    const result = [];
    for(let value of m.values()) {
        result.push(value);
    }

    return result;
};

groupAnagrams(["eat", "tea", "tan", "ate", "nat", "bat"]);