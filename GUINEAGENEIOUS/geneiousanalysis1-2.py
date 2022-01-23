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
            if "Polymorphism" in lines and "Variants" in lines:
                samplename=lines.split(",")[0].split("_")[0]
                samplegene=lines.split(",")[1]
                sampleAAchange=lines.split(",")[16]
                #sampleVAF=(lines.split("\"")[0]).split(",")[-4]
                #print(lines.split(",")[2])
                #if sampleVAF!="":
                #    print(sampleVAF)
                #print(sampleAAchange)
                if sampleAAchange!="":
                    a=sampleAAchange.split(" ")[0]
                    b=sampleAAchange.split(" ")[2]
                    #print(len(s))
                #print(lines.split(",")[16])
                    c=lines.split(",")[19]
                    AAchangereport=(a+c+b)
                    sampleVAF=(lines.split("M05039")[0]).split(",")[-4]
                    sampleVF=(lines.split("M05039")[0]).split(",")[-2]
                    #if samplename=="19GNHa00xp003PfF1290_S85_L001_R_001":
                    #    print(lines.split("M05039")[0].split(","))
                    sampleCoverage=lines.split(",")[27]
                    #print(AAchangereport)
                    if "GN" in samplename:
                        if samplename[9]=="p":
                            #if "Do" in lines and "PfCRT" in lines and AAchangereport=="A220S":
                            #    print(samplename+","+"Pooled"+","+dict1[samplename[4:6]]+","+samplegene+","+AAchangereport)
                            #if samplename=="19GNHa00xp003PfF1290_S85_L001_R_001":
                            #    print(samplename+","+"Pooled"+","+dict1[samplename[4:6]]+","+samplegene+","+AAchangereport+","+sampleCoverage+","+sampleVAF+","+sampleVF)
                            w1.write(samplename+","+"Pooled"+","+dict1[samplename[4:6]]+","+samplegene+","+AAchangereport+","+sampleCoverage+","+sampleVAF+","+sampleVF+"\n")
                            dict2[samplename+","+"Pooled"+","+dict1[samplename[4:6]]+","+samplegene+","+AAchangereport]="exist"
                        else:
                            w1.write(samplename+","+"Individual"+","+dict1[samplename[4:6]]+","+samplegene+","+AAchangereport+","+sampleCoverage+","+sampleVAF+","+sampleVF+"\n")
                            dict2[samplename+","+"Pooled"+","+dict1[samplename[4:6]]+","+samplegene+","+AAchangereport]="exist"
                        #print(lines)
                        #print(sampleVAF)
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
                    if samplename[9]=="p":
                        if samplename+","+"Pooled"+","+dict1[samplename[4:6]]+","+samplegene+","+AAchangereport not in dict2:
                            if "Do" in lines and "PfCRT" in lines and AAchangereport=="A220S":
                                    print(samplename+","+"Pooled"+","+dict1[samplename[4:6]]+","+samplegene+","+AAchangereport=="19GNDo00xp033PfF1290,Pooled,Dorota,PfCRT,A220S")
                        #if samplename=="19GNHa00xp003PfF1290_S85_L001_R_001":
                        #    print(samplename+","+"Pooled"+","+dict1[samplename[4:6]]+","+samplegene+","+AAchangereport+","+sampleCoverage+","+sampleVAF+","+sampleVF)
                        #print("what")
                        #print(samplename+","+"Pooled"+","+dict1[samplename[4:6]]+","+samplegene+","+AAchangereport+","+sampleCoverage+","+sampleVAF+","+sampleVF+"\n")
                        #print(samplename+","+"Pooled"+","+dict1[samplename[4:6]]+","+samplegene+","+AAchangereport)
                        if samplename+","+"Pooled"+","+dict1[samplename[4:6]]+","+samplegene+","+AAchangereport not in dict2:
                            w1.write(samplename+","+"Pooled"+","+dict1[samplename[4:6]]+","+samplegene+","+AAchangereport+","+sampleCoverage+","+sampleVAF+","+sampleVF+"\n")
                    else:
                        if samplename+","+"Pooled"+","+dict1[samplename[4:6]]+","+samplegene+","+AAchangereport not in dict2:
                            w1.write(samplename+","+"Individual"+","+dict1[samplename[4:6]]+","+samplegene+","+AAchangereport+","+sampleCoverage+","+sampleVAF+","+sampleVF+"\n")
                    #print(lines)
                    #print(sampleVAF)
#print(dict2)