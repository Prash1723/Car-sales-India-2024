import pandas as pd
import numpy as np
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

## Percentage sales by manufacturer
make_sales = df.groupby('Make')[['Sales', 'Total']].sum().sort_values(by='Sales',ascending=False).reset_index()
make_sales.columns = ['Make', 'Sales', 'Total']
make_sales['perc_sales'] = (make_sales['Sales']*100)/make_sales['Sales'].sum()
make_sales['perc_total'] = (make_sales['Total']*100)/make_sales['Total'].sum()

plt.figure(figsize=[15,4])
ax1 = sns.barplot(data=make_sales, x='Make', y='perc_sales')
y_offset = 2
# Annotation
for i, t in enumerate(make_sales.perc_sales):
    plt.text(x = i, y = t + y_offset, s = str(round(t, 2))+"%", ha='center', fontsize=11, weight='bold')

plt.title("Percentage sales by manufacturers in India")
plt.show()

## Production by manufacturer
plt.figure(figsize=[15,4])
ax2 = sns.barplot(data=make_sales, x='Make', y='Total')
# Annotation
for i, t in enumerate(make_sales.Total):
     plt.text(x = i, y = t + y_offset, s = str(round(t, 2)), ha='center', fontsize=11, weight='bold')

plt.title("Cars produced by manufacturers in India")
plt.show()

## Sales by body type
bt_sales = df.groupby('Body Type')[['Sales', 'Total']].sum().sort_values(by='Sales',ascending=False).reset_index()
bt_sales.columns = ['Body Type', 'Sales', 'Total']
bt_sales['perc_sales'] = (bt_sales['Sales']*100)/bt_sales['Sales'].sum()
bt_sales['perc_total'] = (bt_sales['Total']*100)/bt_sales['Total'].sum()

plt.figure(figsize=[15,4])
ax3 = sns.barplot(data=bt_sales, x='Body Type', y='perc_sales')
y_offset = 2
# Annotation
for i, t in enumerate(bt_sales.perc_sales):
    plt.text(x = i, y = t + y_offset, s = str(round(t, 2))+"%", ha='center', fontsize=11, weight='bold')

plt.title("Percentage sales by car body types sold in India")
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
bt_make1 = df.groupby(['Make', 'Body Type'])['Sales'].count().reset_index()
bt_make1 = pd.pivot_table(
    bt_make1, 
    values=['Sales'], 
    index=['Make'], 
    columns=['Body Type'], 
    fill_value=0, 
    aggfunc="sum"
    ).reset_index()

print(bt_make1)

bt_make1.columns = ['Make', 'SUV', 'Hatchback', 'Sedan', 'MUV', 'Others']
bt_make1['Total'] = bt_make1[['SUV', 'Hatchback', 'Sedan', 'MUV', 'Others']].sum(axis=1)

bt_perc1 = bt_make1.select_dtypes('number').div(bt_make1['Total']*0.01, axis=0)
bt_make1.update(bt_perc1)
bt_make1.drop('Total', axis=1, inplace=True)
bt_make1.set_index('Make', inplace=True)

fig5, ax4 = plt.subplots(figsize=[4,15])
bottom = np.zeros(len(bt_make1))

# Create each bar with values using a loop
for i, col in enumerate(bt_make1.columns):
    ax4.barh(bt_make1.index, bt_make1[col], left=bottom, label=col)
    bottom+=bt_make1[col].values

# Calculate total values for positioning the total value of stacked bar (100)
totals1 = bt_make1.sum(axis=1)
x_offset = 4

# Assigning total length of the bar as label (annotation)
for i, t in enumerate(totals1):
    ax4.text(t + x_offset, i, round(t), va='center', weight='bold')

# Applying labels (annotation) for the middle bars
for bar in ax4.patches:
    width = bar.get_width()
    if width > 3:  # Only label visible bars
        ax4.text(
            bar.get_x() + width / 2,
            bar.get_y() + bar.get_height() / 2,
            round(width),
            ha='center',
            va='center',
            color='white',
            weight='bold',
            size=8
        )

# Chart control commands
plt.xlim(0,200)
ax4.legend(loc='upper right')
plt.tight_layout()
plt.title("Count of car makers and body types in India")
plt.show()

# Sales by manufacturer and body type
bt_make2 = pd.pivot_table(
    df, 
    values=['Sales'], 
    index=['Make'], 
    columns=['Body Type'], 
    fill_value=0, 
    aggfunc="sum"
    ).reset_index()

