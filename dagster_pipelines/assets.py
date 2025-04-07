import dagster as dg
from dagster_pipelines.etl.extract import read_excel, read_csv
from dagster_pipelines.etl.transform import pivot_data
from dagster_pipelines.etl.load import load_to_duckdb

# 2.3.1.1 Load pivoted KPI_FY.xlsm into KPI_FY
@dg.asset(compute_kind="duckdb", group_name="plan")
def kpi_fy(context: dg.AssetExecutionContext):
    kpi_raw = read_excel()
    Kpi_fy = pivot_data(kpi_raw)
    load_to_duckdb(Kpi_fy, table_name="KPI_FY")
    return Kpi_fy

# 2.3.1.2 Load M_Center.csv into M_Center
@dg.asset(compute_kind="duckdb", group_name="plan")
def m_center(context: dg.AssetExecutionContext):
    M_Center = read_csv()
    load_to_duckdb(M_Center, table_name="M_Center")
    return M_Center

# 2.3.2 Create asset kpi_fy_final_asset()
@dg.asset(compute_kind="duckdb", group_name="plan")
def kpi_fy_final_asset(context: dg.AssetExecutionContext, kpi_fy, m_center):
    kpi_fy_final = kpi_fy.merge(m_center, how="left", on="Center_ID")
    kpi_fy_final["updated_at"] = kpi_fy_final.Timestamp.now()
    load_to_duckdb(kpi_fy_final, table_name="KPI_FY_FINAL")
    return kpi_fy_final