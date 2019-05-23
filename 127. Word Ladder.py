from Queue import Queue

class Solution(object):
    def ladderLength(self, beginWord, endWord, wordList):
        """
        :type beginWord: str
        :type endWord: str
        :type wordList: List[str]
        :rtype: int
        """
        if endWord not in wordList:
            return 0
        q = Queue()
        wordSet = set(wordList)
        q.put((beginWord, 1))
        while q.qsize():
            word, length = q.get()
            if word == endWord:
                return length
            for i in range(len(word)):
                for c in 'abcdefghijklmnopqrstuvwxyz':
                    nextWord = word[:i] + c + word[i + 1:]
                    if nextWord != word and nextWord in wordSet:
                        wordSet.remove(nextWord)
                        q.put((nextWord, length + 1))
        return 0
s = Solution()
print s.ladderLength('hit', 'cog', ["hot","dot","dog","lot","log","cog"])
print s.ladderLength('hit', 'cog', ["hot","dot","dog","lot","log"])