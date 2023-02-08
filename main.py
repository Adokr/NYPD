import argparse
import numpy as np
import pandas as pd

parser = argparse.ArgumentParser()
parser.add_argument("GDP", help="file1 to be read")
parser.add_argument("Population", help="file2 to be read")
parser.add_argument("Emissions", help="file3 to be read")

args = parser.parse_args()

df_gdp = pd.read_csv(args.GDP, sep=',', header=[2])
df_gdp.drop(['Indicator Name', 'Indicator Code', 'Unnamed: 66'], axis=1, inplace=True)

df_pop = pd.read_csv(args.Population, sep = ',', header=[2])
df_pop.drop(['Indicator Name', 'Indicator Code', "Unnamed: 66"], axis=1, inplace=True)

df_emissions = pd.read_csv(args.Emissions, sep = ',')
df_emissions.drop(['Solid Fuel', 'Liquid Fuel', 'Gas Fuel', 'Cement', 'Gas Flaring', 'Bunker fuels (Not in Total)'], axis=1, inplace=True)

df_emissions_total = df_emissions.drop('Per Capita', axis=1)
df_emissions_total.pivot(index="Country", columns="Year", values="Total").reset_index().rename_axis("Year", axis=1, inplace=True)

df_emissions_percapita = df_emissions.drop('Total', axis=1)
df_emissions_percapita.pivot(index="Country", columns="Year", values="Per Capita").reset_index().rename_axis("Year", axis=1, inplace=True)

print(df_emissions_total.values)
