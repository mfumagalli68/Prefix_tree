# Prefix_tree

Prefix tree for short time series predictions based on the paper "Short-term Time Series Forecasting with Regression
Automata".

Main file: Read data, execute an R script for saax representation and  execute functions in the prefix file.

Prefix file:

class TrieNode: build a node
class Trie: build a trie adding node thanks to insert function, which takes in input also the rolling window length.
