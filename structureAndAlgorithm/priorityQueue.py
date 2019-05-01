class PriorityQueue(object):
    def __init__(self, queue):
        self.pq = []
        if queue and len(queue):
            self.pq = queue
        self.createHeap()

    def append(self, item):
        self.pq.append(item)
        self.createHeap()
        # print self.pq

    def pop(self):
        item = self.pq[0]
        self.pq[0], self.pq[len(self.pq) - 1] = self.pq[len(self.pq) - 1], self.pq[0]
        self.pq = self.pq[:len(self.pq) - 1]
        self.createHeap()
        return item

    def sort(self):
        self.createHeap()
        for k in range(len(self.pq) - 1, 0, -1):
            self.swap(self.pq, 0, k)
            self.adjust(self.pq, 0, k)

    def createHeap(self):
        for _i in range(len(self.pq) / 2 - 1, -1, -1):
            self.adjust(self.pq, _i, len(self.pq))

    def adjust(self, arr, i, length):
        temp = arr[i]
        for _i in range(i * 2 + 1, length,  3):
            if _i + 1 < length and arr[_i] < arr[_i + 1]:
                _i += 1
            if arr[_i] > temp:
                arr[i] = arr[_i]
                i = _i
            else:
                break
            arr[i] = temp
    def swap(self, arr, index1, index2):
        arr[index1], arr[index2] = arr[index2], arr[index1]

pq = PriorityQueue([4,6,8,5,9])

pq.append(12)

x = pq.pop()
print x

