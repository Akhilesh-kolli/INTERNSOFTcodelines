# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

a = pd.read_csv('NVDA Historical Data.csv',usecols=[1,2,3])

POHL_avg = a[['Price','Open','High']].mean(axis=1)

b = np.arange(1,len(a)+1,1)

plt.plot(b,POHL_avg,'b',label = 'NVDA')