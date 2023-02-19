from nypd import data
from nypd import analysis

tmp = data.get_data(data.load_files())
df_gdp, df_pop, df_emissions = data.adjustData(tmp[0], tmp[1], tmp[2], data.getYears(tmp[0], tmp[1], tmp[2], 1980, 2005))

lol = data.mergeData(df_gdp, df_pop, df_emissions)
#print(lol[["Year","Country", "Total"]])
print(analysis.max_CO2_percapita(lol))
print(analysis.max_GDP_percapita(lol))

print(analysis.max_change_in_CO2_emissions(lol)[0])
print(analysis.max_change_in_CO2_emissions(lol)[1])

#lol.groupby(["Country"]).size().sort_values())
#print(analysis.max_GDP_percapita(lol))



