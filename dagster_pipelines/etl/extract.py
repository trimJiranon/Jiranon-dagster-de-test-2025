import pandas as pd

# 2.1.1 Read KPI evaluation data from the "Data to DB" sheet in the "KPI_FY.xlsm" Excel file
def read_excel() -> pd.DataFrame:
    df = pd.read_excel('/data/KPI_FY.xlsm')
    pass

# 2.1.2 Read center master data from the "M_Center.csv" CSV file
def read_csv() -> pd.DataFrame:
    df = read_csv('/data/M_Center.csv')
    pass