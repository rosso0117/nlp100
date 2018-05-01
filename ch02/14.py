# coding: utf-8
import sys

args = sys.argv

n = int(args[1])

lines = []
f = open('hightemp.txt', 'r')

for i in range(0, n):
    lines.append(f.readline())
f.close()

f = open('out_14.txt', 'w')
for l in lines:
    f.writelines(l)
f.close()

# check
import subprocess

command = 'cat hightemp.txt | head -n {n} > out_14_unix.txt'.format(n=n)
try:
    res = subprocess.check_call(command, shell=True)
except:
    print('Error')

command = 'diff out_14.txt out_14_unix.txt'
try:
    res = subprocess.check_call(command, shell=True)
    print(res)
except:
    print('Error')