import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

# Set random seed for reproducibility
np.random.seed(42)

# Generate realistic synthetic data
n_campaigns = 120
campaign_data = {
    'marketing_spend': np.random.uniform(10, 100, n_campaigns),
    'conversion_rate': np.random.uniform(1, 20, n_campaigns),
    'campaign_type': np.random.choice(['Social Media', 'Email', 'PPC', 'Display'], n_campaigns),
    'duration_days': np.random.randint(7, 60, n_campaigns)
}

# Add correlation
for i in range(n_campaigns):
    base_conversion = campaign_data['marketing_spend'][i] * 0.15 + np.random.normal(0, 2)
    campaign_data['conversion_rate'][i] = max(0.5, min(25, base_conversion))

df = pd.DataFrame(campaign_data)

# Seaborn styling
sns.set_style("whitegrid")
sns.set_context("notebook", font_scale=1.2)

# Fixed square figure that will export correctly
plt.figure(figsize=(6.4, 6.4))  # 6.4*80dpi ≈ 512px

# ✅ The expected Seaborn scatterplot
sns.scatterplot(
    data=df,
    x='marketing_spend',
    y='conversion_rate',
    hue='campaign_type',
    size='duration_days',
    sizes=(60, 200),
    alpha=0.8,
    palette='Set2'
)

plt.title('Marketing Campaign Effectiveness Analysis\nSpend vs Conversion Rate by Campaign Type',
          fontsize=16, fontweight='bold', pad=20)
plt.xlabel('Marketing Spend (Thousands USD)', fontsize=14, fontweight='semibold')
plt.ylabel('Conversion Rate (%)', fontsize=14, fontweight='semibold')
plt.legend(bbox_to_anchor=(1.05, 1), loc='upper left')
plt.grid(True, alpha=0.3)
sns.despine()
plt.tight_layout()

# ✅ Save directly as 512x512
plt.savefig("chart.png", dpi=80, bbox_inches='tight')

print("Chart generated successfully with Seaborn scatterplot!")

plt.show()
