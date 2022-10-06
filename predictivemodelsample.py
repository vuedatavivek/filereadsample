import glob
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn import model_selection
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
def main():
    path = 'csvfiles'
    files = glob.glob(path+"/HR_comma_sep.csv")
    dataframe = pd.DataFrame()
    content = []
    for filename in files:
        df = pd.read_csv(filename, index_col=None)
        print(df.head(5))
        #print(df.info())
        #print(df.shape)
        #print(df.describe())
        #print(df.corr())
        #df['left'].replace(['YES', 'YES'], [1,0], inplace=True)
        #print(df.agg())
        #prin
    #print(content.index)
    #print(dataframe)
main()