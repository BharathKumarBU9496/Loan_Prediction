import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.preprocessing import LabelEncoder

# Create a sample dataset
data = {
    'Gender': np.random.choice(['Male', 'Female'], size=100),
    'Married': np.random.choice(['Yes', 'No'], size=100),
    'ApplicantIncome': np.random.normal(5000, 1500, 100).astype(int),
    'LoanAmount': np.random.normal(150, 50, 100).astype(int),
    'Credit_History': np.random.choice([1, 0], size=100, p=[0.8, 0.2]),
    'Loan_Status': np.random.choice(['Y', 'N'], size=100, p=[0.7, 0.3])
}

df = pd.DataFrame(data)

# Convert categorical variables to numeric
le = LabelEncoder()
df['Gender'] = le.fit_transform(df['Gender'])
df['Married'] = le.fit_transform(df['Married'])
df['Loan_Status'] = le.fit_transform(df['Loan_Status'])

# Visualization 1: Pairplot
sns.pairplot(df, hue='Loan_Status', vars=['Gender', 'Married', 'ApplicantIncome', 'LoanAmount', 'Credit_History'])
plt.suptitle("Feature Relationships with Loan Status", y=1.02)  # Adjust the title to avoid overlap with plots
plt.show()

# Visualization 2: Heatmap of the correlations
plt.figure(figsize=(8, 6))
sns.heatmap(df.corr(), annot=True, cmap='coolwarm', fmt=".2f")
plt.title("Correlation Heatmap")
plt.show()

# Visualization 3: Count plots for categorical variables
fig, ax = plt.subplots(1, 2, figsize=(12, 5))
sns.countplot(x='Gender', hue='Loan_Status', data=df, ax=ax[0])
ax[0].set_title('Loan Status by Gender')
ax[0].set_xlabel('Gender')
ax[0].set_ylabel('Count')

sns.countplot(x='Married', hue='Loan_Status', data=df, ax=ax[1])
ax[1].set_title('Loan Status by Marital Status')
ax[1].set_xlabel('Marital Status')
ax[1].set_ylabel('Count')

plt.tight_layout()
plt.show()
