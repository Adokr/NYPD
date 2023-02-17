from nypd import files
from nypd import data
import numpy as np

tmp = files.get_data(files.load_files())
df_gdp, df_pop, df_emissions = data.adjustData(tmp[0], tmp[1], tmp[2], data.getYears(tmp[0], tmp[1], tmp[2], 1950, 2014))


df_emissions_total = df_emissions.drop('Per Capita', axis=1)
df_emissions_total = df_emissions_total.pivot(index="Country", columns="Year", values="Total").reset_index()#.rename_axis("Year", axis=1)

df_emissions_percapita = df_emissions.drop('Total', axis=1)
df_emissions_percapita = df_emissions_percapita.pivot(index="Country", columns="Year", values="Per Capita").reset_index()

#print(df_emissions)
#print(data.getYears(df_gdp, df_pop, df_emissions, 1960, 2014))
#print(df_emissions_percapita.values[:,0])
dic_country = df_emissions_percapita.values[:,0]
lol = data.mergeData(df_gdp, df_pop, df_emissions)
print(lol)
#print(dic_country)
#print(df_gdp.values[:,0] == df_pop.values[:,0])


