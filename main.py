# Read text from a file, and count the occurence of words in that text
# Example:
# count_words("The cake is done. It is a big cake!")
# --> {"cake":2, "big:1":1, "the":1, "a":1, "it":1}

from asyncio import coroutines
from asyncore import read
from itertools import count
from unittest.util import _count_diff_hashable

def read_file_content(filename):
    # [assignment] Add your code here
    with open('./story.txt') as f:
        filename = f.read()
    return filename


    def count_words():
        text = read_file_content('./story.txt')
        counts = dict()
        words = text.split(" ")

        for word in words:
            if word in counts:
                counts[word] += 1
            else:
                counts[words] += 1
        return counts
