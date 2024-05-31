import xlrd

class xlsx_Parser():
    pass

import pandas as pd
dfs = pd.read_excel("Recap_Game_FM24.xlsx", sheet_name="Résultats")
print(dfs.head(10))
