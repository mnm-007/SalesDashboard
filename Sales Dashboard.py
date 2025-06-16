import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load and preprocess data
df = pd.read_csv("Dashboard.csv")
df["Date"] = pd.to_datetime(df["Date"], format="%d-%m-%y")

# Set up Seaborn style
sns.set(style="whitegrid")

# ---- KPI Summary ----
total_sales = df["Total Sales"].sum()
total_profit = df["Total Profit"].sum()
avg_unit_price = df["Unit Price"].mean()

print("📊 KPI Summary")
print(f"Total Sales: ${total_sales:,.2f}")
print(f"Total Profit: ${total_profit:,.2f}")
print(f"Average Unit Price: ${avg_unit_price:.2f}")

# ---- Line Chart: Total Sales Over Time ----
plt.figure(figsize=(10, 5))
sns.lineplot(data=df, x="Date", y="Total Sales", marker="o", color="royalblue")
plt.title("Total Sales Over Time")
plt.ylabel("Sales")
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

# ---- Bar Chart: Total Profit by Date ----
plt.figure(figsize=(10, 5))
sns.barplot(data=df, x="Date", y="Total Profit", color="seagreen")
plt.title("Daily Profit")
plt.ylabel("Profit")
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

# ---- Moving Average of Sales (optional) ----
df["Sales MA (7-day)"] = df["Total Sales"].rolling(window=7).mean()

plt.figure(figsize=(10, 5))
sns.lineplot(data=df, x="Date", y="Sales MA (7-day)", color="orange")
plt.title("7-Day Moving Average of Sales")
plt.ylabel("Moving Avg Sales")
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()
