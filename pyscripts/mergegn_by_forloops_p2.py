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
with open ("mergedfile_forloops_p2.csv", "w") as w1:
    #w1.write("CSID,AMD_ID,Sample_ID,Year,Study_site,Treatment_arm,SNP,VAF")
    with open (args.merged, "r") as r1:
        count=0
        list1=[]
        for line in r1:
            count+=1
            countw=0
            tempword1=""
            tempvaf=""
            if count==1:
                w1.write("Poolsize,SITE,YEAR,AMD_ID,Poolsize,Treatment Day,G_annotation,VAF"+"\n")
            for word in line.split(","):
                #######If the row is first and the column is not first then add SNP information to the list#######
                if count==1:
                    if word!="Row Labels":
                        #print(word)
                        list1+=[word]
                        #print(word)
                    #print(list1)
                #######If the row is not the first row then start writing merged rows#######
                if count>1:
                    countw+=1
                    ######If it is first column assign the AMD ID#########
                    if countw==1:
                        ##### if it is first column add the AMD ID of the sample ######
                        tempword1=word
                        #print(tempword1)
                        #print(tempword1)
                        #print(tempword1)
                        #print(word)
                    else:
                        #print
                        ##### if it is not the first column add variant frequency 
                        #print(word)
                        tempvaf=word
                        #print(word)
                        #print(word)
                    #print(list1)
                    ########If it the second column start assigning variant freqeuncy to the row from the pooled data ######
                    if countw>1:
                        #print(tempword1,tempvaf)
                        with open (args.paired, "r") as r2:
                            #######go over the paired info. Go over each rows#####
                            for line2 in r2:
                                #print(line2)
                            #print(line.split(",")[0])
                                #print(line2)
                                #####If AMD ID is found then assgin VAF and SNP to the row#########
                                if tempword1 in line2:
                                    #print(line2)
                                    #if countw<len(list1)+1:
                                        #if countw==len(list1):
                                            #print(line2.strip("\n")+","+list1[countw-1]+","+tempvaf.strip("\n")+"\n")
                                            #print(tempvaf.strip("\n"))
                                            #print(list1[countw-1])
                                        #print(line2.split(",")[1][6:8])
                                    ############When column is looped maximally to the full length of the row 
                                    ############then strip line changer at the end of SNP##########
                                    if countw==len(list1)+1:
                                        #print(tempword1)
                                        #print(countw)
                                        #print(list1[countw-2].strip("\n"))
                                        #print(tempvaf.strip("\n")+"\n")
                                        #print(line2)
                                        if line2.split(",")[3][6:8]!="1A":
                                            #print(list1[countw-1].strip("\n"))
                                            w1.write(line2.strip("\n")+","+line2.split(",")[3][6:8]+","+list1[countw-2].strip("\n")+","+tempvaf.strip("\n")+"\n")
                                        else:
                                            w1.write(line2.strip("\n")+","+"1"+","+list1[countw-2].strip("\n")+","+tempvaf.strip("\n")+"\n")
                                    #print(line2.strip("\n")+","+tempvaf+","+list1[countw-1])
                                    ############When nth column which n is shorther than length of row then 
                                    ############asssign VAF and SNP
                                    ########## Need to add 1 to the len(list1) because countw starts from 1 while len list1 starts from 0#####
                                    ######### Need to subtract 2 for assigning SNP because list1[0] is Row label########
                                    if countw<len(list1)+1: 
                                        #print(tempvaf)
                                        #if countw==11:
                                        #print(tempword1)
                                        #print(countw)
                                        #print(list1[countw-2].strip("\n"))
                                        #print(tempvaf.strip("\n")+"\n")
                                        if line2.split(",")[3][6:8]!="1A":
                                            w1.write(line2.strip("\n")+","+line2.split(",")[3][6:8]+","+list1[countw-2]+","+tempvaf.strip("\n")+"\n")
                                        else:
                                            w1.write(line2.strip("\n")+","+"1"+","+list1[countw-2]+","+tempvaf.strip("\n")+"\n")
    #print(list1)#for line2 in r2:
                    #if "CSID,AMD_ID,Sample_ID" not in line:
                        #print(line)
                        #if line.split(",")[0] in line2:
                            #print(line[1])
                            #print(line[2])
                        #    print(line)
                        #   print(line2+","+line.split(",")[1]+","+line.split(",")[2])
    #print(list1)
