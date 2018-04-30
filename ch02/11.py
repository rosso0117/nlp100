# coding: utf-8

# UNIX
print("UNIX")
import subprocess
command = 'cat hightemp.txt | tr "\t" " "'

try:
    res = subprocess.check_call(command, shell=True)
    print('\n')
except:
    print('Error')
    print('\n')

# Python
print("Python")
replaced = [str(l).replace('\t', " ") for l in open("hightemp.txt", "r").readlines()]
for l in replaced:
    print(l, end='')