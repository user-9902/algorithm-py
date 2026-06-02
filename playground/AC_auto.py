"""
@title:      Aho-Corasick Automaton
@difficulty: 中等
@importance: 3/5
@tags:       trie KMP
"""

"""
寻找字符串子串的算法
流程如下：
    计算模式串的hash值，在文本串中寻找相同的hash值。
    在文本串中，创建一个和模式串长度相同的窗口。计算窗口的hash值。
    右移窗口，并更新hash值。（注意：更新hash值的操作必须是常数时间的，否则算法整体的复杂度不是线性的）
    窗口中的hash和模式串的hash相同时，即“可能”找到了目标字符串。（存在hash碰撞，hash相同还需要比较下具体的内容）
"""




from collections import defaultdict
class TrieNode:
    def __init__(self):
        self.children = defaultdict(TrieNode)
        self.fail = None  # 失败指针
        self.is_end_of_word = False  # 是否为模式串的结尾节点
        self.output = []  # 存储所有可由当前节点触发的模式串


class AhoCorasickAutomaton:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word):
        node = self.root
        for char in word:
            node = node.children[char]
        node.is_end_of_word = True
        node.output.append(word)

    def build_fail_pointers(self):
        queue = []
        for child in self.root.children.values():
            child.fail = self.root
            queue.append(child)

        while queue:
            r = queue.pop(0)
            for key, node in r.children.items():
                fail_node = r.fail
                while fail_node is not None and key not in fail_node.children:
                    fail_node = fail_node.fail
                if fail_node is not None:
                    node.fail = fail_node.children[key]
                else:
                    node.fail = self.root
                node.output.extend(node.fail.output)
                queue.append(node)

    def search(self, text):
        results = []
        current_node = self.root
        for index, char in enumerate(text):
            while current_node is not None and char not in current_node.children:
                current_node = current_node.fail
            if current_node is None:
                current_node = self.root
            else:
                current_node = current_node.children[char]
                for output_word in current_node.output:
                    if current_node.is_end_of_word:
                        results.append(
                            (output_word, index - len(output_word) + 1))
        return results


# 示例
if __name__ == "__main__":
    patterns = ["FOO", "BAR", "FOOBAR", "BARFOO"]
    ac_automaton = AhoCorasickAutomaton()
    for pattern in patterns:
        ac_automaton.insert(pattern)
    ac_automaton.build_fail_pointers()

    text = "FOOBARFOOBARFOO"
    matches = ac_automaton.search(text)
    print("Pattern matches found:")
    for match in matches:
        print(f"Pattern '{match[0]}' found at index {match[1]}")
