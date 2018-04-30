# coding: utf-8

s = "Hi He Lied Because Boron Could Not Oxidize Fluorine. New Nations Might Also Sign Peace Security Clause. Arthur King Can."
l = [1, 5, 6, 7, 8, 9, 15, 16, 19]
d = {}

for (i, w) in enumerate(s.split(" ")):
    index = i + 1
    if index in l:
        c = w[0:1]
        d[c] = index
    else:
        c = w[0:2]
        d[c] = index

print(d)
