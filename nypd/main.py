from nypd import data
from nypd import analysis

tmp = data.get_data(data.load_files())
df_gdp, df_pop, df_emissions = data.adjustData(tmp[0], tmp[1], tmp[2],
                                               data.getYears(tmp[0], tmp[1], tmp[2], tmp[3], tmp[4]))

lol = data.mergeData(df_gdp, df_pop, df_emissions)
print(analysis.max_CO2_percapita(lol))
print(analysis.max_GDP_percapita(lol))
co2 = analysis.max_change_in_CO2_emissions(lol)
print(co2[0])
print(co2[1])

