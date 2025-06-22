import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_excel(r'data/Car Sales in India - 2024 (Unpivot Version).xlsx')

# EDA
print(df.head())

print(df.info())

# Univariate Analysis

## Favourite manufacturer
plt.figure(figsize=[15,4])
sns.countplot(data=df, x='Make')
plt.title("All manufacturers in India")
plt.show()

## Favourite body type
plt.figure(figsize=[15,4])
sns.countplot(data=df, x='Body Type')
plt.title("All car body types sold in India")
plt.show()

## Favourite segment
plt.figure(figsize=[15,4])
sns.countplot(data=df, x='Segment')
plt.title("Favourite segment in India")
plt.show()

## Sales by manufacturer
plt.figure(figsize=[15,4])
sns.barplot(data=df, x='Make', y='Sales')
plt.title("Sales by manufacturers in India")
plt.show()

## Sales by body type
plt.figure(figsize=[15,4])
sns.barplot(data=df, x='Body Type', y='Sales')
plt.title("Sales by car body types sold in India")
plt.show()

# Summary
print(df.select_dtypes('number').describe())

# Bivariate Analysis

## Product body available from manufacturer
plt.figure(figsize=[4,15])
sns.countplot(data=df, y='Make', hue='Body Type')
plt.title("All manufacturers in India")
plt.show()

## Trend Analysis
plt.figure(figsize=[15,5])
sns.lineplot(data=df, x='Months', y='Sales', hue='Make')
plt.title("Sales trend of manufacturers in India")
plt.show()