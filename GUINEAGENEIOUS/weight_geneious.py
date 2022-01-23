#########Extract individual information about variant frequency of individuals###########
#########Extract pooled information about variant frequency of pooled samples###########
with open ("GuineaAnalysis_ps.csv", "r") as r2:
    count=0
    dict1={}
    for lines in r2:
        count+=1
        if count>1:
            #if "Do" in lines and "A220S" in lines:
            #    print(lines)
            #print(lines)
            #print(lines.split(",")[8])
            #print(lines.split(",")[7])
            #print(lines.split(",")[1])
            ########### Combine individual variant frequency with the pooled variant frequencies##########
            #print(lines.split(",")[2])
            #print(lines.split(",")[2]+","+lines.split(",")[4]+","+lines.split(",")[3])
            #print(lines.split(",")[2]+","+lines.split(",")[4]+","+lines.split(",")[3].strip("\n").strip(" "))
            if lines.split(",")[2]+","+lines.split(",")[4]+","+lines.split(",")[3].strip("\n").strip(" ") in dict1:
                #print([lines.split(",")[1],float(lines.split(",")[7].strip("%"))*float(lines.split(",")[1])])
                #print(dict1[lines.split(",")[4]+","+lines.split(",")[6]])
                #print(dict1[lines.split(",")[4].strip(" ")+","+lines.split(",")[6]])
                #print(dict1[lines.split(",")[4].strip(" ")+","+lines.split(",")[6]])
                #if "C59R" == lines.split(",")[6]:
                #    print(lines.split(",")[7])
                #    print([float(lines.split(",")[1]),float(lines.split(",")[7].strip("%"))*float(lines.split(",")[1])])
                #print(lines.split(",")[8])
                #print(lines.split(",")[6].split(" ")[0])
                dict1[lines.split(",")[2]+","+lines.split(",")[4]+","+lines.split(",")[3].strip("\n")]=[x + y for x, y in zip(dict1[lines.split(",")[2]+","+lines.split(",")[4]+","+lines.split(",")[3].strip("\n")],[float(lines.split(",")[8].strip("\n")),float(lines.split(",")[6].split(" ")[0].strip("%"))*float(lines.split(",")[8].strip("\n"))])]
            if lines.split(",")[2]+","+lines.split(",")[4]+","+lines.split(",")[3].strip("\n").strip(" ") not in dict1:
                #print([float(lines.split(",")[1]),float(lines.split(",")[7].strip("%"))*float(lines.split(",")[1])])
                #print([float(lines.split(",")[1]),float(lines.split(",")[7].strip("%"))*float(lines.split(",")[1])])
                #print(lines.split(",")[4].strip(" ")+","+lines.split(",")[6]+","+lines.split(",")[8])
                dict1[lines.split(",")[2]+","+lines.split(",")[4]+","+lines.split(",")[3].strip("\n")]=[float(lines.split(",")[8].strip("\n")),float(lines.split(",")[6].strip("%"))*float(lines.split(",")[8].strip("\n"))]
                #print
#print(dict1)

########Create a csv file with information about weighted average############
with open ("weighted_geneious.csv", "w") as w1:
    w1.write("Site,SNP,Gene,Number of Samples,WVAF\n")
    for item in dict1:
        #print(dict1[item][0],dict1[item][1])
        #print(dict1[item])
        w1.write(item+","+str(dict1[item][0])+","+str(round((dict1[item][1]/dict1[item][0]),1))+"%"+"\n")