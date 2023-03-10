#coding=utf-8
from __future__ import division
import os

def TS(expression_list):
        expression_list = list(map(float, expression_list)) # convert str list into float list
        exp_max = max(expression_list) # max
        ts = 0
        n = int(len(expression_list))
        if exp_max != 0:
                for i in expression_list:
                        exp_i = float(i)
                        v = (1-(exp_i/exp_max))/(n-1)
                        ts += v


        return ts

for file in os.listdir("./"):
        if file.endswith(".txt"):
                inf = open(file, "r")
                ouf = open(file+".cut", "w")
                c1 = inf.readlines()
                for line in c1[1:]:
                        b = line.strip().split()
                        id = b[0]
                        expression_list = b[1:]
                        ts = TS(expression_list)
                        ouf.write("%s\t%s\n" % (id, str(ts)))
