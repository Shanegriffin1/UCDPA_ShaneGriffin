import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
jpn_pop = pd.read_csv("JPNpopcsv.csv")
jpn_pop.drop(jpn_pop.columns[[2, 3, 4, 5,]], axis = 1, inplace = True)
jpn_pop.drop(jpn_pop.index[12:],0,inplace=True)
jpn_pop['Year'] = jpn_pop['Year'].astype('int')
meat = pd.read_csv("meat_consumption_worldwide (3).csv")
beef_meat = meat[meat['SUBJECT'].str.contains('BEEF', na = False)]
jpn_beef_meat = beef_meat[beef_meat['LOCATION'].str.contains('JPN', na=False)]
jpn_beef_meatTT = jpn_beef_meat[jpn_beef_meat['MEASURE'].str.contains('THND_TONNE', na=False)]
jpn_stats = pd.merge(jpn_beef_meatTT, jpn_pop, left_on= 'TIME', right_on= 'Year', how= 'outer')
jpn_stats.fillna('ffill', inplace=False)
jpn_stats.fillna(method='ffill',axis=0, limit=5, inplace=True)
jpn_stats.mask(jpn_stats=='NaN', None).ffill()
jpn_stats.ffill(axis=0)
fig, axes = plt.subplots(2)
sns.lineplot(ax=axes[0], x=jpn_pop['Year'], y=jpn_pop['TotalPopulation'])
axes[0].set_title("Japanese Total Population 1990 - 2026 - 2021 - 2026 estimated", loc = 'left')
plt.grid()
plt.legend(["Population"], loc = "upper right")
sns.lineplot(ax=axes[1], x=jpn_beef_meatTT['TIME'], y=jpn_beef_meatTT['Value'])
axes[1].set_title("Japanese Beef Consumption 1990 - 2026 - 2021 - 2026 estimated", loc = 'right')
plt.xticks(fontsize=3)
plt.grid()
plt.legend(["Consumption Trend"], loc = "lower right")
plt.show()








