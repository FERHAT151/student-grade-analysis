import pandas as pd

df = pd.read_csv("data/students.csv")

print("=== Student Data ===")
print(df)

print("\n=== Statistics ===")

print(f"Average Grade: {df['final_grade'].mean():.2f}")
print(f"Highest Grade: {df['final_grade'].max()}")
print(f"Lowest Grade: {df['final_grade'].min()}")

best_student = df.loc[df['final_grade'].idxmax()]

print("\nTop Student:")
print(best_student["name"])