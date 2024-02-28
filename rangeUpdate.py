import pandas as pd
import numpy as np
artifacts_df = pd.read_excel('../Cln_Dinosaur Fossil Auctions_21FEB2024_DRoss.xlsx', sheet_name="Artifacts")
# values = pd.DataFrame(artifacts_df.Estimate.str.split("-").to_list(), columns=["Estimation_Low", "Estimation_High"])
# artifacts_df[values.columns] = values

val = artifacts_df.Estimate.str.split("-")
val = val.str.extract('(\d+)')
print(val.describe)

# with pd.option_context('display.max_rows', None, 'display.max_columns', None):  # more options can be specified also
#     print(val)