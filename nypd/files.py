import argparse
import pandas as pd

def load_files():
    parser = argparse.ArgumentParser()
    parser.add_argument("GDP", help="gdp file to be read")
    parser.add_argument("Population", help="population file to be read")
    parser.add_argument("Emissions", help="emissions file to be read")
    return parser.parse_args()

def get_data(args):
    return pd.read_csv(args.GDP, sep=',', header=[2]),  pd.read_csv(args.Population, sep = ',', header=[2]), \
            pd.read_csv(args.Emissions, sep = ',')