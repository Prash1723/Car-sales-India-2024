import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_excel(r'data/Car Sales in India - 2024 (Unpivot Version).xlsx')

# EDA
print(df.head())

print(df.info())

# Favourite manufacturer
plt.figure(figsize=[15,4])
sns.countplot(data=df, x='Make')
plt.title("All manufacturers in India")
plt.show()

# Favourite body type
plt.figure(figsize=[15,4])
sns.countplot(data=df, x='Body Type')
plt.title("All car body types sold in India")
plt.show()

# Favourite segment
plt.figure(figsize=[15,4])
sns.countplot(data=df, x='Segment')
plt.title("Favourite segment in India")
plt.show()

# Summary
print(df.select_dtypes('number').describe())

# Bivariate Analysis

## Product body available from manufacturer
plt.figure(figsize=[4,15])
sns.countplot(data=df, y='Make', hue='Body Type')
plt.title("All manufacturers in India")
plt.show()