import pandas as pd
import csv

df = pd.read_csv('merged_star_data.csv')

df.drop(['Unnamed: 0','Star_name.1', 'Distance.1', 'solar_mass', 'solar_radius','Luminosity'],axis=1,inplace=True)
print(df.columns)

final_data = df.dropna()

df.to_csv('cleaned_data.csv', index = False)