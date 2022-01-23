#######Add information about number of mutatns and number of wildtypes given weight variant frequency ########

with open ("weighted_geneious.csv", "r") as w1:
    with open("weighedextra_geneious.csv", "w") as w2:
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