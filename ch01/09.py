# coding: utf-8
import random

def sort_word(word):
    head = word[0]
    tail = word[len(word) - 1]
    l = list(word)[1:len(word)-1]

    random.shuffle(l)

    return head + "".join(l) + tail

str1 = "I couldn't believe that I could actually understand what I was reading : the phenomenal power of the human mind ."
ret = []
for w in str1.split(" "):
    if len(w) <= 4:
        ret.append(w)
    else:
        ret.append(sort_word(w))

print(" ".join(ret))