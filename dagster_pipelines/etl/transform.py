import pandas as pd

# 2.2.1 Pivot data in the "KPI_FY.xlsm" file
def pivot_data(df: pd.DataFrame) -> pd.DataFrame:
    plan_actual_cols = [col for col in df.columns if col.startswith("Plan") or col.startswith("Actual")]

    id_vars = [col for col in df.columns if col not in plan_actual_cols]

    df_melted = df.melt(
        id_vars=id_vars,
        value_vars=plan_actual_cols,
        var_name="Amount_Name",
        value_name="Amount"
    )

    df_melted["Amount_Type"] = df_melted["Amount_Name"].apply(lambda x: "Plan" if x.startswith("Plan") else "Actual")

    final_cols = id_vars + ["Amount_Type", "Amount_Name", "Amount"]
    return df_melted[final_cols]