import numpy as np
import pandas as pd

def max_CO2_percapita(data):
    assert "Per Capita" in data.columns, "Tabela nie zawiera kolumny 'Per Capita'"
    data =  data.groupby(["Year"]).apply(lambda x: x.nlargest(5, "Per Capita"))[["Country", "Per Capita", "Total"]]
    data.index = data.index.droplevel(1)
    return data

def max_GDP_percapita(data):
    assert "GDP_per_capita" in data.columns, "Tabela nie zawiera kolumny 'GDP_per_capita'"
    data = data.groupby(["Year"]).apply(lambda x: x.nlargest(5, "GDP_per_capita"))[["Country", "GDP_per_capita", "GDP"]]
    data.index = data.index.droplevel(1)
    return data

def max_change_in_CO2_emissions(data):
    assert "Per Capita" in data.columns, "Tabela nie zawiera kolumny 'Per Capita'"
    maxYear = max(data["Year"])
    data = data.query(f"Year == {maxYear} or Year == {maxYear-9}")
    data = data.pivot(index="Country", columns="Year")
    data = data.rename_axis(("Stat", "Year"), axis=1)
    data["CO2_change_percapita"] = data[("Per Capita", maxYear)] - data[("Per Capita", maxYear-9)]
    data.columns = data.columns.droplevel(1)
    data = data.rename_axis((None), axis=1)
    return data.nlargest(5, "CO2_change_percapita")[["CO2_change_percapita"]], data.nsmallest(5, "CO2_change_percapita")[["CO2_change_percapita"]]
