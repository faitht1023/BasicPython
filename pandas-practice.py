import pandas as pd
import numpy as np


#list
a = [1, 7, 2]

#creates panda series
#myvar = pd.Series(a)

#myvar = pd.Series(a, index = ["x", "y", "z"])

#print(myvar)

#print(pd.__version__)

#extract label 01 and 02
#time stamps, column 01 and column 02

#reading CSV from GitHub
url = 'https://raw.githubusercontent.com/UBCMint/Signal-Processing-Project-1/main/Data/A001SB1_1.csv?token=GHSAT0AAAAAABYEFWLP6BOUG3B627NNH5NAYY6GF5Q'
df = pd.read_csv(url,index_col=0)

print(df.head(5))