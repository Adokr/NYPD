import pandas as pd
import numpy as np
import pytest
from nypd import analysis

def test_max_CO2_percapita1():
    with pytest.raises(AssertionError, match="Tabela nie zawiera kolumny 'Per Capita'"):
        data = pd.DataFrame(np.array([["AAA"], ["BBB"]]), columns=["Per Ziomal"])
        analysis.max_CO2_percapita(data)
def test_max_GDP_percapita1():
    with pytest.raises(AssertionError, match="Tabela nie zawiera kolumny 'GDP_per_capita'"):
        data = pd.DataFrame(np.array([["AAA"], ["BBB"]]), columns=["GDP Per Ziomal"])
        analysis.max_GDP_percapita(data)
def test_max_change_in_CO2_emission1():
    with pytest.raises(AssertionError, match="Tabela nie zawiera kolumny 'Per Capita'"):
        data = pd.DataFrame(np.array([[100], [10]]), columns=["Per Ziomal"])
        analysis.max_change_in_CO2_emissions(data)
def test_max_change_in_CO2_emission2():
    with pytest.raises(AssertionError, match="Tabela nie zawiera kolumny 'Year'"):
        data = pd.DataFrame(np.array([[100, 2000], [10, 2020]]), columns=["Per Capita", "Jer"])
        analysis.max_change_in_CO2_emissions(data)
def test_max_change_in_CO2_emission3():
    with pytest.raises(AssertionError, match="Wybrano przedział czasowy krótszy niż 10 lat"):
        data = pd.DataFrame(np.array([[100, 2000], [10, 2008]]), columns=["Per Capita", "Year"])
        analysis.max_change_in_CO2_emissions(data)

