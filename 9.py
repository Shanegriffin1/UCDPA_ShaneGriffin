import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
mex_pop = pd.read_csv("Mex_pop.csv")
mex_pop.sort_values(by= 'Population', ascending = True, inplace= True)
#print(mex_pop)
meat = pd.read_csv("meat_consumption_worldwide (3).csv")
beef_meat = meat[meat['SUBJECT'].str.contains('BEEF', na = False)]
mex_beef_meat = beef_meat[beef_meat['LOCATION'].str.contains('MEX', na=False)]
mex_beef_meatTT = mex_beef_meat[mex_beef_meat['MEASURE'].str.contains('THND_TONNE', na=False)]
mex_stats = pd.merge(mex_beef_meatTT, mex_pop, left_on= 'TIME', right_on= 'Year', how= 'outer')
mex_stats.fillna(method='ffill',axis=0, limit=5, inplace=True)
mex_stats.sort_values(by= 'Population')
print(mex_stats)
fig, axes = plt.subplots(2)
sns.lineplot(ax=axes[0], x=mex_beef_meatTT['TIME'], y=mex_beef_meatTT['Value'])
axes[0].set_title("Mexican Beef Consumption 1990-2026 - 2020-2026 estimated", loc = 'left')
plt.grid()
plt.legend(["Consumption"], loc = "upper right")
sns.lineplot(ax=axes[1], x=mex_stats['TIME'], y=mex_stats['Population'])
axes[1].set_title("Mexican Population Growth 1990-2026 - 2020-2026 estimated", loc = 'right')
plt.xticks(fontsize=3)
plt.grid()
plt.legend(["Population Trend"], loc = "lower right")
plt.show()


