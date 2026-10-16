# Student Performance Analytics System

## 1. Project Overview

The Student Performance Analytics System is a beginner-friendly Python project that analyzes student marks and attendance. It processes student data and displays useful information about academic performance.

The project uses Python, Pandas, and NumPy to perform calculations and generate analysis results.

## 2. Project Objective

The main objective of this project is to analyze student performance and understand academic results through marks, grades, pass/fail status, and subject-wise averages.

## 3. Technologies Used

- **Python** – For programming and calculations.
- **Pandas** – For reading and processing student data.
- **NumPy** – For numerical calculations.
- **CSV** – For storing student records and analysis results.
- **VS Code** – For writing and running the Python program.

## 4. Dataset Description

The project uses a CSV file named `students.csv`.

The dataset contains the following columns:

- `Student ID` – Unique ID of each student.
- `Name` – Name of the student.
- `Department` – Student's department.
- `Math_Marks` – Marks obtained in Mathematics.
- `Python_Marks` – Marks obtained in Python.
- `OOPS_Marks` – Marks obtained in Object-Oriented Programming.
- `Attendance` – Student's attendance percentage.

The dataset contains 20 student records.

## 5. Key Features

1. Reads student records from a CSV file.
2. Displays student information.
3. Calculates total marks for each student.
4. Calculates average marks for each student.
5. Assigns grades based on average marks.
6. Identifies pass and fail students.
7. Calculates average marks for each subject.
8. Finds the top-performing student.
9. Calculates the overall class average.
10. Saves the analysis results in a new CSV file.

## 6. Project Structure

```text
Student_Performance_Analytics/
│
├── main.py
├── students.csv
├── student_analysis_results.csv
└── README.md
```

**Note:** `student_analysis_results.csv` is generated automatically when the program runs successfully.

## 7. How to Run the Project

### Step 1: Install Python

Install Python on your computer if it is not already installed.

### Step 2: Install Required Libraries

Open the terminal in VS Code and run:

```bash
python -m pip install pandas numpy
```

### Step 3: Prepare the Dataset

Place `students.csv` in the same folder as `main.py`.

### Step 4: Run the Program

Open the terminal in VS Code and execute:

```bash
python main.py
```

### Step 5: View the Results

The program displays student records, total and average marks, grades, pass/fail results, subject-wise averages, the top-performing student, and the overall class average.

It also creates `student_analysis_results.csv` containing the calculated results.

## 8. Concepts Used

This project uses the following beginner-level Python concepts:

- Variables and data types
- `for` loops
- `if-elif-else` conditions
- Basic calculations
- Pandas DataFrames
- NumPy functions
- Reading and writing CSV files

## 9. Expected Outcome

The system helps analyze student academic performance using marks and attendance data. It provides a simple way to identify the top-performing student, compare subject averages, calculate grades, and understand class performance.

## 10. Future Improvements

- Add data visualizations using Matplotlib.
- Generate a more detailed student performance report.
- Add more subjects and student records.
- Improve attendance analysis.

## 11. Conclusion

The Student Performance Analytics System demonstrates how Python, Pandas, and NumPy can be used to process student data and perform basic academic analysis. This project also provides practical experience with loops, conditions, calculations, and CSV file handling.
