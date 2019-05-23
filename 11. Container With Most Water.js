/**
 * @param {number[]} height
 * @return {number}
 */
var maxArea = function(height) {
    let l = 0, r = height.length - 1;
    let max = 0;
    while (r > l) {
        let area = Math.min(height[l], height[r]) * (r - l);
        if(area > max) {
            max = area;
        }
        if(height[l] > height[r]) {
            r --
        }
        else {
            l ++
        }
    }
    return max;
};

console.log(maxArea([1,8,6,2,5,4,8,3,7]));