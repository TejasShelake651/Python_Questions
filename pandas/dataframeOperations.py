import os
import pandas as pd

def main():
    # 1. Pandas Series with Custom Labels
    print("Pandas Series with Custom Labels:")
    series_data = pd.Series([10, 20, 30, 40], index=['A', 'B', 'C', 'D'])
    print(series_data)
    print("Value at index 'C':", series_data['C'])

    # 2. Creating Pandas DataFrame from a Dictionary
    print("\nPandas DataFrame from Dictionary:")
    student_data = {
        'RollNo': [101, 102, 103, 104],
        'Name': ['Viraj', 'Raj', 'Rahul', 'Sneha'],
        'Marks': [85, 92, 78, 88],
        'Branch': ['CSE', 'IT', 'CSE', 'ENTC']
    }
    df = pd.DataFrame(student_data)
    print(df)

    # 3. Summary Statistics
    print("\nSummary Statistics:\n", df.describe())

    # 4. Boolean Indexing / Filtering
    print("\nFiltered Records (Marks > 80):\n", df[df['Marks'] > 80])

    # 5. Exporting DataFrame to CSV and Reading back
    sample_csv = "temp_students_export.csv"
    df.to_csv(sample_csv, index=False)
    print(f"\nSaved DataFrame to '{sample_csv}' and reading it back:")
    df_from_csv = pd.read_csv(sample_csv)
    print(df_from_csv)

    if os.path.exists(sample_csv):
        os.remove(sample_csv)


if __name__ == "__main__":
    main()
