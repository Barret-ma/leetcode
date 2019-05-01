/**
 * Definition for singly-linked list.
 * function ListNode(val) {
 *     this.val = val;
 *     this.next = null;
 * }
 */
/**
 * @param {ListNode} head
 * @return {ListNode}
 */

function ListNode(val) {
    this.val = val;
    this.next = null;
}

var swapPairs = function(head) {
    if(!head || !head.next) {
        return head;
    }
    let p = head;
    let np = head.next;
    let newHead = head.next;
    let preNode = null;
    while(np) {
        if(!np.next) {
            np.next = p;
            p.next = null;
            if(preNode) {
                preNode.next = np;
            }
            break;
        }
        p.next = np.next;
        np.next = p;
        if(preNode) {
            preNode.next = np;
        }
        preNode = p;
        p = p.next;
        np = p && p.next;
    }
    return newHead;
};

let n1 = new ListNode(1);
let n2 = new ListNode(2);
let n3 = new ListNode(3);
let n4 = new ListNode(4);
let n5 = new ListNode(5);
let n6 = new ListNode(6);
n1.next = n2;
n2.next = n3;
n3.next = n4;
n4.next = n5;
n5.next = n6;

swapPairs(n1);