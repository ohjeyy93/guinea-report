#########Extract individual information about variant frequency of individuals###########

with open ("gp1_paired_merge_df.csv", "r") as r1:
    dict1={}
    count=0
    for lines in r1:
        count+=1
        if count>1:
            #print(lines.split(",")[9])
            if lines.split(",")[4]+","+lines.split(",")[7]+","+lines.split(",")[9] in dict1 and "N" not in lines.split(",")[8]:
                dict1[lines.split(",")[4].strip(" ")+","+lines.split(",")[7]+","+lines.split(",")[9]]=[x + y for x, y in zip(dict1[lines.split(",")[4]+","+lines.split(",")[7]+","+lines.split(",")[9]],[1,float(lines.split(",")[8].strip("%"))])]
            if lines.split(",")[4]+","+lines.split(",")[7]+","+lines.split(",")[9] not in dict1 and "N" not in lines.split(",")[8]:
                dict1[lines.split(",")[4].strip(" ")+","+lines.split(",")[7]+","+lines.split(",")[9]]=[1,float(lines.split(",")[8].strip("%"))]
#print(dict1)
#########Extract pooled information about variant frequency of pooled samples###########
with open ("pooled_seq_results_df_re1.csv", "r") as r2:
    count=0
    for lines in r2:
        count+=1
        if count>1:
            #print(lines)
            #print(lines.split(",")[8])
            #print(lines.split(",")[7])
            #print(lines.split(",")[1])
            ########### Combine individual variant frequency with the pooled variant frequencies##########
            if lines.split(",")[4]+","+lines.split(",")[6]+","+lines.split(",")[8] in dict1 and "N" not in lines.split(",")[7]:
                #print([lines.split(",")[1],float(lines.split(",")[7].strip("%"))*float(lines.split(",")[1])])
                #print(dict1[lines.split(",")[4]+","+lines.split(",")[6]])
                #print(dict1[lines.split(",")[4].strip(" ")+","+lines.split(",")[6]])
                #print(dict1[lines.split(",")[4].strip(" ")+","+lines.split(",")[6]])
                #if "C59R" == lines.split(",")[6]:
                #    print(lines.split(",")[7])
                #    print([float(lines.split(",")[1]),float(lines.split(",")[7].strip("%"))*float(lines.split(",")[1])])
                print(lines)
                dict1[lines.split(",")[4].strip(" ")+","+lines.split(",")[6]+","+lines.split(",")[8]]=[x + y for x, y in zip(dict1[lines.split(",")[4]+","+lines.split(",")[6]+","+lines.split(",")[8]],[float(lines.split(",")[1]),float(lines.split(",")[7].strip("%"))*float(lines.split(",")[1])])]
            if lines.split(",")[4]+","+lines.split(",")[6]+","+lines.split(",")[8] not in dict1 and "N" not in lines.split(",")[7]:
                #print([float(lines.split(",")[1]),float(lines.split(",")[7].strip("%"))*float(lines.split(",")[1])])
                #print([float(lines.split(",")[1]),float(lines.split(",")[7].strip("%"))*float(lines.split(",")[1])])
                #print(lines.split(",")[4].strip(" ")+","+lines.split(",")[6]+","+lines.split(",")[8])
                dict1[lines.split(",")[4].strip(" ")+","+lines.split(",")[6]+","+lines.split(",")[8]]=[float(lines.split(",")[1]),float(lines.split(",")[7].strip("%"))*float(lines.split(",")[1])]
                #print
#print(dict1)

########Create a csv file with information about weighted average############
with open ("weighted_df.csv", "w") as w1:
    w1.write("Site,SNP,Gene,Number of Samples,WVAF\n")
    for item in dict1:
        #print(dict1[item][0],dict1[item][1])
        #print(dict1[item])
        w1.write(item+","+str(dict1[item][0])+","+str(round((dict1[item][1]/dict1[item][0]),1))+"%"+"\n")