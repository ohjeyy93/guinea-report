import argparse
import pandas as pd
import subprocess
import csv
import itertools

parser = argparse.ArgumentParser(description='name')
parser.add_argument('-g1', dest='merged1', type=str, help="name of voi file")
parser.add_argument('-g2', dest='merged2', type=str, help="name of merged file")
parser.add_argument('-o', dest='output', type=str, help="name of paired info file")
args = parser.parse_args()

with open (args.merged1, "r") as r1:
    with open (args.merged2, "r") as r2:
        with open (args.output, "w") as w1:
            w1.write("Pool,SITE,YEAR,AMD_ID,Poolsize,Treatment Day,G_annotation,VAF,Gene,Type,SNP\n")
            count=0
            for lines in r2:
                count+=1
                if count>1:
                    w1.write(lines)
            count=0
            for lines in r1:
                count+=1
                if count>1:
                    w1.write(lines)
    