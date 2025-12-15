import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns
import pandas as pd
import os

# Set style
sns.set_theme(style="whitegrid")
plt.rcParams['font.family'] = 'sans-serif'
plt.rcParams['font.sans-serif'] = ['Arial', 'DejaVu Sans', 'Liberation Sans', 'Bitstream Vera Sans', 'sans-serif']

# Data from Project README/Results
data = {
    'Model': ['XGBoost (Corona Subset)', 'FNN (Corona Subset)', 'XGBoost (Generalization)'],
    'AUC': [0.994, 0.975, 0.981],
    'F1 Score': [0.88, 0.71, 0.87],
    'MCC': [0.789, 0.579, 0.829]
}

df = pd.DataFrame(data)

# Melt dataframe for seaborn
df_melted = df.melt(id_vars='Model', var_name='Metric', value_name='Score')

# Create plot
plt.figure(figsize=(10, 6))
palette = ["#2ecc71", "#3498db", "#9b59b6"]  # Green, Blue, Purple
ax = sns.barplot(x='Metric', y='Score', hue='Model', data=df_melted, palette=palette)

# Add values on top of bars
for container in ax.containers:
    ax.bar_label(container, fmt='%.3f', padding=3, fontsize=10, fontweight='bold')

# Customization
plt.title('Model Performance Comparison: XGBoost vs FNN', fontsize=16, fontweight='bold', pad=20)
plt.ylabel('Score', fontsize=12)
plt.xlabel('Metric', fontsize=12)
plt.ylim(0, 1.15)  # Add space for labels and legend
plt.legend(title='Model Scenario', loc='upper center', bbox_to_anchor=(0.5, -0.15), ncol=3, frameon=False)

# Adjust layout
plt.tight_layout()

# Save
output_path = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), 'assets', 'results_comparison.png')
plt.savefig(output_path, dpi=300, bbox_inches='tight')
print(f"Plot saved to {output_path}")
