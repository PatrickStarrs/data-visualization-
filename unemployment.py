import csv as c
import numpy as np
import matplotlib.pyplot as plt 

filename = 'data_2.csv'

with open (filename) as f:
    reader = c.reader(f)
    ump_r = []
    for row_readin in reader:
        #print(row_readin[0])
        ID_number = int(row_readin[0])
        checker = ID_number/1000
        if isinstance(checker,int) == 0:
            if row_readin[9] == "":
                print("?")
            else:
                ump_r.append(float(row_readin[9]))
plt.hist(ump_r, bins=100)