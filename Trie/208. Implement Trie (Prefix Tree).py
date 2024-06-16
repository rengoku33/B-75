"""
Approach:
declare a clase TrieNode and __init__ with Hashmap (key= char, val= TrieNode), and endofword... perform insertion and search word/prefix

Time: O(26) => o(1) --- space: O(n)
"""

class TrieNode:
    def __init__(self):
        self.children = {}
        self.endofword = False

class Trie(object):

    def __init__(self):
        self.root = TrieNode()

    def insert(self, word):
        curr = self.root
        for c in word:
            if c not in curr.children:
                curr.children[c]=TrieNode()
            curr = curr.children[c]
        curr.endofword = True

    def search(self, word):
        curr = self.root
        for c in word:
            if c in curr.children:
                curr=curr.children[c]
            else:
                return False
        return curr.endofword

    def startsWith(self, prefix):
        curr = self.root
        for c in prefix:
            if c in curr.children:
                curr = curr.children[c]
            else:
                return False
        return True

