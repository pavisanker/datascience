import matplotlib.pyplot as plt
import pandas as pd

df =  pd.read_csv('medal.csv')
country_data = df["country"]
medal_data = df["gold_medal"]


plt.pie(medal_data, labels=country_data)
plt.title("Gold medal achievements of five most successful\n"+"countries in 2016 Summer Olympics")
plt.show() 


#medal.csv
#country,gold_medal
#United States,46
#Great Britain,27
#China,26
#Russia,19
#Germany,17

