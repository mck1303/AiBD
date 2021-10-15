import pandas as pd
import numpy as np

df=pd.read_csv('C:\\Users\Emperor\Desktop\Lab1\OriginalData\drinks.csv')

Beer=df[['country','beer_servings']]
Wine=df[['country','wine_servings']]
Spirit=df[['country','spirit_servings']]
Total=df[['country','total_litres_of_pure_alcohol']]

Beer['type']='beer'
Wine['type']='wine'
Spirit['type']='spirit'
Total['type']='pure alcohol'

Beer.columns=('Country','Litres','Type')
Wine.columns=('Country','Litres','Type')
Spirit.columns=('Country','Litres','Type')
Total.columns=('Country','Litres','Type')

Beer=Beer[['Country','Type','Litres']]
Spirit=Spirit[['Country','Type','Litres']]
Wine=Wine[['Country','Type','Litres']]
Total=Total[['Country','Type','Litres']]

New=pd.concat([Beer,Spirit,Wine,Total])
New=New.sort_values(['Country','Type'])

New=New.reset_index()
New=New[['Country','Type','Litres']]
New.to_csv(path_or_buf='C:\\Users\\Emperor\\Desktop\\Lab1\\AnalysisData\\fixed_drinks.csv', index=False) 