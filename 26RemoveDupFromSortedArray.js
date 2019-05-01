var removeDuplicates = function(nums) {
    let current = null;
    const l = nums.length;
    for(let i = 0; i < l; i ++) {
        
        if(current !== nums[i]) {
            current = nums[i];
            nums.push(current);
        }
    }
    nums.splice(0, l);
    return nums.length;
};

console.log(removeDuplicates([1,1,2]));