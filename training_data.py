#!/usr/bin/python

import argparse
from argparse import RawTextHelpFormatter
import datetime
import struct
import random
from time import sleep
import sys

def getUniqueFileID():
    now = datetime.datetime.now()
    return int(now.strftime("%d%H%M%S"))

parser = argparse.ArgumentParser(formatter_class=RawTextHelpFormatter)
parser.add_argument("rows", type=int,help="Number of points")
parser.add_argument("cols", type=int,help="Number of dimensions")
parser.add_argument("dist", type=int,help="""Type of distribution\n0: Uniform Distribution\n1: Centered Uniform
        Distribution\n2: Beta distribution\n3: Exponential distribution""",choices=[0, 1, 2,3])
args = parser.parse_args()

fileid = getUniqueFileID()
datafilename = "data_" + str(fileid) + ".dat"
#datafilename = "data_" + str(fileid) + ".txt" 

fp = open(datafilename,"wb")
#fp = open(datafilename,"w")

cols = args.cols
rows = args.rows
dist = args.dist

# generate file header for datafile
fp.write("TRAINING\n")
fp.write(struct.pack("=q",getUniqueFileID()))
fp.write(struct.pack("=q",args.rows))
fp.write(struct.pack("=q",args.cols))
#fid = str(getUniqueFileID())
#r = str(args.rows)
#c = str(args.cols)
#fp.write(fid + "\n")
#fp.write(r + "\n")
#fp.write(c + "\n")

funcList = [random.uniform,random.gauss,random.betavariate,random.expovariate]
paramList = [(-1000,1000),(0,1000),(30,20),(0.01,)]

part = int(rows/100)
# Now generating data for data file 
if(part!=0):
    print("Data file generation progress:")
for i in range(0,rows):
    #progress bar
    if(part!=0 and i%part==0):
        sys.stdout.write('\r')
        sys.stdout.write("[%-100s] %d%%" % ('='*(i/part), (i/part)))
        sys.stdout.flush()
    buff = str()
    for j in range(0,cols):
        buff+=struct.pack("=f",funcList[dist](*paramList[dist]))
        #p = str(funcList[dist](*paramList[dist]))
        #buff+=p + "\n"
    fp.write(buff)
fp.close()

if(part!=0):
    print("\n")
print("\nData file : " + datafilename);
