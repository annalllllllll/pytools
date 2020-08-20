import struct
import os
import binascii
import pickle

if __name__ == "__main__":
    filename = 'addr0x180000' 
    filepath = './'

    file =    open(filepath + filename + '.txt', 'r')
    fileNew = open(filepath + filename + '.bin', 'wb')

    size = os.path.getsize(filepath)
    print(size)
    lines = file.readlines()
    for line in lines:
        curLine = line.split(' ')
        for i in range(len(curLine)):
            if (len(curLine[i]) == 0) or (curLine[i] == '\n'):
                continue
            data = int(curLine[i], 16)
            s = struct.pack('B', data)
            fileNew.write(s)
    file.close()
    fileNew.close()
