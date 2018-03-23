/**
 * Definition for singly-linked list.
 * function ListNode(val) {
 *     this.val = val;
 *     this.next = null;
 * }
 */
/**
 * @param {ListNode} l1
 * @param {ListNode} l2
 * @return {ListNode}
 */

function ListNode(val) {
	this.val = val;
	this.next = null;
}
var addTwoNumbers = function(l1, l2) {
    var lStack1 = [];
    var lStack2 = [];
    var point1 = l1;
    var point2 = l2;

    while(point1.next || point2.next) {
		lStack1.push(point1.val || 0);
		lStack2.push(point2.val || 0);
		point1 = point1 && point1.next || {};
		point2 = point2 && point2.next || {};

    }

    lStack1.push((point1 && point1.val) || 0);
    lStack2.push((point2 && point2.val) || 0);

    var val1, val2, sum, carry = 0;
    var lStack3 = [];
	for(var i = 0, len = lStack1.length; i < len; i ++) {
		val1 = lStack1[i];
		val2 = lStack2[i];

		sum = val1 + val2 + carry;
		carry = 0;
		if(sum >= 10) {
			carry = 1;
			lStack3.push(sum%10);
		}
		else {
			lStack3.push(sum);
		}
	}   

    if(carry) {
		lStack3.push(carry);
	}
	var result, point3, pointStart, pointMiddle;
	for(var j = 0, len = lStack3.length; j < len; j ++) {
		result = lStack3[j];
		point3 = new ListNode(result);
		if(j == 0) {
			pointStart = point3;
		}
		if(pointMiddle) {
			pointMiddle.next = point3;
		}
		pointMiddle = point3;
	}

	return pointStart;

};

var ll1 = new ListNode(3);
ll1.next = new ListNode(4);
ll1.next.next = new ListNode(2);


var ll2 = new ListNode(4);
ll2.next = new ListNode(6);
ll2.next.next = new ListNode(5);

addTwoNumbers(ll1, ll2);