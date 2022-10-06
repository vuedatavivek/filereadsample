from dataclasses import fields
import glob
import json
from operator import countOf
import pandas as pd
import csv
def createdatamodel(row, columns):
    newobj = {}
    for field in columns:
        newobj[field]= row[columns.index(field)]
    return newobj

def filedata(filename):
    dataset = []
    columns = []
    rows = []
    with open(filename, 'r') as csvfile:
        csvreader = csv.reader(csvfile)
        columns = next(csvreader)
        for row in csvreader:
            rows.append(row)
            dataobj = createdatamodel(row, columns)
            dataset.append(dataobj)

        print("Total no of rows: %d"%(csvreader.line_num))
        print("Total no of columns: %d"%(len(columns)))
        # json_obj = json.dumps(dataset)
        # with open('dictionary.json', 'w') as outfile:
        #     outfile.write(json_obj)

def main():
    path = 'csvfiles'
    files = glob.glob(path+"/*.csv")
    dataframe = pd.DataFrame()
    content = []
    for filename in files:
        print(filename)
        filedata(filename)
        df = pd.read_csv(filename, index_col=None)
        df.shape
        content.append(df)
    dataframe = pd.concat(content)

    #print(content.index)
    #print(dataframe)
main()
