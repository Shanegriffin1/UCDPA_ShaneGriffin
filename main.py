

git remote add origin https://github.com/Shanegriffin1/UCDPA_ShaneGriffin.git
git branch -M main
git push -u origin main

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
meat = pd.read_csv("meat_consumption_worldwide (3).csv")
beef_meat = meat[meat['SUBJECT'].str.contains('BEEF', na = False)]
jpn_beef_meat = beef_meat[beef_meat['LOCATION'].str.contains('JPN', na=False)]
jpn_beef_meatTT = jpn_beef_meat[jpn_beef_meat['MEASURE'].str.contains('THND_TONNE', na=False)]
jpn_pop = pd.read_csv("JPNpopcsv.csv")
jpn_pop.drop(jpn_pop.columns[[2, 3, 4, 5,]], axis = 1, inplace = True)
jpn_pop.drop(jpn_pop.index[12:],0,inplace=True)
jpn_stats = pd.merge(jpn_beef_meatTT, jpn_pop, left_on= 'TIME', right_on= 'Year', how= 'outer')
jpn_stats.fillna(method='ffill',axis=0, limit=5, inplace=True)
x = jpn_beef_meatTT['TIME']
y = jpn_beef_meatTT['Value']
plt.plot(x,y,color = 'red', linestyle = 'solid', marker='o', label = "Japan")
mex_beef_meat = beef_meat[beef_meat['LOCATION'].str.contains('MEX', na=False)]
mex_beef_meatTT = mex_beef_meat[mex_beef_meat['MEASURE'].str.contains('THND_TONNE', na=False)]
mex_pop = pd.read_csv("Mex_pop.csv")
mex_stats = pd.merge(mex_beef_meatTT, mex_pop, left_on= 'TIME', right_on= 'Year', how= 'outer')
mex_stats.fillna(method='ffill',axis=0, limit=5, inplace=True)
x = mex_beef_meatTT['TIME']
y = mex_beef_meatTT['Value']
plt.plot(x,y,color = 'green', linestyle = 'dashed', marker='o', label = "Japan")
plt.grid()
plt.legend(['Japanese Consumption', 'Mexican Consumption'], loc= 'best')
plt.title("Japan v Mexico Beef Consumption")
plt.xlabel("Year", color= 'blue')
plt.ylabel("Beef Consumption Per Thousand Tonne", color= 'blue')
plt.show()





















