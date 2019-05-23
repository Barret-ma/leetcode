var removeElement = function(nums, val) {
    let length = nums.length;
    let l = nums.length;
    nums.forEach((n, index) => {
        if(n !== val) {
            nums[l] = n;
            l ++;
        }    
    })
    nums.splice(0, length);
    return nums.length;
};

removeElement([0,1,2,2,3,0,4,2], 2);