bt_make2.columns = ['Make', 'SUV', 'Hatchback', 'Sedan', 'MUV', 'Others']
bt_make2['Total'] = bt_make2[['SUV', 'Hatchback', 'Sedan', 'MUV', 'Others']].sum(axis=1)

bt_perc = bt_make2.select_dtypes('number').div(bt_make2['Total']*0.01, axis=0)
bt_make2.update(bt_perc)
bt_make2.drop('Total', axis=1, inplace=True)
bt_make2.set_index('Make', inplace=True)

fig5, ax5 = plt.subplots(figsize=[4,15])
bottom = np.zeros(len(bt_make2))

# Create each bar with values using a loop
for i, col in enumerate(bt_make2.columns):
    ax5.barh(bt_make2.index, bt_make2[col], left=bottom, label=col)
    bottom+=bt_make2[col].values

# Calculate total values for positioning the total value of stacked bar (100)
totals = bt_make2.sum(axis=1)
x_offset = 4

# Assigning total length of the bar as label (annotation)
for i, t in enumerate(totals):
    ax5.text(t + x_offset, i, round(t), va='center', weight='bold')

# Applying labels (annotation) for the middle bars
for bar in ax5.patches:
    width = bar.get_width()
    if width > 3:  # Only label visible bars
        ax5.text(
            bar.get_x() + width / 2,
            bar.get_y() + bar.get_height() / 2,
            round(width),
            ha='center',
            va='center',
            color='white',
            weight='bold',
            size=8
        )

# Chart control commands
plt.xlim(0,200)
ax5.legend(loc='upper right')
plt.tight_layout()
plt.title("Sales by makers and body types in India")
plt.show()

## Trend Analysis
plt.figure(figsize=[15,5])
sns.lineplot(data=df, x='Months', y='Sales', hue='Make')
plt.title("Sales trend of manufacturers in India")
plt.show()

## Seasonality for car sales
seasons = df.groupby('Months')['Sales'].sum()*100/df['Sales'].sum()
plt.figure(figsize=[15,5])
ax6 = sns.barplot(seasons)
# Annotation
y_offset = 0.2
for i, t in enumerate(seasons):
     plt.text(x = i, y = t + y_offset, s = str(round(t, 2))+"%", ha='center', fontsize=11, weight='bold')

plt.title("Seasonality of cars sales in India")
plt.show()

# Sales by manufacturer and body type
seasons_bt = pd.pivot_table(
    df, 
    values=['Sales'], 
    index=['Months'], 
    columns=['Body Type'], 
    fill_value=0, 
    aggfunc="sum"
    ).reset_index()

seasons_bt.columns = ['Months', 'SUV', 'Hatchback', 'Sedan', 'MUV', 'Others']
seasons_bt['Total'] = seasons_bt[['SUV', 'Hatchback', 'Sedan', 'MUV', 'Others']].sum(axis=1)

sbt_perc = seasons_bt.select_dtypes('number').div(seasons_bt['Total']*0.01, axis=0)
seasons_bt.update(sbt_perc)
seasons_bt.drop('Total', axis=1, inplace=True)
seasons_bt.set_index('Months', inplace=True)

fig5, ax7 = plt.subplots(figsize=[4,15])
bottom = np.zeros(len(seasons_bt))

# Create each bar with values using a loop
for i, col in enumerate(seasons_bt.columns):
    ax7.barh(seasons_bt.index, seasons_bt[col], left=bottom, label=col)
    bottom+=seasons_bt[col].values

# Calculate total values for positioning the total value of stacked bar (100)
totals = seasons_bt.sum(axis=1)
x_offset = 4

# Assigning total length of the bar as label (annotation)
for i, t in enumerate(totals):
    ax7.text(t + x_offset, i, round(t), va='center', weight='bold')

# Applying labels (annotation) for the middle bars
for bar in ax7.patches:
    width = bar.get_width()
    if width > 3:  # Only label visible bars
        ax7.text(
            bar.get_x() + width / 2,
            bar.get_y() + bar.get_height() / 2,
            round(width),
            ha='center',
            va='center',
            color='white',
            weight='bold',
            size=8
        )

# Chart control commands
plt.xlim(0,200)
ax7.legend(loc='upper right')
plt.tight_layout()
plt.title("Seasonality in car body types sold in India")
plt.show()