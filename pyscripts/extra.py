#######Add information about number of mutatns and number of wildtypes given weight variant frequency ########
import argparse
import pandas as pd
import subprocess
import csv
import itertools

parser = argparse.ArgumentParser(description='name')
parser.add_argument('-i', dest='input', type=str, help="name of voi file")
parser.add_argument('-o', dest='output', type=str, help="name of merged file")
args = parser.parse_args()


with open (args.input, "r") as w1:
    with open(args.output, "w") as w2:
        count=0
        w2.write("SITE,G_annotation,Gene, Number of Samples,WVAF,SNP,Number of Mutants, Number of wildtypes\n")
        for lines in w1:
            count+=1
            if count>1:
                print(lines)
                if float(lines.split(",")[4].strip("%\n"))==0:
                    #print(lines)
                    w2.write(lines.strip("\n")+","+lines.split(",")[1][0:-1]+",0"+","+lines.split(",")[3]+"\n")
                else:
                    #print(lines.split(",")[3])
                    #print(float(lines.split(",")[3].strip("%\n"))/100)
                    w2.write(lines.strip("\n")+","+lines.split(",")[1][1::]+","+str(round(float(lines.split(",")[3])*float(lines.split(",")[4].strip("%\n"))/100))+","+str(float(lines.split(",")[3])-round(float(lines.split(",")[3])*float(lines.split(",")[4].strip("%\n"))/100))+"\n")