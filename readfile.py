from dataclasses import fields
import glob
from operator import countOf
import pandas as pd
import csv

def filedata(filename):
    columns = []
    rows = []
    with open(filename, 'r') as csvfile:
        csvreader = csv.reader(csvfile)
        columns = next(csvreader)
        for row in csvreader:
            rows.append(row)
        print("Total no of rows: %d"%(csvreader.line_num))
        print("Total no of columns: %d"%(len(columns)))

path = 'csvfiles'

files = glob.glob(path+"/*.csv")

dataframe = pd.DataFrame()
content = []

for filename in files:
    print(filename)
    filedata(filename)
    df = pd.read_csv(filename, index_col=None)
    content.append(df)
dataframe = pd.concat(content)
print(content.index)
#print(dataframe)