#print(("0.539").is())
with open ("mergedfile_forloops_p2.csv", "r") as w2:
    with open ("Gp1_pooled_merge_final_fl_p2.csv", "w") as w3:        
        for line in w2:
            #print(line)
            #print(line.split(",")[-2])
            #print(line.split(",")[-1])
            #print(line)
            #print(line)
            #if "18GNLa00xp030PfF1153" in line:
            #    print(line.split(",")[-1].strip("\n")=="0")
            if line.split(",")[-2]=="G_annotation":
                w3.write(line.strip("\n")+",Gene"+",Type"+",SNP\n")
            else:
                if line.split(",")[-2] in dict1:
                    #print(line.strip("\n").split(",")[6])
                    #print(line.strip("\n").strip(line.strip("\n").split(",")[6])+str(round(float(line.split(",")[-1])*100,1))+"%")
                    #print(line.split(",")[-1].strip("\n"))
                    #print(line.split(",")[-1].strip("\n").isdigit())
                    #print(line.split(",")[-1].strip("\n").strip("\n"))
                    #print(line.split(",")[-1].strip("\n").strip("\n"))
                    #print("%" in line.split(",")[-1].strip("\n").strip("\n")==True)
                    #print(line.split(",")[-1].strip("\n").strip("\n"))
                    #print(line)
                    #print(line.split(",")[-1].strip("\n").strip("\n"))
                    #print(line.strip("\n").strip(line.strip("\n").split(",")[5]))
                    #print(line)
                    #print(line)
                    #print(line.strip("\n").split(",")[7])
                    #print(line.strip("\n").strip(line.strip("\n").split(",")[7]))
                    #print(line[0:-len(line.strip("\n").split(",")[7])-1])
                    if "N" not in line.split(",")[-1].strip("\n").strip("\n") and line.split(",")[-1].strip("\n")=="0":
                        #print("True")
                        #print(line.split(",")[-1].strip("\n").strip("\n"))
                        #print(line.split(",")[-2])
                        #print(str(round(float(line.split(",")[-1])*100))+"%")
                        w3.write(line[0:-len(line.strip("\n").split(",")[7])-1]+str(round(float(line.split(",")[-1])*100))+"%"+","+dict1[line.split(",")[-2]]+","+"wildtype,"+line.split(",")[-2][0:-1]+"\n")
                    if "N" not in line.split(",")[-1].strip("\n").strip("\n") and line.split(",")[-1].strip("\n")!="0":
                        #print(float(line.split(",")[-1]))
                        #print(str(round(float(line.split(",")[-1])*100))+"%")
                        #print(line.strip("\n").strip(line.strip("\n").split(",")[6]))
                        #print(line.strip("\n").split(",")[7])
                        #print(line.strip("\n").strip(line.strip("\n").split(",")[7]))
                        w3.write(line[0:-len(line.strip("\n").split(",")[7])-1]+str(round(float(line.split(",")[-1])*100))+"%"+","+dict1[line.split(",")[-2]]+","+"mutation,"+line.split(",")[-2][1::]+"\n")
                    if "N" in line.split(",")[-1].strip("\n").strip("\n"):
                        #print("false")
                        w3.write(line.strip("\n")+","+dict1[line.split(",")[-2]]+","+"NA,"+"NA"+"\n")
                        
                else:
                    #print(line)
                    for key in dict1:
                        if line.split(",")[-2][0:-1] in key:
                            if "N" not in line.split(",")[-1].strip("\n") and line.split(",")[-1].strip("\n")=="0":
                                #print(str(round(float(line.split(",")[-1])*100))+"%")
                                w3.write(line[0:-len(line.strip("\n").split(",")[7])-1]+str(round(float(line.split(",")[-1])*100))+"%"+","+dict1[key]+","+"wildtype,"+line.split(",")[-2][0:-1]+"\n")
                            if "N" not in line.split(",")[-1].strip("\n") and line.split(",")[-1].strip("\n")!="0":
                                #print(str(round(float(line.split(",")[-1])*100))+"%")
                                w3.write(line[0:-len(line.strip("\n").split(",")[7])-1]+str(round(float(line.split(",")[-1])*100))+"%"+","+dict1[key]+","+"mutation,"+line.split(",")[-2][1::]+"\n")
                            if "N" in line.split(",")[-1].strip("\n") == False:
                                w3.write(line.strip("\n")+","+dict1[key]+","+"NA"+",NA"+"\n")
#        print(line)    
       #with open ("Paired_Info.xlsx", "r") as r2:
        #for line in 
        #    for line in xlsx: 
        #        for line2 in xlsx[line]:
        #            w1.write()