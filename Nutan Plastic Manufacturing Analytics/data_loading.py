# ============================================================
# NUTAN PLASTIC - DATA ANALYSIS PROJECT
# ============================================================

# ------------------------------------------------------------
# 1. IMPORT LIBRARIES
# ------------------------------------------------------------

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
# ------------------------------------------------------------
# 1. IMPORT LIBRARIES
# ------------------------------------------------------------

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns


# ------------------------------------------------------------
# 2. LOAD DATASET
# ------------------------------------------------------------

file_path = "Nutan_Plastic.csv"

df = pd.read_csv(file_path)
# ------------------------------------------------------------
# 3. DISPLAY BASIC INFORMATION
# ------------------------------------------------------------

print("\n================ DATASET LOADED ================\n")

print("Dataset Shape:")
print(df.shape)

print("\nNumber of Rows:", df.shape[0])
print("Number of Columns:", df.shape[1])


print("\n================ COLUMN NAMES ================\n")

print(df.columns.tolist())

# ------------------------------------------------------------
# 4. DISPLAY FIRST 5 RECORDS
# ------------------------------------------------------------

print("\n================ FIRST 5 RECORDS ================\n")

print(df.head())


# ------------------------------------------------------------
# 5. DISPLAY LAST 5 RECORDS
# ------------------------------------------------------------

print("\n================ LAST 5 RECORDS ================\n")

print(df.tail())

# ------------------------------------------------------------
# 6. DATA TYPES
# ------------------------------------------------------------

print("\n================ DATA TYPES ================\n")

print(df.dtypes)


# ------------------------------------------------------------
# 7. DATASET INFORMATION
# ------------------------------------------------------------

print("\n================ DATASET INFORMATION ================\n")

df.info()


# ------------------------------------------------------------
# 8. CHECK MISSING VALUES
# ------------------------------------------------------------

print("\n================ MISSING VALUES ================\n")

missing_values = df.isnull().sum()

print(missing_values)


print("\nTotal Missing Values:")

print(df.isnull().sum().sum())

# ------------------------------------------------------------
# 9. CHECK DUPLICATE RECORDS
# ------------------------------------------------------------

print("\n================ DUPLICATE RECORDS ================\n")

duplicates = df.duplicated().sum()

print("Number of duplicate records:", duplicates)

# ------------------------------------------------------------
# 10. CONVERT DATE COLUMN
# ------------------------------------------------------------

df["Production_Date"] = pd.to_datetime(
    df["Production_Date"],
    dayfirst=True,
    errors="coerce"
)


print("\n================ DATE INFORMATION ================\n")

print("Minimum Production Date:")

print(df["Production_Date"].min())

print("\nMaximum Production Date:")

print(df["Production_Date"].max())

# ------------------------------------------------------------
# 11. CREATE YEAR AND MONTH COLUMNS
# ------------------------------------------------------------

df["Year"] = df["Production_Date"].dt.year

df["Month"] = df["Production_Date"].dt.month

df["Month_Name"] = df["Production_Date"].dt.strftime("%B")

df["Month_Year"] = (
    df["Production_Date"]
    .dt.to_period("M")
    .astype(str)
)
# ------------------------------------------------------------
# 12. STATISTICAL SUMMARY
# ------------------------------------------------------------

print("\n================ STATISTICAL SUMMARY ================\n")

print(df.describe())

# ------------------------------------------------------------
# 13. UNIQUE VALUES
# ------------------------------------------------------------

print("\n================ UNIQUE VALUES ================\n")


print("\nProducts:")

print(df["Product_Name"].unique())


print("\nProduct Categories:")

print(df["Product_Category"].unique())


print("\nShifts:")

print(df["Shift"].unique())


print("\nMachines:")

print(df["Machine_ID"].unique())


print("\nProduction Status:")

print(df["Production_Status"].unique())


print("\nBatch Quality:")

print(df["Batch_Quality"].unique())


print("\nProduct Quality Level:")

print(df["Product_Quality_Level"].unique())


print("\nDefect Types:")

print(df["Defect_Type"].unique())

