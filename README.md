# Study Score Calculator v1

## About the Project

Study Score Calculator is a Python project that I created to analyze student exam performance using Pandas and NumPy.

The project calculates student marks, percentages, grades, and pass or fail results. It also analyzes subject-wise class performance and creates student rankings.

The dataset is manually created using Python dictionaries.

## Features

- Create and display student marks data
- Calculate total marks
- Calculate student percentages
- Assign grades based on percentages
- Check student pass and fail status
- Find highest-performing student
- Find lowest-performing student
- Calculate subject-wise class averages
- Identify strongest and weakest subjects
- Calculate class pass percentage
- Rank students based on performance
- Identify students who need improvement
- Perform data validation
- Export reports to CSV files
- Perform automated tests using unittest

## Technologies Used

- Python
- Pandas
- NumPy
- CSV File Handling
- Unittest

## Project Structure

```text
Study-Score-Calculator/
│
├── main.py
├── README.md
├── requirements.txt
├── .gitignore
│
├── tests/
│   └── test_analysis.py
│
└── output/
    ├── student_results.csv
    ├── subject_performance.csv
    ├── student_ranking.csv
    └── students_needing_improvement.csv
```

## Installation

### 1. Clone the Repository

```bash
git clone https://github.com/JS-JUNAIDSALEEM/Study-Score-Calculator.git
```

### 2. Open the Project Folder

```bash
cd Study-Score-Calculator
```

### 3. Install Required Libraries

```bash
pip install -r requirements.txt
```

### 4. Run the Project

```bash
python main.py
```

## Reports

The project generates four CSV reports inside the output folder:

- **student_results.csv:** Contains student marks, percentages, grades, and results.
- **subject_performance.csv:** Shows average, highest, and lowest marks for each subject.
- **student_ranking.csv:** Shows student rankings based on their percentages.
- **students_needing_improvement.csv:** Contains students who need improvement based on their results.

## Data Validation

The project checks student data before performing calculations.

It validates:

- Required columns
- Empty datasets
- Missing values
- Unique student IDs
- Valid student IDs and names
- Numeric marks
- Marks between 0 and 100

## Automated Testing

The project includes 15 automated tests using Python's unittest framework.

These tests check data validation, student IDs, student names, marks, and other important conditions.

To run the tests, use:

```bash
py -m unittest tests/test_analysis.py -v
```

## Passing Criteria

A student must get at least 40 marks in every subject to pass.

Grades are assigned according to the student's percentage.

## What I Learned

While making this project, I practiced:

- Creating and working with Pandas DataFrames
- Performing calculations on student marks
- Using NumPy conditions
- Applying multiple conditions with np.select
- Finding highest and lowest values
- Sorting student records
- Analyzing subject-wise performance
- Working with CSV files
- Performing data validation
- Writing automated tests using unittest

## Future Improvements

- Allow users to enter student marks.
- Add more subjects.
- Store student records permanently.
- Create charts for student performance.
- Add a simple student performance dashboard.

## Author

### Junaid Saleem

- **GitHub:** [JS-JUNAIDSALEEM](https://github.com/JS-JUNAIDSALEEM)
- **LinkedIn:** [Junaid Saleem](https://www.linkedin.com/in/junaid-saleem-developer/)