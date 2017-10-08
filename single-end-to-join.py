#This script transform single-end bed files to joined.bed format for cntr.py program
import sys
from sys import argv

f = open (argv[1], "r")
name = argv[1]
out = open (name+".joined", "w")
for line in f:
    sline=line.strip().split()
    #print sline[5]
    if sline[5] == "+":
        out.write(sline[0]+"\t"+sline[3]+"\t"+sline[5]+"\t"+"-"+"\t"+sline[1]+"\t"+sline[2]+"\n")
    else:
        out.write(sline[0]+"\t"+sline[3]+"\t"+sline[5]+"\t"+"+"+"\t"+sline[1]+"\t"+sline[2]+"\n")
f.close()
out.close()

