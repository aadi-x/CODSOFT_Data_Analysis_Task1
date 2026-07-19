import pandas as pd

# Load dataset
df = pd.read_csv("CodSoft/train.csv")

print("Original Shape:", df.shape)

# Check missing values
print("\nMissing Values:")
print(df.isnull().sum())

# Remove duplicate rows
df = df.drop_duplicates()

# Fill missing Age values with median
df["Age"] = df["Age"].fillna(df["Age"].median())

# Fill missing Embarked values with mode
df["Embarked"] = df["Embarked"].fillna(df["Embarked"].mode()[0])

# Drop Cabin column (too many missing values)
df.drop("Cabin", axis=1, inplace=True)

# Save cleaned dataset
df.to_csv("cleaned_titanic.csv", index=False)

print("\nCleaned Shape:", df.shape)

print("\nMissing Values After Cleaning:")
print(df.isnull().sum())

print("\nDataset Cleaned Successfully!")