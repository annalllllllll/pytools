import struct
import os
import re


if __name__ == "__main__":
    filename = 'aes_anw'
    filepath = './'

    file =    open(filepath + filename + '.txt', 'r')
    fileNew = open(filepath + filename + '__.txt', 'w')

    lines = file.readlines()
    for line in lines:
        s = re.split("\t", line)
        print(s)
        for i in s:
            if len(i) > 4 or len(i) < 2:
                continue
            a = i[2:] + i[:2]
            print(a)
            fileNew.write(a+'\n')

    file.close()
    fileNew.close()
