import struct
import os
import re


def s16(value):
    return  -(value & 0x8000) | (value & 0x7fff)


if __name__ == "__main__":
    filename = 'tmp'
    filepath = './'

    file = open(filepath + filename + '.txt', 'r')
    fileNew = open(filepath + filename + '__.txt', 'w')

    lines = file.readlines()
    for line in lines:
        s = re.split("\t", line)
        # s = re.split(",", line)
        # print(s)
        for i in s:
            # print(i)

            # plan 1
            # if i == ' \n' or i == '\n':
            #     continue
            # j = re.split("\t", i)
            # for k in j:
            #     if k == '' or k == '\n':
            #         continue
            #     m = int(k, 10)                         # 字符串 -> 数
            #     # print(m)
            #     n = hex(m & 0xFFFF)                    # 有符号十进制数据 -> 无符号short整型
            #     n = str(n)                             # 十六进制数 -> 字符串 （会有0x格式）
            #     # print(n)
            #     qww = n.replace('0x', '')              # 输出去除十六进制转化时产生的0x
            #     print(qww)
            #     fileNew.write(qww.zfill(4) + '\n')     # 字符串前补零凑4位

            # plan 2
            qww = i.replace('\n', '')
            if len(qww) > 4:
                continue
            a = qww[2:] + qww[:2]                        # 高低位拼接 例： 1234 -> 3412
            b = str(s16(int(a, 16)))
            print(b)
            fileNew.write(b+'\n')

    file.close()
    fileNew.close()
