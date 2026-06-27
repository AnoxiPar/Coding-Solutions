class TrieNode:
    def __init__(self):
        self.data={}
        self.next=False
class Trie:
    def insert(self,node,word):
        for i in word:
            if i not in node.data:
                node.data[i]=TrieNode()
            node=node.data[i]
        node.next=True
    def lcp(self,node):
        res=""
        while(1):
            if(len(node.data)>1 or node.next==True):
                break
            for i in node.data:
                res+=i
                node=node.data[i]
        return res
class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        node=TrieNode()
        t=Trie()
        for i in strs:
            t.insert(node,i)
        return t.lcp(node)