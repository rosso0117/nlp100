# coding: utf-8
def get_n_gram_set(target, n):
    res = set()
    for i in range(0, len(target) - n + 1):
        res.add(target[i:i+n])
    return res

# paradise
s1 = "paraparaparadise"
set1 = get_n_gram_set(s1, 2)

# paragraph
s2 = "paragraph"
set2 = get_n_gram_set(s2, 2)


# セット
print("set1", set1)
print("set2", set2)

# 和集合
print("和集合", set1 | set2)

# 積集合
print("積集合", set1 & set2)

# 差集合
print("差集合", set1 - set2)