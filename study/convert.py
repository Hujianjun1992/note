#!/usr/bin/env python
# -*- coding: utf-8 -*-
import shlex
import string
import struct
import subprocess
# import os

L = []
X = []
Y = []
Z = []
Laser = []

def signed(n):
    if n & 0x80 == 0x80:
        return (-1)*(n & 0x7f)
    else:
        return n & 0x7f

def bytes2float(L = None):
    if L == None:
        L = []
    i_format = struct.Struct("4B")
    middle_str = i_format.pack(*L)
    f_format = struct.Struct('f')
    value = f_format.unpack(middle_str)
    return value[0]

# print signed(18)
# print signed(19)
# print signed(255)
# print signed(190)


with open('/home/hxb/catkin_ws/src/loam_back_and_forth/data/data.txt') as f:
    for line in f.readlines():
        line = line.strip()
        lineWords = shlex.split(line)
        if string.find(lineWords[0], "row_step:") != -1:
            dataNum = int(lineWords[1])
        if string.find(lineWords[0],"data:") != -1:
            lineWords[1] = lineWords[1][1:]
            i = 0
            while i < dataNum / 20:
                    X.append((int(lineWords[ 1 + i * 20 + 0][:-1])))
                    X.append((int(lineWords[ 1 + i * 20 + 1][:-1])))
                    X.append((int(lineWords[ 1 + i * 20 + 2][:-1])))
                    X.append((int(lineWords[ 1 + i * 20 + 3][:-1])))
                    Y.append((int(lineWords[ 1 + i * 20 + 4][:-1])))
                    Y.append((int(lineWords[ 1 + i * 20 + 5][:-1])))
                    Y.append((int(lineWords[ 1 + i * 20 + 6][:-1])))
                    Y.append((int(lineWords[ 1 + i * 20 + 7][:-1])))
                    Z.append((int(lineWords[ 1 + i * 20 + 8][:-1])))
                    Z.append((int(lineWords[ 1 + i * 20 + 9][:-1])))
                    Z.append((int(lineWords[ 1 + i * 20 + 10][:-1])))
                    Z.append((int(lineWords[ 1 + i * 20 + 11][:-1])))
                    x = bytes2float(X)
                    y = bytes2float(Y)
                    z = bytes2float(Z)
                    # x = struct.unpack('<f', struct.pack('4b', *X))[0]
                    # y = struct.unpack('<f', struct.pack('4b', *Y))[0]
                    # z = struct.unpack('<f', struct.pack('4b', *Z))[0]
                    # print "X:", X, "Y:", Y, "Z:",Z
                    # print "x: ", x, "y: ", y, "z: ", z
                    X = []
                    Y = []
                    Z = []
                    L.append(x)
                    L.append(y)
                    L.append(z)
                    i += 1
                    # print L

                # print x, y, z,
            # print L
            # print len(L)
            Laser.append(L)
            # print "the num of L:" + str(i) + "  len of L:"+str(len(L))
            L = []

# print len(Laser)
# print Laser[0]
# print len(Laser[1])
# print type(Laser[1])
# print len(Laser)
# print Laser[1][1]
# print len(Laser[0])
# for i in range(len(Laser)):
    # print Laser[i]
    # raw_input()

# print int(Laser[0][0])

# os.removedirs('./pcd')
# os.mkdir('./pcd/')




cnt = 0
while cnt < len(Laser):
    print "current file tag is : " , cnt
    with open('pcd/test_pcd' + str(cnt) + '.pcd','w') as f:
        f.write("# .PCD v.7 - Point Cloud Data file format\n")
        f.write("VERSION .7\n")
        f.write("FIELDS x y z rgb\n")
        f.write("SIZE 4 4 4 4\n")
        f.write("TYPE F F F F\n")
        f.write("COUNT 1 1 1 1\n")
        f.write("WIDTH %d\n" % (len(Laser[cnt]) / 3))
        f.write("HEIGHT 1\n")
        f.write("POINTS %d\n" % (len(Laser[cnt]) / 3))
        f.write("DATA ascii\n")
        num =  0
        while num < len(Laser[cnt]) / 3:
            f.write("%f " % ((Laser[cnt][num * 3 + 0])))
            f.write("%f " % ((Laser[cnt][num * 3 + 1])))
            f.write("%f " % ((Laser[cnt][num * 3 + 2])))
            f.write("%f\n" % 4.2108e+06)
            num += 1
    cnt += 1

for i in range(len(Laser)):
    subprocess.call(["pcl_viewer", "./pcd/test_pcd" + str(i) + ".pcd"])
    # raw_input()
