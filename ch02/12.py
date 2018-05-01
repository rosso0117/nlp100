# coding: utf-8

# UNIX
import subprocess
command = 'cut -c 1 hightemp.txt > col1_unix.txt'
try:
    res = subprocess.check_call(command, shell=True)
    print('\n')
except:
    print('Error')
    print('\n')

command = 'cut -c 2 hightemp.txt > col2_unix.txt'
try:
    res = subprocess.check_call(command, shell=True)
    print('\n')
except:
    print('Error')
    print('\n')

# Python
import os
print("Python")

col1 = []
col2 = []

f = open('hightemp.txt', 'r')
lines = f.readlines()
f.close()

os.remove('col1.txt')
os.remove('col2.txt')
wf1 = open('col1.txt', 'w')
wf2 = open('col2.txt', 'w')

for (i, l) in enumerate(lines):
    wf1.writelines(l[0])
    wf1.writelines('\n')
    wf2.writelines(l[1])
    wf2.writelines('\n')

wf1.close()
wf2.close()

# check
command = 'diff col1.txt col1_unix.txt'
try:
    res = subprocess.check_call(command, shell=True)
    print(res)
except:
    print('Error')
    print('\n')

command = 'diff col2.txt col2_unix.txt'
try:
    res = subprocess.check_call(command, shell=True)
    print(res)
except:
    print('Error')
    print('\n')