# ------------------------------------------------------------
# 14. BASIC PRODUCTION CALCULATIONS
# ------------------------------------------------------------

total_planned = df["Planned_Qty"].sum()

total_produced = df["Produced_Qty"].sum()

total_good = df["Good_Qty"].sum()

total_rejected = df["Rejected_Qty"].sum()

total_production_hours = df["Production_Hours"].sum()

total_downtime = df["Downtime_Hours"].sum()

total_raw_material = df["Raw_Material_Used_Kg"].sum()

total_wastage = df["Wastage_Kg"].sum()


print("\n================ PRODUCTION SUMMARY ================\n")

print("Total Planned Quantity:", total_planned)

print("Total Produced Quantity:", total_produced)

print("Total Good Quantity:", total_good)

print("Total Rejected Quantity:", total_rejected)

print("Total Production Hours:", total_production_hours)

print("Total Downtime Hours:", total_downtime)

print("Total Raw Material Used (Kg):", total_raw_material)

print("Total Wastage (Kg):", total_wastage)

# ------------------------------------------------------------
# 15. PRODUCTION ACHIEVEMENT
# ------------------------------------------------------------

if total_planned != 0:

    production_achievement = (
        total_produced / total_planned
    ) * 100

else:

    production_achievement = 0


print(
    "\nProduction Achievement:",
    round(production_achievement, 2),
    "%"
)

# ------------------------------------------------------------
# 16. QUALITY RATE
# ------------------------------------------------------------

if total_produced != 0:

    quality_rate = (
        total_good / total_produced
    ) * 100

else:

    quality_rate = 0


print(
    "Overall Quality Rate:",
    round(quality_rate, 2),
    "%"
)

# 17. REJECTION RATE
# ------------------------------------------------------------

if total_produced != 0:

    rejection_rate = (
        total_rejected / total_produced
    ) * 100

else:

    rejection_rate = 0


print(
    "Overall Rejection Rate:",
    round(rejection_rate, 2),
    "%"
)

# ------------------------------------------------------------
# 18. AVERAGE EFFICIENCY
# ------------------------------------------------------------

average_efficiency = df[
    "Production_Efficiency_%"
].mean()


print(
    "Average Production Efficiency:",
    round(average_efficiency, 2),
    "%"
)

# ------------------------------------------------------------
# 19. AVERAGE DEFECT RATE
# ------------------------------------------------------------

average_defect_rate = df[
    "Defect_Rate_%"
].mean()


print(
    "Average Defect Rate:",
    round(average_defect_rate, 2),
    "%"
)

# ============================================================
# PRODUCT ANALYSIS
# ============================================================

print("\n\n================ PRODUCT ANALYSIS ================\n")


product_analysis = df.groupby(
    "Product_Name"
).agg(

    Planned_Qty=("Planned_Qty", "sum"),

    Produced_Qty=("Produced_Qty", "sum"),

    Good_Qty=("Good_Qty", "sum"),

    Rejected_Qty=("Rejected_Qty", "sum"),

    Production_Hours=("Production_Hours", "sum"),

    Downtime_Hours=("Downtime_Hours", "sum"),

    Raw_Material_Used_Kg=(
        "Raw_Material_Used_Kg",
        "sum"
    ),

    Wastage_Kg=("Wastage_Kg", "sum"),

    Average_Efficiency=(
        "Production_Efficiency_%",
        "mean"
    ),

    Average_Defect_Rate=(
        "Defect_Rate_%",
        "mean"
    ),

    Average_Quality_Score=(
        "Product_Quality_Score",
        "mean"
    )

).reset_index()


print(product_analysis)

# ============================================================
# MACHINE ANALYSIS
# ============================================================

print("\n\n================ MACHINE ANALYSIS ================\n")


