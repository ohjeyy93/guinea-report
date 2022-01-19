import argparse
import pandas as pd
import subprocess
import csv
import itertools

parser = argparse.ArgumentParser(description='name')
parser.add_argument('-v', dest='voi', type=str, help="name of voi file")
parser.add_argument('-g', dest='merged', type=str, help="name of merged file")
parser.add_argument('-p', dest='paired', type=str, help="name of paired info file")
args = parser.parse_args()

with open (args.voi, "r") as v1:
    dict1={}
    for line in v1:
        dict1[line.split(",")[2]+line.split(",")[3]+line.split(",")[4].strip("\n")]=line.split(",")[1]

#print(dict1)

df = pd.read_csv(args.merged)
listofSNPs1=[]
for col in df.columns:
    ###Ignore the row label####
    ####Fill nan with NAs#####
    df[col]=df[col].fillna("NA")
    if col!="AMD ID":
        listofSNPs1+=[col]

with open ("mergedfile_df_p1.csv", "w") as w1:
    w1.write("Poolsize,SITE,YEAR,AMD_ID,Poolsize,Treatment Day,G_annotation,VAF"+"\n")
    #w1.write("CSID,AMD_ID,Sample_ID,Year,Study_site,Treatment_arm,SNP,VAF")
    for index, row in df.iterrows():
        #####Print the AMD ID of each row####
        AMDID=row["AMD ID"]
        with open (args.paired, "r") as r1:
            for line in r1:
                if AMDID in line:
                    #print(line+)
                    for item in listofSNPs1:
                        if line.split(",")[3][6:8]!="1A":
                            #print(line)
                            #print(line.split(",")[1][6:8])
                            w1.write(line.strip("\n")[0:-3]+","+line.split(",")[3][6:8]+","+item+","+str(row[item])+"\n")
                        else:
                            w1.write(line.strip("\n")[0:-3]+",1"+","+item+","+str(row[item])+"\n")
                #for line2 in r2:
                    #if "CSID,AMD_ID,Sample_ID" not in 

with open ("mergedfile_df_p1.csv", "r") as w2:
    with open ("GP2_merge_final_df_p1.csv", "w") as w3:        
        for line in w2:
            #print(line.split(",")[-2])
            #print(line.split(",")[-1])
            #print(line)
            if line.split(",")[-2]=="G_annotation":
                w3.write(line.strip("\n")+",Gene"+",Type"+",SNP\n")
            else:
                if line.split(",")[-2] in dict1:
                    #print(line.split(",")[-1].strip("\n"))
                    #print(line.split(",")[-1].strip("\n").isdigit())
                    #print(line.split(",")[-1].strip("\n").strip("\n"))
                    #print(line.split(",")[-1].strip("\n").strip("\n"))
                    #print("%" in line.split(",")[-1].strip("\n").strip("\n")==True)
                    #print(line.split(",")[-1].strip("\n").strip("\n"))
                    #print(line)
                    #print(line.split(",")[-1].strip("\n").strip("\n"))
                    if "N" not in line.split(",")[-1].strip("\n").strip("\n") and line.split(",")[-1].strip("\n")=="0%":
                        #print("True")
                        #print(line.split(",")[-1].strip("\n").strip("\n"))
                        #print(line.split(",")[-2])
                        w3.write(line.strip("\n")+","+dict1[line.split(",")[-2]]+","+"wildtype,"+line.split(",")[-2][0:-1]+"\n")
                    if "N" not in line.split(",")[-1].strip("\n").strip("\n") and line.split(",")[-1].strip("\n")!="0%":
                        w3.write(line.strip("\n")+","+dict1[line.split(",")[-2]]+","+"mutation,"+line.split(",")[-2][1::]+"\n")
                    if "N" in line.split(",")[-1].strip("\n").strip("\n"):
                        #print("false")
                        w3.write(line.strip("\n")+","+dict1[line.split(",")[-2]]+","+"NA,"+"NA"+"\n")
                        
                else:
                    for key in dict1:
                        if line.split(",")[-2][0:-1] in key:
                            if "N" not in line.split(",")[-1].strip("\n") and line.split(",")[-1].strip("\n")=="0%":
                                w3.write(line.strip("\n")+","+dict1[key]+","+"wildtype,"+line.split(",")[-2][0:-1]+"\n")
                            if "N" not in line.split(",")[-1].strip("\n") and line.split(",")[-1].strip("\n")!="0%":
                                w3.write(line.strip("\n")+","+dict1[key]+","+"mutation,"+line.split(",")[-2][1::]+"\n")
                            if "N" in line.split(",")[-1].strip("\n") == False:
                                w3.write(line.strip("\n")+","+dict1[key]+","+"NA"+",NA"+"\n")
#        print(line)    
       #with open ("Paired_Info.xlsx", "r") as r2:
        #for line in 
        #    for line in xlsx: 
        #        for line2 in xlsx[line]:
        #            w1.write()