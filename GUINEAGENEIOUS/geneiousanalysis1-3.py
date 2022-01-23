###Open raw output table file "Annotations.csv" from Geneious#####

count220=0
dict3={}
with open ("Annotations.csv", "r") as r1:
    with open("GuineaAnalysis.csv" , "w") as w1:
        w1.write("Sample,Pooled,SITE,GENE,SNP,COVERAGE,VAF,VF\n")
        count=0
        dict1={}
        dict1["Ha"]="Hamdalaye"
        dict1["Do"]="Dorota"
        dict1["Ma"]="Maferinyah"
        dict1["La"]="Lay-Sarè"
        dict1["LS"]="Lay-Sarè"
        dict2={}
        for lines in r1:
            
            count+=1
            
            ######Check if there is Polymorphism in the line from the table#######
            ######If there is polymorphism then that means there is variant######
            ######According to Geneious as geneious report variants as polymorphisms####
            
            if "Polymorphism" in lines and "Variants" in lines:
                ####sample name is first column right before the _ string#####
                samplename=lines.split(",")[0].split("_")[0]
                ####Sample gene is the second coulmmn in the line####
                samplegene=lines.split(",")[1]
                ###Sample AA change is column 17 which has the amino acid changes####
                sampleAAchange=lines.split(",")[16]
                #sampleVAF=(lines.split("\"")[0]).split(",")[-4]
                #print(lines.split(",")[2])
                #if sampleVAF!="":
                #    print(sampleVAF)
                #print(sampleAAchange)
                ####If there is Amino acid change reported combine it with the c variable which is codon position####
                ####to create a SNP change report #####
                if sampleAAchange!="":
                    a=sampleAAchange.split(" ")[0]
                    b=sampleAAchange.split(" ")[2]
                    #print(len(s))
                #print(lines.split(",")[16])
                    c=lines.split(",")[19]
                    AAchangereport=(a+c+b)
                    #print(AAchangereport)
                    sampleVAF=(lines.split("M05039")[0]).split(",")[-4]
                    sampleVF=(lines.split("M05039")[0]).split(",")[-2]
                    #if samplename=="19GNHa00xp003PfF1290_S85_L001_R_001":
                    #    print(lines.split("M05039")[0].split(","))
                    sampleCoverage=lines.split(",")[27]
                    #print(AAchangereport)
                    if "GN" in samplename:
                        #if "A220S" in lines:
                        #    print(samplename)
                        #if AAchangereport=="A220S" and "Do" in lines:
                            #print(samplename,AAchangereport)
                        #    if "PfCRT" in lines:
                        #        count220+=1
                        #    if "PfCRT" in lines:
                                ###check in item is already in dictionary###
                                #samplename,AAchangereport
                                #if (samplename,AAchangereport) in dict3:
                                #print(samplename,AAchangereport)
                        #dict3[samplename,AAchangereport]="exist"
                        ####Use a dictionary to prevent overlaps######
                        if samplename[9]=="p" and (samplename,AAchangereport) not in dict3:
                            dict3[samplename,AAchangereport]="exist"
                            #if "Do" in lines and "PfCRT" in lines and AAchangereport=="A220S":
                            #    print(samplename+","+"Pooled"+","+dict1[samplename[4:6]]+","+samplegene+","+AAchangereport)
                            #if samplename=="19GNHa00xp003PfF1290_S85_L001_R_001":
                            #    print(samplename+","+"Pooled"+","+dict1[samplename[4:6]]+","+samplegene+","+AAchangereport+","+sampleCoverage+","+sampleVAF+","+sampleVF)
                            w1.write(samplename+","+"Pooled"+","+dict1[samplename[4:6]]+","+samplegene+","+AAchangereport+","+sampleCoverage+","+sampleVAF+","+sampleVF+"\n")
                            dict2[samplename+","+"Pooled"+","+dict1[samplename[4:6]]+","+samplegene+","+AAchangereport]="exist"
                        if samplename[9]!="p" and (samplename,AAchangereport) not in dict3:
                            w1.write(samplename+","+"Individual"+","+dict1[samplename[4:6]]+","+samplegene+","+AAchangereport+","+sampleCoverage+","+sampleVAF+","+sampleVF+"\n")
                            dict2[samplename+","+"Individual"+","+dict1[samplename[4:6]]+","+samplegene+","+AAchangereport]="exist"
                        #print(lines)
                        #print(sampleVAF)
with open ("Annotations.csv", "r") as r1:
    with open("GuineaAnalysis.csv" , "a") as w1:
        for lines in r1:
            if "Coverage" in lines:
                #print(lines)
                samplename=lines.split(",")[0].split("_")[0]
                samplegene=lines.split(",")[1]
                AAchangereport=lines.split(",")[-1].strip("\n")
                sampleVAF="0%"
                sampleVF="0"
                #if samplename=="19GNHa00xp003PfF1290_S85_L001_R_001":
                #    print(lines.split("M05039")[0].split(","))
                sampleCoverage=lines.split(",")[-3]
                #print(AAchangereport)
                if "GN" in samplename:
                    if samplename[9]=="p" and (samplename,AAchangereport) not in dict3:
                         dict3[samplename,AAchangereport]="exist"
                        #if "Do" in lines and "A220S" in lines:
                        #    print(lines)
                        if samplename+","+"Pooled"+","+dict1[samplename[4:6]]+","+samplegene+","+AAchangereport not in dict2:
                            w1.write(samplename+","+"Pooled"+","+dict1[samplename[4:6]]+","+samplegene+","+AAchangereport+","+sampleCoverage+","+sampleVAF+","+sampleVF+"\n")
                    if samplename[9]!="p" and (samplename,AAchangereport) not in dict3::
                        if samplename+","+"Pooled"+","+dict1[samplename[4:6]]+","+samplegene+","+AAchangereport not in dict2:
                            w1.write(samplename+","+"Individual"+","+dict1[samplename[4:6]]+","+samplegene+","+AAchangereport+","+sampleCoverage+","+sampleVAF+","+sampleVF+"\n")
                    #print(lines)
                        #print(sampleVAF)
#print(dict2)
print(count220)
print(len(dict3))
print(dict3)