machine_analysis = df.groupby(
    "Machine_ID"
).agg(

    Planned_Qty=("Planned_Qty", "sum"),

    Produced_Qty=("Produced_Qty", "sum"),

    Good_Qty=("Good_Qty", "sum"),

    Rejected_Qty=("Rejected_Qty", "sum"),

    Production_Hours=("Production_Hours", "sum"),

    Downtime_Hours=("Downtime_Hours", "sum"),

    Wastage_Kg=("Wastage_Kg", "sum"),

    Average_Efficiency=(
        "Production_Efficiency_%",
        "mean"
    ),

    Average_Defect_Rate=(
        "Defect_Rate_%",
        "mean"
    )

).reset_index()


print(machine_analysis)

# ============================================================
# SHIFT ANALYSIS
# ============================================================

print("\n\n================ SHIFT ANALYSIS ================\n")


shift_analysis = df.groupby(
    "Shift"
).agg(

    Planned_Qty=("Planned_Qty", "sum"),

    Produced_Qty=("Produced_Qty", "sum"),

    Good_Qty=("Good_Qty", "sum"),

    Rejected_Qty=("Rejected_Qty", "sum"),

    Downtime_Hours=("Downtime_Hours", "sum"),

    Wastage_Kg=("Wastage_Kg", "sum"),

    Average_Efficiency=(
        "Production_Efficiency_%",
        "mean"
    ),

    Average_Defect_Rate=(
        "Defect_Rate_%",
        "mean"
    )

).reset_index()


print(shift_analysis)

# ============================================================
# DEFECT ANALYSIS
# ============================================================

print("\n\n================ DEFECT ANALYSIS ================\n")


# Treat "None" as no defect
df["Defect_Type"] = df[
    "Defect_Type"
].fillna("None")


defect_analysis = (
    df["Defect_Type"]
    .value_counts()
    .reset_index()
)


defect_analysis.columns = [
    "Defect_Type",
    "Count"
]


print(defect_analysis)

# ============================================================
# PRODUCTION STATUS ANALYSIS
# ============================================================

print("\n\n================ PRODUCTION STATUS ================\n")


status_analysis = (
    df["Production_Status"]
    .value_counts()
    .reset_index()
)


status_analysis.columns = [
    "Production_Status",
    "Count"
]


print(status_analysis)

# ============================================================
# QUALITY LEVEL ANALYSIS
# ============================================================

print("\n\n================ PRODUCT QUALITY LEVEL ================\n")


quality_analysis = (
    df["Product_Quality_Level"]
    .value_counts()
    .reset_index()
)


quality_analysis.columns = [
    "Product_Quality_Level",
    "Count"
]


print(quality_analysis)

# ============================================================
# BATCH QUALITY ANALYSIS
# ============================================================

print("\n\n================ BATCH QUALITY ================\n")


batch_quality = (
    df["Batch_Quality"]
    .value_counts()
    .reset_index()
)


batch_quality.columns = [
    "Batch_Quality",
    "Count"
]


print(batch_quality)

# ============================================================
# MONTHLY PRODUCTION
# ============================================================

print("\n\n================ MONTHLY PRODUCTION ================\n")


monthly_production = df.groupby(
    "Month_Year"
).agg(

    Planned_Qty=("Planned_Qty", "sum"),

    Produced_Qty=("Produced_Qty", "sum"),

    Good_Qty=("Good_Qty", "sum"),

    Rejected_Qty=("Rejected_Qty", "sum"),

    Downtime_Hours=("Downtime_Hours", "sum"),

    Wastage_Kg=("Wastage_Kg", "sum"),

    Average_Efficiency=(
        "Production_Efficiency_%",
        "mean"
    ),

    Average_Defect_Rate=(
        "Defect_Rate_%",
        "mean"
    )

).reset_index()


print(monthly_production)

# ============================================================
# OPERATOR ANALYSIS
# ============================================================

print("\n\n================ OPERATOR ANALYSIS ================\n")


operator_analysis = df.groupby(
    "Operator_ID"
).agg(

    Produced_Qty=("Produced_Qty", "sum"),

    Good_Qty=("Good_Qty", "sum"),

    Rejected_Qty=("Rejected_Qty", "sum"),

    Downtime_Hours=("Downtime_Hours", "sum"),

    Average_Efficiency=(
        "Production_Efficiency_%",
        "mean"
    ),

    Average_Defect_Rate=(
        "Defect_Rate_%",
        "mean"
    )

).reset_index()


