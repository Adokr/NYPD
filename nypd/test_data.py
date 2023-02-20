import numpy as np
import pandas as pd
import pytest
from nypd import data

@pytest.mark.parametrize("minYear, maxYear", [("2000", "1999"), ("1960", "1959")])
def test_get_years1(minYear, maxYear):
    with pytest.raises(AssertionError, match="Podano nieprawidłowy przedział lat"):
        data.getYears(None, None, None, minYear, maxYear)

@pytest.mark.parametrize("minYear, maxYear", [("2000", "aa"), ("aaa", "1959")])
def test_get_years2(minYear, maxYear):
    with pytest.raises(AssertionError, match="Lata muszą być liczbami"):
        data.getYears(None, None, None, minYear, maxYear)

def test_adjust_data1():
    with pytest.raises(AssertionError, match="Tabela GDP nie zawiera kolumny 'Country Name'"):
        gdp = pd.DataFrame(np.array([["AAA"], ["AAA"]]), columns=["Kałntry Nejm"])
        data.adjustData(gdp, None, None, [])
def test_adjust_data2():
    with pytest.raises(AssertionError, match="Tabela Population nie zawiera kolumny 'Country Name'"):
        gdp = pd.DataFrame(np.array([["AAA"], ["AAA"]]), columns=["Country Name"])
        pop = pd.DataFrame(np.array([["AAA"], ["AAA"]]), columns=["Kałntry Nejm"])
        data.adjustData(gdp, pop, None, [])
def test_adjust_data3():
    with pytest.raises(AssertionError, match="Brak pełnych danych dla podanych lat"):
        gdp = pd.DataFrame(np.array([["AAA"], ["AAA"]]), columns=["Country Name"])
        pop = pd.DataFrame(np.array([["AAA"], ["AAA"]]), columns=["Country Name"])
        data.adjustData(gdp, pop, None, [])
def test_merge_data1():
    with pytest.raises(AssertionError, match="Tabela GDP nie zawiera kolumny 'Country'"):
        gdp = pd.DataFrame(np.array([["AAA"], ["AAA"]]), columns = ["Kałntry"])
        data.mergeData(gdp, None, None)
def test_merge_data2():
    with pytest.raises(AssertionError, match="Tabela Population nie zawiera kolumny 'Country'"):
        gdp = pd.DataFrame(np.array([["AAA"], ["AAA"]]), columns = ["Country"])
        pop = pd.DataFrame(np.array([["AAA"], ["AAA"]]), columns=["Kałntry"])
        data.mergeData(gdp, pop, None)
def test_merge_data3():
    with pytest.raises(AssertionError, match="Tabela Emissions nie zawiera kolumny 'Country'"):
        gdp = pd.DataFrame(np.array([["AAA"], ["AAA"]]), columns = ["Country"])
        pop = pd.DataFrame(np.array([["AAA"], ["AAA"]]), columns=["Country"])
        emissions = pd.DataFrame(np.array([["AAA"], ["AAA"]]), columns=["Kałntry"])
        data.mergeData(gdp, pop, emissions)
