/**
 * @param {string} s
 * @return {boolean}
 */
var isValid = function(s) {
    const track = [];
    for(let i = 0; i < s.length; i++) {
        const l = track.length - 1;
        if(s[i] == ')') {
            if(track && track[l] == '(') {
                track.pop();
            }
            else 
                track.push(s[i]);
        }
        else if(s[i] == '}') {
            if(track && track[l] == '{') {
                track.pop();
            }
            else 
                track.push(s[i]);
        }
        else if(s[i] == ']') {
            if(track && track[l] == '[') {
                track.pop();
            }
            else 
                track.push(s[i]);
        }
        else {
            track.push(s[i]);
        }
        
    }
    return !track.length;
};

// console.log(isValid('()'));
// console.log(isValid('()[]{}'));
// console.log(isValid('(]'));
// console.log(isValid('([)]'));
console.log(isValid(']'));