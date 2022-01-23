with open ("GuineaAnalysis.csv", "r") as r1:
    with open ("GuineaAnalysis_ps.csv", "w") as w1:
        w1.write("Sample,Pooled,SITE,GENE,SNP,COVERAGE,VAF,VF,PooledSize\n")
        for lines in r1:
            a=lines.split(",")[0]
            test1=""
            with open("Pooled_Info_Part1.csv" , "r") as r2:
                for lines2 in r2:
                    if a in lines2:
                        if lines2[0:-3][-1].isdigit():
                            #print("\n" in lines2[0:-3][-1])
                            w1.write(lines.strip("\n")+","+lines2[0:-3][-1]+"\n")
                            test1="used"
                        if lines2[0:-4][-1].isdigit():
                            w1.write(lines.strip("\n")+","+lines2[0:-4][-1]+"\n")
                            test1="used"
            with open("Pooled_Info_Part2_fixed.csv" , "r") as r3:
                for lines3 in r3:
                    if a in lines3:
                        #print(lines3)
                        w1.write(lines.strip("\n")+","+lines3.strip("\n")[-1]+"\n")
                        test1="used"
            if test1!="used" and lines.startswith("Sample")==False:
                w1.write(lines.strip("\n")+",1\n")
                