print(operator_analysis)

# ============================================================
# TOP 10 PRODUCTS BY PRODUCTION
# ============================================================

print("\n\n================ TOP 10 PRODUCTS ================\n")


top_products = (
    df.groupby("Product_Name")["Produced_Qty"]
    .sum()
    .sort_values(ascending=False)
    .head(10)
)


print(top_products)

# ============================================================
# TOP 10 MACHINES BY PRODUCTION
# ============================================================

print("\n\n================ TOP 10 MACHINES ================\n")


top_machines = (
    df.groupby("Machine_ID")["Produced_Qty"]
    .sum()
    .sort_values(ascending=False)
    .head(10)
)


print(top_machines)

# ============================================================
# LOW EFFICIENCY MACHINES
# ============================================================

print("\n\n================ MACHINE EFFICIENCY ================\n")


machine_efficiency = (
    df.groupby("Machine_ID")[
        "Production_Efficiency_%"
    ]
    .mean()
    .sort_values()
)


print(machine_efficiency)

# ============================================================
# HIGH DEFECT PRODUCTS
# ============================================================

print("\n\n================ HIGH DEFECT PRODUCTS ================\n")


high_defect_products = (
    df.groupby("Product_Name")[
        "Defect_Rate_%"
    ]
    .mean()
    .sort_values(ascending=False)
)


print(high_defect_products)

# ============================================================
# CORRELATION ANALYSIS
# ============================================================

print("\n\n================ CORRELATION MATRIX ================\n")


numeric_columns = [

    "Planned_Qty",

    "Produced_Qty",

    "Good_Qty",

    "Rejected_Qty",

    "Production_Hours",

    "Downtime_Hours",

    "Raw_Material_Used_Kg",

    "Wastage_Kg",

    "Production_Efficiency_%",

    "Defect_Rate_%",

    "Product_Quality_Score"

]


correlation = df[numeric_columns].corr()


print(correlation)

# ============================================================
# VISUALIZATION
# ============================================================

sns.set_theme(style="whitegrid")

# ------------------------------------------------------------
# GRAPH 1 - PRODUCTION BY PRODUCT
# ------------------------------------------------------------

plt.figure(figsize=(12, 6))

product_production = (
    df.groupby("Product_Name")["Produced_Qty"]
    .sum()
    .sort_values(ascending=False)
)


sns.barplot(
    x=product_production.values,
    y=product_production.index
)


plt.title("Production Quantity by Product")

plt.xlabel("Produced Quantity")

plt.ylabel("Product")

plt.tight_layout()

plt.show()

# ------------------------------------------------------------
# GRAPH 2 - PRODUCTION BY MACHINE
# ------------------------------------------------------------

plt.figure(figsize=(10, 6))

machine_production = (
    df.groupby("Machine_ID")["Produced_Qty"]
    .sum()
    .sort_values(ascending=False)
)


sns.barplot(
    x=machine_production.index,
    y=machine_production.values
)


plt.title("Production Quantity by Machine")

plt.xlabel("Machine ID")

plt.ylabel("Produced Quantity")

plt.tight_layout()

plt.show()

# ------------------------------------------------------------
# GRAPH 3 - PRODUCTION BY SHIFT
# ------------------------------------------------------------

plt.figure(figsize=(8, 5))

shift_production = (
    df.groupby("Shift")["Produced_Qty"]
    .sum()
)


sns.barplot(
    x=shift_production.index,
    y=shift_production.values
)


plt.title("Production Quantity by Shift")

plt.xlabel("Shift")

plt.ylabel("Produced Quantity")

plt.tight_layout()

plt.show()

# ------------------------------------------------------------
# GRAPH 4 - DEFECT TYPE
# ------------------------------------------------------------

plt.figure(figsize=(10, 6))

defect_counts = (
    df["Defect_Type"]
    .value_counts()
)


sns.barplot(
    x=defect_counts.values,
    y=defect_counts.index
)


plt.title("Defect Type Distribution")

