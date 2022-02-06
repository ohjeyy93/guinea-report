{\rtf1\ansi\ansicpg1252\cocoartf1671\cocoasubrtf600
{\fonttbl\f0\fswiss\fcharset0 Helvetica;\f1\fnil\fcharset0 LucidaGrande;}
{\colortbl;\red255\green255\blue255;}
{\*\expandedcolortbl;;}
\margl1440\margr1440\vieww33100\viewh17680\viewkind0
\pard\tx720\tx1440\tx2160\tx2880\tx3600\tx4320\tx5040\tx5760\tx6480\tx7200\tx7920\tx8640\pardirnatural\partightenfactor0

\f0\fs24 \cf0 \'dfMalaria has been a major illness in Africa. The drug resistance of malaria is making it more difficult to treat the patients with Malaria. To overcome the drug resistance CDC is developing a surveillance protocol for tracking drug ressitance of malarial genes. As part of the protocol and basic step we analyze Plasmodium Falciparum genes gained for patients. This ReadME is for other users to understand the work I've done which analyzes genes and reports findings. \
\
## ReadMe for Geneious workflow and scripts for reports for lab and EPI\
#### \'a01. Geneious Workflow\
    Geneious Workflow contains mainly four steps for processing raw sequences to variants and coverage. You select a samples then go to workflows and run the SNP_Coverage_Analysis.geneiousWorkflow. Then, it automatically runs all the below steps from a -> d. \
    \
###### a. Trimming (Discard unnecessary reads that would cause noise to the data)\
    Geneious uses BBduk for trimming raw sequences. The settings are\
    1. Trim Adapters: All Truseq, Nextera and PhilX adapters \
    
\f1 \uc0\u10003 
\f0  Trim Right End\
    
\f1 \uc0\u10003 
\f0  Kmer Length 27 \
    
\f1 \uc0\u10003 
\f0  Maximum Substitutions 1 \
    
\f1 \uc0\u10003 
\f0  Maximum Substitutions + INDELs: 0,\
    2. Trim Low quality: \
    
\f1 \uc0\u10003 
\f0 Both Ends \
    
\f1 \uc0\u10003 
\f0 Minimum Quality 35\
    3. Trim Adapters based on paired read overhangs: Minimum Overlap: 24\
    4. Discard Short Reads: Minimum Length: 150 bp\
\
###### b. Map to Reference (To observe differences in genetic structure from reference)\
    The workflow uses Map to reference for algining reads to the reference\
    1. Dissolve contigs and re-assemble: reference sequecne is updated_MaRS_refs_ET (6sequences), \
    Assemble each sequence list separately\
    2. Mapper: \
    
\f1 \uc0\u10003 
\f0  Bowtie2 \
    
\f1 \uc0\u10003 
\f0  alginment Type: End to End \
    
\f1 \uc0\u10003 
\f0  Use Preset: High Sensitivity/Medium\
    3. Do not trim (discrad trim annotations)\
    4. Save contigs\
    \
###### c. Find Variations/SNPs (To find the unique genetic structure from the samples)\
    1. Find Variants: Minimum Variant Frequency: 0.05\
    2. Analtze effect of variants on translations : Default Genetic Code, Standard\
    3. Advanced: Use separate annotations for each variant at a position\
     
\f1 \uc0\u10003 
\f0  Record names of all contributing sequences of each variant\
     
\f1 \uc0\u10003 
\f0  Only find variations in annotation types = TrackerSNP\
     
\f1 \uc0\u10003 
\f0  Also find varations within 0bases of those types\
     
\f1 \uc0\u10003 
\f0  CDS properties to Copy: gene, product, protein_id, locus, tag, note.\
    \
###### d. Find coverage (To see if there are WildTypes we are interested )\
    1. Only Find in: Annotations in reference sequence of type: TrackerSNP, Create coverage annotations on reference sequence\
    2. High Coverage: Find regions with coverage above, number of sequences: 0\
    \
###### e. Selecting workflow outputs (contigs )\
    1. After the workflow is done contig documents will be generated in the same folder with AMD_ID and gene information\
    2. To select the contigs you click on modified \
    * If you can't see modified header scroll to the right \
    3. Then select the files that are generated later with AMD_ID and gene information in the document title\
    \
###### f. Export findings to a csv raw output (To process more data )\
    1. Select all the documents with coverage and variant information\
    * Select in as mentioned in step e\
    2. Select all the columns\
    3. Select all the types\
    4. Export table \
    * Export as Annotations.csv\
\
\
#### 2. Python scripts for Geneious raw input\
###### a. Read Annotations.csv file and process\
    1. Python script has with open function to open file and read each lines from the file\
    2. Each jupyter note script will process Geneious raw output for different purposes.\
\
###### b. File1: Individual_geneious_EP/LAB (Individual and Pooled)\
    1 This jupyter note file is for processing individual file\
    2. This file produces the file with these headers: \
    * Sample,Pooled,Year,SITE,TreatmentDay,GENE,G_annotation,COVERAGE,VAF,VF,SNP,TYPE\
    3. The information in the header are obtained from running this jupyter file\
    4. The raw Geneious output will be transformed to .csv file with above header information\
    5. EP/LAB means there are two vesions of this code. EP stands for epidemiology team which has reportable mutatns while LAB version has other mutations.\
    \
###### c. File2: Pooled_geneious_EP/LAB (Pooled)\
    1 This jupyter note file is for processing Pooled file\
    2. This file produces the file with these headers: \
    * Sample,Pooled,Year,SITE,TreatmentDay,GENE,G_annotation,COVERAGE,VAF,VF,SNP,TYPE\
    3. The information in the header are obtained from running this jupyter file\
    4. The raw Geneious output will be transformed to .csv file with above header information\
    5. EP/LAB means there are two vesions of this code. EP stands for epidemiology team which has reportable mutatns while LAB version has other mutations.\
\
###### d. File3: geneiousanalysis1_combined1.ipynb (Individual and Pooled)\
    1. This jupyter note file is for processing combined pooled and individual files\
    2. The purpose of processing both pooled and individual file is for later producing\
    weighted average variant frequency file with total number of samples in the file.\
    3. This file produces the file with these headers: \
    * Sample,Pooled,Year,SITE,TreatmentDay,GENE,G_annotation,COVERAGE,VAF,VF,SNP,TYPE\
    4. The information in the header are obtained from the jupyter file\
    \
###### e. File4: Pooled_geneious_EP/LAB.ipynb\
    1. This jupyter note file is for processing adding pooled group and pooled size to previously produced pooled file from file 2. \
    *Simply adding two more columns to already exisintg columns\
    \
###### f. File5: geneiousanalysis2_pooled/EP.ipynb\
    1. This jupyter note file is for processing adding pooled group and pooled size to previously produced pooled file from file 3 which contains both individual and pooled information. \
    *Simply adding two more columns to already exisintg columns\
    \
    \
###### g. File6: weight_geneious_LAB/EP_fixed1.ipynb\
    1. Last step of producing weighted vaf and total sample files\
    *The header of final output is "Site,G_annotation,Gene,Number of Samples,SNP,WVAF,Number of Mutants, Number of wildtypes"\
    \
    \
For more specific description look into individual jupyter notebook scripts. It contains doc string to explain overall script and line by line comment for specific details.\
\
\
    \
    \
  \
\
\
}