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
plt.title("Indian's favourite manufacturers")
plt.show()

# Favourite model
plt.figure(figsize=[4,15])
sns.countplot(data=df, y='Model')
plt.title("Indian's favourite model")
plt.show()

# Favourite body type
plt.figure(figsize=[15,4])
sns.countplot(data=df, x='Body Type')
plt.title("Indian's favourite body type")
plt.show()