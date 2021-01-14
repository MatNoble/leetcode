#==================================================
#==>      Title: Python Basic
#==>     Author: Zhang zhen                   
#==>      Email: hustmatnoble.gmail.com
#==>     GitHub: https://github.com/MatNoble
#==>       Date: 1/14/2021
#==================================================

import os
path = './python basic'

print('==================')
f = open(path + '/file.txt', 'r')
print(f.read())
f.close()

print('==================')
f = open(path + '/file.txt', 'r')
print(f.read(5) + '\n')
f.close()

print('==================')
f = open(path + '/file.txt', 'r')
print(f.readline())
print(f.readline())
f.close()

print('==================')
f = open(path + '/file.txt', 'r')
for x in f:
    print(x)
f.close()

print('==================')
f = open(path + '/file.txt', 'a')
f.write("Now this file has more content!\n")
f.close()

f = open(path + '/file.txt', 'r')
print(f.read())
f.close()

print('==================')
f = open(path + '/test.txt', 'w')
f = open(path + '/test1.txt', 'w')

# del
os.remove(path + '/text1.txt')

