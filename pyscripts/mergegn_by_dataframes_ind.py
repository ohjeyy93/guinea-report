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
#######Import reportable variants##########
#######The purpose of importing csv document with reportable variable is to assign genes to SNPs later########
with open (args.voi, "r") as v1:
    dict1={}
    for line in v1:
        dict1[line.split(",")[2]+line.split(",")[3]+line.split(",")[4].strip("\n")]=line.split(",")[1]

####Create a dataframe of an paired merge file#####
####Use the column names to create list of SNPs####
df = pd.read_csv(args.merged)
listofSNPs1=[]
for col in df.columns:
    ###Ignore the row label####
    ####Fill nan with NAs#####
    df[col]=df[col].fillna("NA")
    if col!="AMD ID":
        listofSNPs1+=[col]
####Create a mergefile to write####       
#df.fillna("NA") 
#print(df)
with open ("mergedfile_df.csv", "w") as w1:
    ####Wrtie the first row of the mergefile#####
    w1.write("CSID,AMD_ID,Sample_ID,YEAR,SITE,Treatment_arm,Treatment Day,G_annotation,VAF"+"\n")
####Iterate over dataframe rows####
    for index, row in df.iterrows():
        #####Print the AMD ID of each row####
        AMDID=row["AMD ID"]
        with open (args.paired, "r") as r1:
            for line in r1:
                if AMDID in line:
                    #print(line+)
                    for item in listofSNPs1:
                        if line.split(",")[1][6:8]!="1A":
                            #print(line.split(",")[1][6:8])
                            w1.write(line.strip("\n")+","+line.split(",")[1][6:8]+","+item+","+str(row[item])+"\n")
                        else:
                            w1.write(line.strip("\n")+",1"+","+item+","+str(row[item])+"\n")

with open ("mergedfile_df.csv", "r") as w2:
    with open ("gp1_paired_merge_df.csv", "w") as w3:        
        for line in w2:
            #print(line.split(",")[-2])
            #print(line.split(",")[-1])
            #print(line.split(",")[-2])
            #########If column is G_annotation add three extra Column for Gene,Type,SNP#######

            if line.split(",")[-2]=="G_annotation":
                w3.write(line.strip("\n")+",Gene"+",Type,SNP"+"\n")
            #print(line.split(",")[-2])
            else:
                #######If row is not the name of columns with actual data start assgining Gene, Type, and SNP#####
                #######If mutation is reportable add according to dictionary#########
                if line.split(",")[-2] in dict1:
                    #print(line.split(",")[-1].strip("\n"))
                    #print(line.split(",")[-1].strip("\n").isdigit())
                    #print(line.split(",")[-1].strip("\n").strip("\n"))
                    #print(line.split(",")[-1].strip("\n").strip("\n"))
                    #print("%" in line.split(",")[-1].strip("\n").strip("\n")==True)
                    #print(line.split(",")[-1].strip("\n").strip("\n"))
                    #print(line)
                    if "%" in line.split(",")[-1].strip("\n").strip("\n") and line.split(",")[-1].strip("\n")=="0%":
                        #print("True")
                        w3.write(line.strip("\n")+","+dict1[line.split(",")[-2]]+","+"wildtype,"+line.split(",")[-2][0:-1]+"\n")
                    if "%" in line.split(",")[-1].strip("\n").strip("\n") and line.split(",")[-1].strip("\n")!="0%":
                        w3.write(line.strip("\n")+","+dict1[line.split(",")[-2]]+","+"mutation,"+line.split(",")[-2][1::]+"\n")
                    if "%" not in line.split(",")[-1].strip("\n").strip("\n"):
                        #print("false")
                        w3.write(line.strip("\n")+","+dict1[line.split(",")[-2]]+","+"NA,NA"+"\n")
                        
                else:
                    #######If mutation is not reportable add according to dictionary of reportable genes#########
                    for key in dict1:
                        if line.split(",")[-2][0:-1] in key:
                            if "%" in line.split(",")[-1].strip("\n") and line.split(",")[-1].strip("\n")=="0%":
                                w3.write(line.strip("\n")+","+dict1[key]+","+"wildtype,"+line.split(",")[-2][0:-1]+"\n")
                            if "%" in line.split(",")[-1].strip("\n") and line.split(",")[-1].strip("\n")!="0%":
                                w3.write(line.strip("\n")+","+dict1[key]+","+"mutation,"+line.split(",")[-2][1::]+"\n")
                            if "%" not in line.split(",")[-1].strip("\n") == False:
                                w3.write(line.strip("\n")+","+dict1[key]+","+"NA,NA"+"\n")
#        print(line)    
       #with open ("Paired_Info.xlsx", "r") as r2:
        #for line in 
        #    for line in xlsx: 
        #        for line2 in xlsx[line]:
        #            w1.write()