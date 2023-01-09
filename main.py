import argparse

parser = argparse.ArgumentParser()
parser.add_argument("GDP", help="file1 to be read")
parser.add_argument("Population", help="file2 to be read")
parser.add_argument("Emissions", help="file3 to be read")

args = parser.parse_args()

print("cośtam działa")