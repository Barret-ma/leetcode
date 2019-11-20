var searchInsert = function(nums, target) {

    function binarySearch(n, t, p) {
        if(!n) return p;
        if(n.length <= 1) {
            return p;
        }
        let mid = n[Math.ceil(n.length / 2) - 1];
        if(mid < t) {
            return binarySearch(n.slice(Math.ceil(n.length / 2)), t, Math.ceil(n.length / 2) + p);
        }
        else if(mid > t){
            return binarySearch(n.slice(0, Math.ceil(n.length / 2)), t, p);
        }
        else {
            return p + Math.ceil(n.length / 2) - 1;
        }
    }
    
    const index = binarySearch(nums, target, 0);
    return target > nums[index] ? index + 1 : index;
};

console.log(searchInsert([1,3,5,6], 7));
console.log(searchInsert([1,3,5,6], 0));
console.log(searchInsert([1,3,5,6], 5));
console.log(searchInsert([1,3,5,6], 2));