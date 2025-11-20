import pandas as pd
import matplotlib.pyplot as plt
from datetime import datetime

# ----------------------------
# Load Data
# ----------------------------
df = pd.read_csv("data/application_data.csv")


# Convert date columns to datetime
df["applied_date"] = pd.to_datetime(df["applied_date"], errors="coerce")
df["response_date"] = pd.to_datetime(df["response_date"], errors="coerce")

# ----------------------------
# Summary Statistics
# ----------------------------
total_apps = len(df)
interviews = len(df[df["status"] == "Interview"])
rejections = len(df[df["status"] == "Rejected"])
waiting = len(df[df["status"] == "Applied"])

summary = f"""
JOB APPLICATION TRACKER SUMMARY
---------------------------------
Total Applications: {total_apps}
Interviews: {interviews}
Rejections: {rejections}
Waiting for Response: {waiting}
"""

print(summary)

# Save summary to reports folder
with open("reports/summary.txt", "w") as f:

    f.write(summary)

# ----------------------------
# Visualization 1 – Status Count
# ----------------------------
status_counts = df["status"].value_counts()

plt.figure(figsize=(6, 4))
status_counts.plot(kind="bar")
plt.title("Application Status Overview")
plt.ylabel("Count")
plt.tight_layout()
plt.savefig("charts/status_chart.png")
plt.close()

# ----------------------------
# Visualization 2 – Applications Over Time
# ----------------------------
df_by_date = df.groupby("applied_date").size()

plt.figure(figsize=(8, 4))
df_by_date.plot(kind="line", marker="o")
plt.title("Applications Over Time")
plt.ylabel("Number of Applications")
plt.tight_layout()
plt.savefig("charts/applications_over_time.png")
plt.close()

print("Charts saved in /charts folder")
print("Summary saved in /reports/summary.txt")
