#######Import reportable variants##########
#######The purpose of importing csv document with reportable variable is to assign genes to SNPs later########

with open ("voinew3.csv", "r") as v1:
    dict1={}
    for line in v1:
        dict1[line.split(",")[2]+line.split(",")[3]+line.split(",")[4].strip("\n")]=line.split(",")[1]
#print(dict1)
##########First open the file that is going to be written with merged results##########
with open ("mergedfile.csv", "w") as w1:
    #w1.write("CSID,AMD_ID,Sample_ID,Year,Study_site,Treatment_arm,SNP,VAF")
    with open ("gp1_paired_merge.csv", "r") as r1:
        count=0
        list1=[]
        #####First go over the paired merge file which has SNP and variation frequency information########
        for line in r1:
            #print(line)
            count+=1
            countw=0
            tempword1=""
            tempvaf=""
            if count==1:
                #####Write the first line of the new merged file to create the column names of each column###########
                w1.write("CSID,AMD_ID,Sample_ID,YEAR,SITE,Treatment_arm,Treatment Day,G_annotation,VAF"+"\n")
            ######Go over each word in the line which is going over each variant freqeuncy corresponding to different SNP#####
            for word in line.split(","):
                #print(word)
                #######If the row is first and the column is not first then add SNP information to the list#######
                if count==1:
                    if word!="AMD ID":
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
                        with open ("Paired_Info.csv", "r") as r2:
                            #######go over the paired info. Go over each rows#####
                            for line2 in r2:
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
                                        if line2.split(",")[1][6:8]!="1A":
                                            #print(list1[countw-1].strip("\n"))
                                            w1.write(line2.strip("\n")+","+line2.split(",")[1][6:8]+","+list1[countw-2].strip("\n")+","+tempvaf.strip("\n")+"\n")
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
                                        if line2.split(",")[1][6:8]!="1A":
                                            w1.write(line2.strip("\n")+","+line2.split(",")[1][6:8]+","+list1[countw-2]+","+tempvaf.strip("\n")+"\n")
                                        else:
                                            w1.write(line2.strip("\n")+","+"1"+","+list1[countw-2]+","+tempvaf.strip("\n")+"\n")
                #for line2 in r2:
                    #if "CSID,AMD_ID,Sample_ID" not in line:
                        #print(line)
                        #if line.split(",")[0] in line2:
                            #print(line[1])
                            #print(line[2])
                        #    print(line)
                        #   print(line2+","+line.split(",")[1]+","+line.split(",")[2])
    #print(list1)
########Using created merge file with Paired row assigned with SNP and VAF######
########Assign mutation type and gene ######
with open ("mergedfile.csv", "r") as w2:
    with open ("gp1_paired_merge_true.csv", "w") as w3:        
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