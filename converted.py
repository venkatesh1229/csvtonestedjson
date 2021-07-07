import json
import pandas as pd

# Function to arrage data to nested manager
def fdrec(df):
    drec = dict()
    ncols = df.values.shape[1] # Shape of columns 10
    for line in df.values: # loop each row in datafile
        d = drec
        for j, col in enumerate(line[:-1]): # Add countble to each ithm in the row like (0, "value1"), (1, "value2")
            if not col in d.keys(): # Check the values exits in dict or not
                if j != ncols-2: # existing item came and align the nested form 
                    d[col] = {}
                    d = d[col] 
                else:
                    d[col] = line[-1]
            else:
                if j!= ncols-2: # new item came to first time it adds to d
                    d = d[col]
    return drec

df = pd.DataFrame(pd.read_csv("data.csv", sep = ",",index_col = False))
dd = fdrec(df)
with open("data.json", 'w') as outfile:
    json.dump(dd, outfile)
