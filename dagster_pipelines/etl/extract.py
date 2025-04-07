import pandas as pd

# 2.1.1 Read KPI evaluation data from the "Data to DB" sheet in the "KPI_FY.xlsm" Excel file
def read_excel() -> pd.DataFrame:
    file_path = "dagster_pipelines/data/KPI_FY.xlsm"
    try:
        df = pd.read_excel(file_path, sheet_name="Data to DB")
        print(f"Loaded Excel file: {file_path} (rows: {len(df)})")
        return df
    except FileNotFoundError:
        raise Exception(f"Excel file not found at {file_path}")
    except Exception as e:
        raise Exception(f"Failed to read Excel file: {e}")

# 2.1.2 Read center master data from the "M_Center.csv" CSV file
def read_csv() -> pd.DataFrame:
    file_path = "dagster_pipelines/data/M_Center.csv"
    try:
        df = pd.read_csv(file_path)
        print(f"Loaded Excel file: {file_path} (rows: {len(df)})")
        return df
    except FileNotFoundError:
        raise Exception(f"Excel file not found at {file_path}")
    except Exception as e:
        raise Exception(f"Failed to read Excel file: {e}")