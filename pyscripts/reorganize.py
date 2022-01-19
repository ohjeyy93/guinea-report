import argparse
import pandas as pd
import subprocess
import csv
import itertools

parser = argparse.ArgumentParser(description='name')
parser.add_argument('-s', dest='stacked', type=str, help="name of voi file")
parser.add_argument('-r', dest='organized', type=str, help="name of merged file")
args = parser.parse_args()

with open(args.stacked, 'r') as infile, open(args.organized, 'w') as outfile:
    # output dict needs a list for new column ordering
    fieldnames = ['Pool', 'Poolsize', 'AMD_ID', 'YEAR','SITE', "Treatment Day", 'G_annotation', 'VAF','Gene', 'Type', 'SNP']
    #Pool    SITE    YEAR    AMD_ID  Poolsize    G_annotation    VAF Gene    Type    SNP
    writer = csv.DictWriter(outfile, fieldnames=fieldnames)
    # reorder the header first
    writer.writeheader()
    for row in csv.DictReader(infile):
        # writes the reordered rows to the new file
        writer.writerow(row)