plt.xlabel("Number of Records")

plt.ylabel("Defect Type")

plt.tight_layout()

plt.show()

# ------------------------------------------------------------
# GRAPH 5 - QUALITY LEVEL
# ------------------------------------------------------------

plt.figure(figsize=(8, 5))

quality_counts = (
    df["Product_Quality_Level"]
    .value_counts()
)


sns.barplot(
    x=quality_counts.index,
    y=quality_counts.values
)


plt.title("Product Quality Level Distribution")

plt.xlabel("Quality Level")

plt.ylabel("Number of Records")

plt.tight_layout()

plt.show()

# ------------------------------------------------------------
# GRAPH 6 - PRODUCTION STATUS
# ------------------------------------------------------------

plt.figure(figsize=(8, 5))

status_counts = (
    df["Production_Status"]
    .value_counts()
)


sns.barplot(
    x=status_counts.index,
    y=status_counts.values
)


plt.title("Production Status Distribution")

plt.xlabel("Production Status")

plt.ylabel("Number of Records")

plt.tight_layout()

plt.show()

# ------------------------------------------------------------
# GRAPH 7 - MONTHLY PRODUCTION
# ------------------------------------------------------------

plt.figure(figsize=(15, 6))

plt.plot(
    monthly_production["Month_Year"],
    monthly_production["Produced_Qty"],
    marker="o"
)


plt.title("Monthly Production Trend")

plt.xlabel("Month")

plt.ylabel("Produced Quantity")

plt.xticks(rotation=45)

plt.tight_layout()

plt.show()

# ------------------------------------------------------------
# GRAPH 8 - MONTHLY EFFICIENCY
# ------------------------------------------------------------

plt.figure(figsize=(15, 6))

plt.plot(
    monthly_production["Month_Year"],
    monthly_production["Average_Efficiency"],
    marker="o"
)


plt.title("Monthly Production Efficiency")

plt.xlabel("Month")

plt.ylabel("Efficiency (%)")

plt.xticks(rotation=45)

plt.tight_layout()

plt.show()

# ------------------------------------------------------------
# GRAPH 9 - MONTHLY DOWNTIME
# ------------------------------------------------------------

plt.figure(figsize=(15, 6))

plt.plot(
    monthly_production["Month_Year"],
    monthly_production["Downtime_Hours"],
    marker="o"
)


plt.title("Monthly Downtime Analysis")

plt.xlabel("Month")

plt.ylabel("Downtime Hours")

plt.xticks(rotation=45)

plt.tight_layout()

plt.show()

# ------------------------------------------------------------
# GRAPH 10 - CORRELATION HEATMAP
# ------------------------------------------------------------

plt.figure(figsize=(12, 8))

sns.heatmap(
    correlation,
    annot=True,
    fmt=".2f",
    cmap="coolwarm"
)


plt.title("Correlation Between Production Variables")

plt.tight_layout()

plt.show()

# ============================================================
# SAVE ANALYSIS FILES
# ============================================================

product_analysis.to_csv(
    "product_analysis.csv",
    index=False
)


machine_analysis.to_csv(
    "machine_analysis.csv",
    index=False
)


shift_analysis.to_csv(
    "shift_analysis.csv",
    index=False
)


monthly_production.to_csv(
    "monthly_production.csv",
    index=False
)


defect_analysis.to_csv(
    "defect_analysis.csv",
    index=False
)


operator_analysis.to_csv(
    "operator_analysis.csv",
    index=False
)

# ============================================================
# SAVE CLEANED DATASET
# ============================================================

df.to_csv(
    "Nutan_Plastic_Cleaned.csv",
    index=False
)


print("\n\n================================================")
print("       ANALYSIS COMPLETED SUCCESSFULLY")
print("================================================")

print("\nFiles created:")

print("1. product_analysis.csv")
print("2. machine_analysis.csv")
print("3. shift_analysis.csv")
print("4. monthly_production.csv")
print("5. defect_analysis.csv")
print("6. operator_analysis.csv")
print("7. Nutan_Plastic_Cleaned.csv")

print("\nDone!")

