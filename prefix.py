

# Time:  O(n), per operation
# Space: O(1)
#
# Implement a trie with insert, search, and startsWith methods.
#
# Note:
# You may assume that all inputs are consist of lowercase letters a-z.
#

import sys
from pandas import *
import subprocess

class TrieNode:
    # Initialize your data structure here.
    def __init__(self,k):
        self.is_string = False
        self.number=k
        self.leaves = {}

    def getLetter(self):
        return (list(self.leaves.keys()))

class Trie:

    def __init__(self):
        self.root = TrieNode([0])

    # @param {string} word
    # @return {void}
    # Inserts a word into the trie.
    def insert(self, word,value,windowlength):


        window=0
        if(isinstance(windowlength,int)==False):
            sys.exit("errors, windowlength must be int")

        if(isinstance(word,str)==False):
            sys.exit("errors, word must be a string")
        if( isinstance(value,list)==False):
            sys.exit("errors, value must be a list")


        while( window < len(word)):
            flag=0
            l = list(word)
            l = [l[window:window + windowlength] for window in range(window, len(l), windowlength)]
            if(isinstance(l,str)==False):
                l = [''.join(i) for i in l][0]
            value_let = [value[window:window + windowlength] for window in range(window, len(value), windowlength)][0]
            l=list(l)
            cur = self.root
            for p, num in zip(l, value_let):
                if not p in cur.leaves:
                    cur.leaves[p] = TrieNode([num])
                    cur = cur.leaves[p]
                else:
                    cur = cur.leaves[p]
                    flag=flag+1
                    if(flag==windowlength):
                        cur.number.extend([num])

            cur.is_string = True

            window=window+1


    # @param {string} prefix
    # @return {boolean}
    # Returns if there is any word in the trie
    # that starts with the given prefix.

    def predict(self,letter,word,value):
        values=[]
        word = list(word)
        cur=self.root
        if letter in cur.leaves:
            cur=cur.leaves[letter]
            node_value=cur.number
            lista=list(cur.leaves.keys())
            for deep_trie in lista:
                values.extend(cur.leaves[deep_trie].number)

        else:
            for c in word:
                cur=cur.leaves[c]
                if letter in cur.leaves:
                    lista = list(cur.leaves.keys())
                    for deep_trie in lista:
                        values.extend(cur.leaves[deep_trie].number)

        predictions=node_value[0]+(sum(values)/len(values))

        return predictions




        #take the number associated at the letter followed by our letter




#ab ba ec cd-h


