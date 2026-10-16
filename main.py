
# Student Performance Analytics System

# Import libraries
import pandas as pd
import numpy as np

# Step 1: Read the CSV file
df = pd.read_csv("students.csv")

# Step 2: Display student data
print("STUDENT PERFORMANCE ANALYTICS SYSTEM")
print("------------------------------------")

print("\nStudent Records:")
print(df)

# Step 3: Count total students
total_students = len(df)
print("\nTotal Students:", total_students)

# Step 4: Calculate total marks and average marks
for i in range(len(df)):

    # Get marks of the current student
    math = df.loc[i, "Math_Marks"]
    python = df.loc[i, "Python_Marks"]
    oops = df.loc[i, "OOPS_Marks"]

    # Calculate total and average
    total = math + python + oops
    average = total / 3

    # Save the results in the DataFrame
    df.loc[i, "Total_Marks"] = total
    df.loc[i, "Average_Marks"] = average

# Display total and average marks
print("\nTotal and Average Marks:")
print(df[["Name", "Total_Marks", "Average_Marks"]])

# Step 5: Calculate grades
for i in range(len(df)):

    average = df.loc[i, "Average_Marks"]

    if average >= 90:
        grade = "A+"
    elif average >= 80:
        grade = "A"
    elif average >= 70:
        grade = "B"
    elif average >= 60:
        grade = "C"
    elif average >= 50:
        grade = "D"
    else:
        grade = "F"

    df.loc[i, "Grade"] = grade

# Display grades
print("\nStudent Grades:")
print(df[["Name", "Average_Marks", "Grade"]])

# Step 6: Check pass or fail
# A student passes if all three subjects have at least 35 marks
for i in range(len(df)):

    math = df.loc[i, "Math_Marks"]
    python = df.loc[i, "Python_Marks"]
    oops = df.loc[i, "OOPS_Marks"]

    if math >= 35 and python >= 35 and oops >= 35:
        result = "Pass"
    else:
        result = "Fail"

    df.loc[i, "Result"] = result

# Display pass/fail results
print("\nPass or Fail:")
print(df[["Name", "Result"]])

# Step 7: Find average marks in each subject
print("\nSubject-wise Average Marks:")

math_average = np.mean(df["Math_Marks"])
python_average = np.mean(df["Python_Marks"])
oops_average = np.mean(df["OOPS_Marks"])

print("Math Average:", round(math_average, 2))
print("Python Average:", round(python_average, 2))
print("OOPS Average:", round(oops_average, 2))

# Step 8: Find the top-performing student
highest_average = df["Average_Marks"].max()

print("\nTop-performing Student:")

for i in range(len(df)):
    if df.loc[i, "Average_Marks"] == highest_average:
        print(df.loc[i, "Name"])
        print("Average Marks:", highest_average)

# Step 9: Find overall class average
class_average = np.mean(df["Average_Marks"])

print("\nOverall Class Average:", round(class_average, 2))

# Step 10: Save the final results
df.to_csv("student_analysis_results.csv", index=False)

print("\nAnalysis completed successfully!")
print("Results saved in student_analysis_results.csv")

