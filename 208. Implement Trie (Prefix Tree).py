# Implement a trie with insert, search, and startsWith methods.

# Example:

# Trie trie = new Trie();

# trie.insert("apple");
# trie.search("apple");   // returns true
# trie.search("app");     // returns false
# trie.startsWith("app"); // returns true
# trie.insert("app");   
# trie.search("app");     // returns true
# Note:

# You may assume that all inputs are consist of lowercase letters a-z.
# All inputs are guaranteed to be non-empty strings.

class Trie(object):

    class TreeNode():
        def __init__(self):
            self.isWord = False
            self.children = [None] * 26

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.root = Trie.TreeNode()

    def insert(self, word):
        """
        Inserts a word into the trie.
        :type word: str
        :rtype: None
        """
        p = self.root
        for c in word:
            index = ord(c) - ord('a')
            if not p.children[index]:
                p.children[index] = Trie.TreeNode()
            p = p.children[index]
        p.isWord = True

    def search(self, word):
        """
        Returns if the word is in the trie.
        :type word: str
        :rtype: bool
        """
        node = self.find(word)
        return node is not None and node.isWord

    def startsWith(self, prefix):
        """
        Returns if there is any word in the trie that starts with the given prefix.
        :type prefix: str
        :rtype: bool
        """
        return self.find(prefix) is not None
    def find(self, prefix):
        p = self.root
        for c in prefix:
            index = ord(c) - ord('a')
            if not p.children[index]:
                return None
            p = p.children[index]
        return p



# Your Trie object will be instantiated and called as such:
obj = Trie()
for word in ["Trie","insert","search","search","startsWith","insert","search"]:
    obj.insert(word)
print(obj.search('apple'))
print(obj.startsWith('apple'))
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)