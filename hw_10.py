import os
import re

#Задача 3
file_path = 'info.txt'
with open(file_path, 'r', encoding='utf-8') as f:
    line = f.readline().lower()
    while line:
        line = line.split()
        s = {}
        i1 = 0
        i2 = ''
        q = 0
        t = []
        min1 = 0
        for i in line:
            if i not in s:
                s[i] = 1
            else:
                s[i] += 1
        for values in s.values():  # нахожу максимальное повторение
            if values > i1:
                i1 = values
        for keys, values in s.items():
            if values == i1:
                min1 = keys
        for keys, values in s.items():
            if values == i1:
                if min1 > keys:
                    min1 = keys
        print(min1, i1)
        line = f.readline().lower()

#Задача № 4
with open('Stop_words', 'r', encoding='UTF-8') as forb, open("info.txt", 'r', encoding='UTF-8') as trans:
    f = forb.read().split()
    d = trans.read().split()
    for i in d:
        z, k = 0, 0
        for j in f:
            if j in i.lower():
                while i[0].lower() != j[z]:
                    z += 1
                p = i[z:len(j)]
                k = 1
        print(len(p) * '*' + i[len(p):] if k == 1 else i, end=' ')

#Задача № 5

with open("klass.txt", 'r', encoding='UTF-8') as file:
    klass=[]
    for i in file.readlines():
        line = i.rstrip("\n")
        num = int(line[-1])
        if num < 3:
            klass.append(line[:-2])
    print(f"Список отстающих учеников :{klass}")
