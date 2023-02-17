import numpy as np
import pandas as pd
from nypd.dict import get_dict

def adjustData(df_gdp, df_pop, df_emissions, years):
    assert len(years) != 0
    df_gdp = df_gdp.rename(columns={'Country Name': 'Country'})
    df_pop = df_pop.rename(columns={'Country Name': 'Country'})
    #df_emissions = df_emissions.drop(['Solid Fuel', 'Liquid Fuel', 'Gas Fuel',
                                      #'Cement', 'Gas Flaring', 'Bunker fuels (Not in Total)'], axis=1)
    df_gdp = pd.DataFrame(df_gdp[["Country"] + years])
    df_pop = pd.DataFrame(df_pop[["Country"] + years])
    df_emissions = pd.DataFrame(df_emissions[df_emissions.Year.astype(str).isin(years)])
    return df_gdp, df_pop, df_emissions
def getYears(gdp, pop, emissions, minYear, maxYear):
    years = []
    years_gdp = gdp.columns[4:-1].astype("int64")
    years_pop = pop.columns[4:-1].astype("int64")
    years_emissions = list(np.unique(emissions.Year))
    minRange = max(min(years_gdp), min(years_pop), min(years_emissions), minYear)
    maxRange = min(max(years_gdp), max(years_pop), max(years_emissions), maxYear)

    for i in range(minRange, maxRange + 1):
        if (i in years_gdp and i in years_pop and i in years_emissions):
            years.append(str(i))
    return years

def cleanData():
    return False

def mergeData(gdp, pop, emissions):
    assert 'Country' in gdp.columns, "Tabela GDP nie zawiera kolumny 'Country'"
    assert 'Country' in pop.columns, "Tabela Population nie zawiera kolumny 'Country'"
    assert 'Country' in emissions.columns, "Tabela Emissions nie zawiera kolumny 'Country'"
    countries = get_dict()
    gdp = gdp.melt(id_vars=["Country"], var_name="Year", value_name="GDP")
    pop = pop.melt(id_vars=["Country"], var_name="Year", value_name="Population")
    data = pd.merge(gdp, pop, on=("Country", "Year"))
    data["Country"] = data["Country"].str.upper()
    for index, row in data.iterrows():
        if row["Country"] in countries:
            data.at[index, "Country"] = countries[row["Country"]]
    for index, row in emissions.iterrows():
        if row["Country"] in countries:
            emissions.at[index, "Country"] = countries[row["Country"]]
    tab1 = np.setdiff1d(np.unique(data["Country"]), np.unique(emissions["Country"]))
    tab2 = np.setdiff1d(np.unique(emissions["Country"]), np.unique(data["Country"]))
    print(f"Kraje, które nie występują w tabeli Emissions: {tab1}")
    print(f"Kraje, które nie wystęoują w tabeli GDP/Population: {tab2}")
    data = data.astype({"Year": "int64"})
    data = pd.merge(data, emissions, on=("Country", "Year"))
    return data
