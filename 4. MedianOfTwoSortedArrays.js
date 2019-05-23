var findMedianSortedArrays = function(nums1, nums2) {
    const m = nums1.length, n = nums2.length;
    const total = m + n;
    return (findKth(nums1, 0, nums2, 0, Math.floor((m + n + 1) / 2)) + findKth(nums1, 0, nums2, 0, Math.floor((m + n + 2) / 2))) / 2;

    function findKth(nums1, starta, nums2, startb, k) {
        console.log(`==================${k}====================`);
        if(starta >= nums1.length) {
            return nums2[startb + k - 1];
        }
        if(startb >= nums2.length) {
            return nums1[starta + k - 1];
        }
        if(k === 1) {
            return Math.min(nums1[starta + k - 1], nums2[startb + k - 1]);
        }

        let mid = Math.floor(k / 2 - 1);
        let midNum1 = starta + mid >= nums1.length ? Infinity : nums1[starta + mid];
        let midNum2 = startb + mid >= nums2.length ? Infinity : nums2[startb + mid];
        if(midNum1 > midNum2) {
            return findKth(nums1, starta, nums2, Math.floor(startb + k / 2), Math.ceil(k - k / 2));
        }
        else {
            return findKth(nums1, Math.floor(starta + k / 2), nums2, startb, Math.ceil(k - k / 2));
        }
    }
};

// console.log(findMedianSortedArrays([1, 3, 7], [1, 5, 11]));
// console.log(findMedianSortedArrays([1, 2], [3, 5, 9, 10]));
// console.log(findMedianSortedArrays([1], [1]))
console.log(findMedianSortedArrays([1], [2, 3, 4, 5, 6]))