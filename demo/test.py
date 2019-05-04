# from collections import deque
# for i in range(4):
#     print i

# testArr = [1,2]
# testArr[0], testArr[1] = testArr[1], testArr[0]
# print testArr

# for i in range(2 * 0, 10, 2 * 0 + 1):
#     print i

# x = [12, 6, 9, 5, 4, 8]
# x = x[:len(x) - 1]
# print x

# def test():
#     for i in range(3):
#         print i
#         for j in range(4):
#             print j
#             if j == 2:
#                 return False
# print test()



# from collections import deque
# str = 'abcdecdcba'
# def palindrome(str):
#     dq = deque([])
#     for l in str:
#         dq.append(l)
#     while len(dq) != 1 and len(dq) != 0:
#         right = dq.pop()
#         left = dq.popleft()
#         if (right != left):
#             return False
#     return True

# print palindrome(str)

# from Queue import Queue
# l = ['a']
# print l + ['b']


# q = Queue()
# q.put('a')
# q.put('b')
# print q.get()
# # print len(q)
# print q.qsize()
# while not q.empty():
#     print q.get()
# q.put(('abc', 1))
# word, l = q.get()
# print word
# print l

# space = [['.'] * 4 for _ in range(4)]
# print space
# space[0][1] = ['Q']
# print space
# a = 'abc'

# print a[:0] + '.' + a[1:]
# a = 1
# print a ^ 1
# stack = []
# stack.append(1)
# stack.append(2)
# print stack.pop()
# dq = deque('abc')
# print len(dq)
# print dq.popleft()
l = []
l.append(None)
print l