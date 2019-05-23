var removeNthFromEnd = function(head, n) {
    let nodeArr = [head];
    let p = head.next;
    while(p) {
        nodeArr.push(p);
        p = p.next;
    }
    nodeArr.splice(nodeArr.length - n, 1);
    let newHead;
    nodeArr.forEach((point, index) => {
        if(index == 0) {
            newHead = point;
            newHead.next = nodeArr[index + 1];
        }
        else point.next = nodeArr[index + 1] || null;
    })
    return newHead || null;
};

function ListNode(val) {
    this.val = val;
    this.next = null;
}

let l = new ListNode(1);

removeNthFromEnd(l, 1);