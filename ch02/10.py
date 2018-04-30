# coding: utf-8

# UNIX
import subprocess
args = ['wc', '-l', 'hightemp.txt']

try:
    res = subprocess.check_call(args)
except:
    print("Error")

# Python
text = open("hightemp.txt", "r")

# 全行読み込み
lines = text.readlines()

# 行数表示
print(len(lines))

text.close()