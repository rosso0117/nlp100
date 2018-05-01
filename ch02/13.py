# coding: utf-8

f1 = open('col1.txt')
f2 = open('col2.txt')
f1_lines = f1.readlines()
f2_lines = f2.readlines()
merged = []

for (l1, l2) in zip(f1_lines, f2_lines):
    merged.append(l1.replace('\n', '') + '\t' + l2)

f1.close()
f2.close()

f_merged = open('col_merged.txt', 'w')
for l in merged:
    f_merged.writelines(l)

f_merged.close()

# check
import subprocess

command = 'paste col1.txt col2.txt > col_merged_unix.txt'
try:
    res = subprocess.check_call(command, shell=True)
except:
    print('Error')

command = 'diff col_merged.txt col_merged_unix.txt'
try:
    res = subprocess.check_call(command, shell=True)
    print(res)
except:
    print('Error')