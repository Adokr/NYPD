from nypd import files

df_gdp, df_pop, df_emissions = files.get_data(files.load_files())

df_gdp = df_gdp.drop(['Indicator Name', 'Indicator Code', 'Unnamed: 66', 'Country Code'], axis=1)

df_pop = df_pop.drop(['Indicator Name', 'Indicator Code', "Unnamed: 66", 'Country Code'], axis=1)

df_emissions = df_emissions.drop(['Solid Fuel', 'Liquid Fuel', 'Gas Fuel', 'Cement', 'Gas Flaring', 'Bunker fuels (Not in Total)'], axis=1)

df_emissions_total = df_emissions.drop('Per Capita', axis=1)
df_emissions_total = df_emissions_total.pivot(index="Country", columns="Year", values="Total").reset_index()#.rename_axis("Year", axis=1)

df_emissions_percapita = df_emissions.drop('Total', axis=1)
df_emissions_percapita = df_emissions_percapita.pivot(index="Country", columns="Year", values="Per Capita").reset_index()
#print(df_gdp.values[:,0] == df_pop.values[:,0])
#print(df_emissions_percapita.values[:,0] == df_emissions_total.values[:,0])
print(df_gdp.values[:,0])
print(df_emissions_percapita.values[:,0])
dic_country = df_emissions_percapita.values[:,0]
#print(dic_country)
#print(df_gdp.values[:,0] == df_pop.values[:,0])


