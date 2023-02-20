import argparse
import numpy as np
import pandas as pd
from nypd.dict import get_dict

def load_files():
    parser = argparse.ArgumentParser()
    parser.add_argument("GDP", help="gdp file to be read")
    parser.add_argument("Population", help="population file to be read")
    parser.add_argument("Emissions", help="emissions file to be read")
    parser.add_argument("Min", help="first year")
    parser.add_argument("Max", help="last year")
    return parser.parse_args()

def get_data(args):
    return pd.read_csv(args.GDP, sep=',', header=[2]),  pd.read_csv(args.Population, sep = ',', header=[2]), \
            pd.read_csv(args.Emissions, sep = ','), args.Min, args.Max

def adjustData(df_gdp, df_pop, df_emissions, years):
    assert 'Country Name' in df_gdp.columns, "Tabela GDP nie zawiera kolumny 'Country Name'"
    assert 'Country Name' in df_pop.columns, "Tabela Population nie zawiera kolumny 'Country Name'"
    assert len(years) != 0, "Brak pełnych danych dla podanych lat"
    df_gdp = df_gdp.rename(columns={'Country Name': 'Country'})
    df_pop = df_pop.rename(columns={'Country Name': 'Country'})
    df_gdp = pd.DataFrame(df_gdp[["Country"] + years])
    df_pop = pd.DataFrame(df_pop[["Country"] + years])
    df_emissions = pd.DataFrame(df_emissions[df_emissions.Year.astype(str).isin(years)])
    return df_gdp, df_pop, df_emissions
def getYears(gdp, pop, emissions, minYear, maxYear):
    assert isinstance(minYear, int) and isinstance(maxYear, int), "Lata muszą być liczbami"
    assert minYear < maxYear, "Podano nieprawidłowy przedział lat"
    years = []
    years_gdp = gdp.columns[4:-1].astype("int64")
    years_pop = pop.columns[4:-1].astype("int64")
    years_emissions = list(np.unique(emissions.Year))
    minRange = max(min(years_gdp), min(years_pop), min(years_emissions), int(minYear))
    maxRange = min(max(years_gdp), max(years_pop), max(years_emissions), int(maxYear))

    for i in range(minRange, maxRange + 1):
        if (i in years_gdp and i in years_pop and i in years_emissions):
            years.append(str(i))
    return years

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
    data["GDP_per_capita"] = data["GDP"] / data["Population"]

    return data
