import heapq
from collections import Counter


class Node:
    def __init__(self, char, freq):
        self.char = char
        self.freq = freq
        self.left = None
        self.right = None

    def __lt__(self, other):
        return self.freq < other.freq


def build_huffman_tree(text):
    frequency = Counter(text)
    priority_queue = [Node(char, freq) for char, freq in frequency.items()]
    heapq.heapify(priority_queue)

    while len(priority_queue) > 1:
        left = heapq.heappop(priority_queue)
        right = heapq.heappop(priority_queue)

        merged = Node(None, left.freq + right.freq)
        merged.left = left
        merged.right = right

        heapq.heappush(priority_queue, merged)

    return priority_queue[0]


def huffman_codes(node, code="", mapping=None):
    if mapping is None:
        mapping = dict()

    if node is not None:
        if node.char is not None:
            mapping[node.char] = code
        huffman_codes(node.left, code + "0", mapping)
        huffman_codes(node.right, code + "1", mapping)

    return mapping


text = "this is an example for huffman encoding"
huffman_tree = build_huffman_tree(text)
codes = huffman_codes(huffman_tree)
print("Huffman Codes: ", codes)
