#! /usr/bin/python3

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
plt.rcParams['savefig.format'] = 'jpg'

data = np.array(pd.read_csv("time_series_covid19_confirmed_global.csv"))


fecha = np.array(pd.read_csv("time_series_covid19_confirmed_global.csv", 
													header = None))[0, 4:]
fecha7 = np.append(fecha, ['4/10/20', '4/11/20','4/12/20',
							'4/13/20','4/14/20','4/15/20','4/16/20'])
USAdata = data[225,4:]
USAlog = np.array([np.log10(x) for x in USAdata])
date = np.arange(USAdata.shape[0])
date7 = np.arange(date.size + 7)

p = np.polyfit(date, USAlog, 1)

abline = p[0]*date7 + p[1]

print(10**abline[-1])

interval = np.array([True if i > 31 else False for i in date])
print(fecha[32])

fig, ax = plt.subplots(figsize=(18,12))
ax.plot(fecha, USAlog, 'ko-')
ax.plot(fecha7, abline, 'r-', label = "Linear Best Fit")
ax.set_ylabel("$\log_{10}(C)$", size =20)
ax.set_xlabel("Date", size = 20)
ax.fill_between(date, np.zeros(date.size), USAlog,
				where= interval, color ='blue')
ax.tick_params(length=6, width=2, labelsize=20)
ax.set_ylim(0,)
temp = ax.xaxis.get_ticklabels()
temp = list(set(temp) - set(temp[::21]))
for label in temp:
	label.set_visible(False)
ax.set_title("Confirmed COVID-19 cases $(C)$ in the USA", size = 20)
ax.legend(loc=('best'))
fig.savefig("Log10CasesVsDate")

