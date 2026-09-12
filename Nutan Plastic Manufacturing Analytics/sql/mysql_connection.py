

import mysql.connector
import pandas as pd

conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="12345",
    database="nutan_plastic_db"
)
print ("mysql connected successfully!")

# -----------------------------------
# FETCH DATA FROM NUTAN_PLASTIC TABLE
# -----------------------------------

query = """
SELECT *
FROM Nutan_Plastic
"""

df = pd.read_sql(query, conn)

print("\nData fetched successfully!")
print("Total Rows:", len(df))
print("Total Columns:", len(df.columns))

print("\nFirst 10 Records:")
print(df.head(10))

# -----------------------------------
# BASIC INFORMATION
# -----------------------------------

print("\nColumn Names:")
print(df.columns.tolist())

print("\nData Information:")
print(df.info())

# -----------------------------------
# PRODUCTION ANALYSIS
# -----------------------------------

print("\nTotal Production:")
print(df["Produced_Qty"].sum())

print("\nTotal Good Quantity:")
print(df["Good_Qty"].sum())

print("\nTotal Rejected Quantity:")
print(df["Rejected_Qty"].sum())

# -----------------------------------
# MACHINE ANALYSIS
# -----------------------------------

machine_analysis = df.groupby("Machine_ID").agg(
    Total_Produced=("Produced_Qty", "sum"),
    Total_Good=("Good_Qty", "sum"),
    Total_Rejected=("Rejected_Qty", "sum"),
    Average_Efficiency=("Production_Efficiency_Percent", "mean"),
    Total_Downtime=("Downtime_Hours", "sum")
).reset_index()

print("\nMachine Analysis:")
print(machine_analysis)

# -----------------------------------
# PRODUCT ANALYSIS
# -----------------------------------

product_analysis = df.groupby("Product_Name").agg(
    Total_Produced=("Produced_Qty", "sum"),
    Total_Good=("Good_Qty", "sum"),
    Total_Rejected=("Rejected_Qty", "sum")
).reset_index()

print("\nProduct Analysis:")
print(product_analysis)

# -----------------------------------
# SHIFT ANALYSIS
# -----------------------------------

shift_analysis = df.groupby("Shift").agg(
    Produced_Qty=("Produced_Qty", "sum"),
    Good_Qty=("Good_Qty", "sum"),
    Rejected_Qty=("Rejected_Qty", "sum"),
    Average_Efficiency=("Production_Efficiency_Percent", "mean")
).reset_index()

print("\nShift Analysis:")
print(shift_analysis)

# -----------------------------------
# DEFECT ANALYSIS
# -----------------------------------

defect_analysis = df.groupby("Defect_Type").agg(
    Total_Rejected=("Rejected_Qty", "sum")
).reset_index()

defect_analysis = defect_analysis.sort_values(
    by="Total_Rejected",
    ascending=False
)

print("\nDefect Analysis:")
print(defect_analysis)

# -----------------------------------
# QUALITY ANALYSIS
# -----------------------------------

quality_analysis = df.groupby("Product_Quality_Level").agg(
    Total_Records=("Product_Quality_Level", "count"),
    Average_Quality_Score=("Product_Quality_Score", "mean")
).reset_index()

print("\nQuality Analysis:")
print(quality_analysis)

# -----------------------------------
# MONTHLY PRODUCTION TREND
# -----------------------------------

df["Production_Date"] = pd.to_datetime(
    df["Production_Date"]
)

monthly_production = df.groupby(
    df["Production_Date"].dt.to_period("M")
).agg(
    Produced_Qty=("Produced_Qty", "sum"),
    Good_Qty=("Good_Qty", "sum"),
    Rejected_Qty=("Rejected_Qty", "sum")
).reset_index()

monthly_production["Production_Date"] = (
    monthly_production["Production_Date"].astype(str)
)

print("\nMonthly Production:")
print(monthly_production)


# -----------------------------------
# SAVE ANALYSIS RESULTS
# -----------------------------------

machine_analysis.to_csv("machine_analysis.csv", index=False)
product_analysis.to_csv("product_analysis.csv", index=False)
shift_analysis.to_csv("shift_analysis.csv", index=False)
defect_analysis.to_csv("defect_analysis.csv", index=False)
quality_analysis.to_csv("quality_analysis.csv", index=False)
monthly_production.to_csv("monthly_production.csv", index=False)

print("\nAnalysis files saved successfully!")