import pandas as pd

from custom_errors.errors import WrongFileFormat

# df = pd.read_csv("vod_csv.csv")

# print(df.head())

raise WrongFileFormat("only csv allowed")
