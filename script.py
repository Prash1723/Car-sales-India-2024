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
make_sales = df.groupby('Make')[['Sales', 'Total']].sum().sort_values(by='Sales',ascending=False).reset_index()
make_sales.columns = ['Make', 'Sales', 'Total']
make_sales['Sales_perc'] = make_sales.Sales/make_sales.Total

plt.figure(figsize=[15,4])
ax1 = sns.barplot(data=make_sales, x='Make', y='Sales')
y_offset = 2
# Annotation
for i, t in enumerate(make_sales.Sales):
    plt.text(x = i, y = t + y_offset, s = str(round(t, 2)), ha='center', fontsize=11, weight='bold')

plt.title("Sales by manufacturers in India")
plt.show()

## Percentage sales by manufacturer
plt.figure(figsize=[15,4])
ax2 = sns.barplot(data=make_sales, x='Make', y='Total')
# Annotation
for i, t in enumerate(make_sales.Total):
     plt.text(x = i, y = t + y_offset, s = str(round(t, 2)), ha='center', fontsize=11, weight='bold')

plt.title("Cars produced by manufacturers in India")
plt.show()

## Sales by body type
bt_sales = df.groupby('Body Type')[['Sales', 'Total']].sum().sort_values(ascending=False).reset_index()
bt_sales.columns = ['Body Type', 'Sales', 'Total']

plt.figure(figsize=[15,4])
ax3 = sns.barplot(data=bt_sales, x='Body Type', y='Sales')
y_offset = 2
# Annotation
for i, t in enumerate(bt_sales.Sales):
    plt.text(x = i, y = t + y_offset, s = str(round(t, 2)), ha='center', fontsize=11, weight='bold')

plt.title("Sales by car body types sold in India")
plt.show()

## Total production by car body type
plt.figure(figsize=[15,4])
ax4 = sns.barplot(data=bt_sales, x='Body Type', y='Total')
y_offset = 2
# Annotation
for i, t in enumerate(bt_sales.Total):
    plt.text(x = i, y = t + y_offset, s = str(round(t, 2)), ha='center', fontsize=11, weight='bold')

plt.title("Production by car body types sold in India")
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

## 