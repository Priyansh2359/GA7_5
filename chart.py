# chart.py
# Author: 23f2000814@ds.study.iitm.ac.in
# This script generates a professional violinplot for support response times

import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

# -----------------------------
# Generate synthetic business data
# -----------------------------
np.random.seed(42)

channels = ["Email", "Chat", "Phone", "Social Media"]

data = []
for channel in channels:
    if channel == "Email":
        response_times = np.random.normal(loc=30, scale=10, size=200)  # slower
    elif channel == "Chat":
        response_times = np.random.normal(loc=10, scale=4, size=200)   # fast
    elif channel == "Phone":
        response_times = np.random.normal(loc=20, scale=6, size=200)   # medium
    else:  # Social Media
        response_times = np.random.normal(loc=15, scale=5, size=200)   # moderate
    
    # Clip values to avoid negatives
    response_times = np.clip(response_times, 1, None)
    
    for rt in response_times:
        data.append({"Channel": channel, "ResponseTime": rt})

df = pd.DataFrame(data)

# -----------------------------
# Visualization
# -----------------------------
sns.set_style("whitegrid")
sns.set_context("talk")  # presentation-ready sizes

plt.figure(figsize=(8, 8))  # 512x512 pixels with dpi=64

ax = sns.violinplot(
    x="Channel",
    y="ResponseTime",
    data=df,
    palette="Set2",
    inner="box",  # add a small boxplot inside
    linewidth=1.2
)

# Title and labels
ax.set_title("Customer Support Response Time Distribution by Channel", fontsize=14, weight="bold")
ax.set_xlabel("Support Channel", fontsize=12)
ax.set_ylabel("Response Time (minutes)", fontsize=12)

# Save chart (512x512 pixels)
plt.savefig("chart.png", dpi=64, bbox_inches="tight")
plt.close()
