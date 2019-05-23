var romanToInt = function(s) {
    const numMap = {
        'I': 1,
        'V': 5,
        'X': 10,
        'L': 50,
        'C': 100,
        'D': 500,
        'M': 1000
    };
    
    const arr = s.split('');
    let result = 0;
    for(let i = arr.length - 1; i >= 0; i --) {
        if(s[i] && s[i + 1] && numMap[s[i]] < numMap[s[i + 1]]) {

                result -= numMap[s[i]];
        }
        else {
            result += numMap[s[i]];
        }
    }
    
    console.log(result);
    return result;
};

romanToInt('III');
romanToInt('IV');
romanToInt('VI');
