import pandas as pd
import matplotlib.pyplot as plt

# Load Titanic dataset
df = pd.read_csv("train.csv")

# -----------------------------
# Bar Chart (Categorical Variable - Sex)
# -----------------------------
gender_counts = df['Sex'].value_counts()

plt.figure()
plt.bar(gender_counts.index, gender_counts.values)

plt.xlabel("Gender")
plt.ylabel("Number of Passengers")
plt.title("Distribution of Gender on Titanic")

plt.show()


# -----------------------------
# Histogram (Continuous Variable - Age)
# -----------------------------
plt.figure()
plt.hist(df['Age'].dropna(), bins=10)

plt.xlabel("Age")
plt.ylabel("Number of Passengers")
plt.title("Distribution of Age on Titanic")

plt.show()
