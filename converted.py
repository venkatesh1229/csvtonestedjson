import json
import pandas as pd


def fdrec(df):
    drec = dict()
    ncols = df.values.shape[1]
    for line in df.values:
        d = drec
        for j, col in enumerate(line[:-1]):
            if not col in d.keys():
                if j != ncols-2:
                    d[col] = {}
                    d = d[col]
                else:
                    d[col] = line[-1]
            else:
                if j!= ncols-2:
                    d = d[col]
    return drec

df = pd.DataFrame(pd.read_csv("data.csv", sep = ",",index_col = False))
dd = fdrec(df)
with open("data.json", 'w') as outfile:
    json.dump(dd, outfile)
