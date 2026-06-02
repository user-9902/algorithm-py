"""
@title:      211. 添加与搜索单词 - 数据结构设计
@difficulty: 中等
@importance: 4/5
@tags:       字典树
"""
from collections import defaultdict


class TrieNode:
    def __init__(self):
        self.children = defaultdict(TrieNode)
        self.is_end_of_word = False


class WordDictionary:

    def __init__(self):
        self.root = TrieNode()

    def addWord(self, word: str) -> None:
        cur = self.root
        for c in word:
            cur = cur.children[c]
        cur.is_end_of_word = True

    def search(self, word: str) -> bool:
        def dfs(node, word):
            n = len(word)
            for i in range(n):
                if word[i] == '.':
                    for node in node.children:
                        return any(node, word[i+1:])
                cur = node.children.get(word[i])
                if cur is None:
                    return False
            return cur.is_end_of_word

        return dfs(self.root, word)
