import pandas as pd
import numpy as np
import os

# Create output folder
os.makedirs("output", exist_ok=True)

# Student marks data
data = [
    {"Student_ID": 1,   "Student_Name": "Ali",     "English": 78,   "Math": 85,   "Computer": 92,   "Physics": 74,   "Chemistry": 80},
    {"Student_ID": 2,   "Student_Name": "Ahmed",   "English": 65,   "Math": 72,   "Computer": 80,   "Physics": 68,   "Chemistry": 75},
    {"Student_ID": 3,   "Student_Name": "Sara",    "English": 90,   "Math": 95,   "Computer": 96,   "Physics": 88,   "Chemistry": 91},
    {"Student_ID": 4,   "Student_Name": "Hassan",  "English": 55,   "Math": 48,   "Computer": 70,   "Physics": 52,   "Chemistry": 60},
    {"Student_ID": 5,   "Student_Name": "Ayesha",  "English": 82,   "Math": 89,   "Computer": 94,   "Physics": 85,   "Chemistry": 87},
    {"Student_ID": 6,   "Student_Name": "Usman",   "English": 45,   "Math": 38,   "Computer": 65,   "Physics": 42,   "Chemistry": 50},
    {"Student_ID": 7,   "Student_Name": "Fatima",  "English": 88,   "Math": 92,   "Computer": 90,   "Physics": 86,   "Chemistry": 89},
    {"Student_ID": 8,   "Student_Name": "Bilal",   "English": 70,   "Math": 62,   "Computer": 75,   "Physics": 58,   "Chemistry": 66},
    {"Student_ID": 9,   "Student_Name": "Zain",    "English": 35,   "Math": 45,   "Computer": 50,   "Physics": 30,   "Chemistry": 40},
    {"Student_ID": 10,  "Student_Name": "Maham",   "English": 95,   "Math": 98,   "Computer": 97,   "Physics": 93,   "Chemistry": 96}
]

# Create DataFrame
df = pd.DataFrame(data)

subjects = ["English", "Math", "Computer", "Physics", "Chemistry"]

print("\n========== STUDENT MARKS DATA ==========")
print(df.to_string(index=False))


# 1. Calculate total marks

df["Total_Marks"] = df[subjects].sum(axis=1)

df["Percentage"] = (df["Total_Marks"] / (len(subjects) * 100)) * 100

# Check student pass or fail.
df["Result"] = np.where((df[subjects] >= 40).all(axis=1), "Pass", "Fail")

print("\n========== STUDENT RESULTS ==========")
print(df[["Student_Name", "Total_Marks", "Percentage", "Result"]].to_string(index=False))


# 2. Calculate grades

df["Grade"] = np.select(
    [
        df["Result"] == "Fail",
        df["Percentage"] >= 90,
        df["Percentage"] >= 80,
        df["Percentage"] >= 70,
        df["Percentage"] >= 60,
        df["Percentage"] >= 50
    ],
    [
        "F",
        "A+",
        "A",
        "B",
        "C",
        "D"
    ],
    default="F"
)

print("\n========== GRADE REPORT ==========")
print(df[["Student_Name", "Percentage", "Grade"]].to_string(index=False))


# 3. Find highest and lowest performing students

top_student = df.loc[df["Percentage"].idxmax()]
lowest_student = df.loc[df["Percentage"].idxmin()]

print("\n========== STUDENT PERFORMANCE ==========")

print("Highest Performing Student:", top_student["Student_Name"])
print("Highest Percentage:", round(top_student["Percentage"], 2))

print("Lowest Performing Student:", lowest_student["Student_Name"])
print("Lowest Percentage:", round(lowest_student["Percentage"], 2))


# 4. Subject-wise class performance

print("\n========== SUBJECT PERFORMANCE ==========")

subject_summary = pd.DataFrame({
    "Subject": subjects,
    "Class_Average": [df[subject].mean() for subject in subjects],
    "Highest_Marks": [df[subject].max() for subject in subjects],
    "Lowest_Marks": [df[subject].min() for subject in subjects]
})

subject_summary["Class_Average"] = subject_summary["Class_Average"].round(2)
print(subject_summary.to_string(index=False))


# 5. Find strongest and weakest subjects

strongest_subject = subject_summary.loc[subject_summary["Class_Average"].idxmax()]
weakest_subject = subject_summary.loc[subject_summary["Class_Average"].idxmin()]

print("\nStrongest Subject:", strongest_subject["Subject"])
print("Average Marks:", strongest_subject["Class_Average"])

print("\nWeakest Subject:", weakest_subject["Subject"])
print("Average Marks:", weakest_subject["Class_Average"])


# 6. Count passed and failed students

print("\n========== CLASS RESULT SUMMARY ==========")

passed_students = (df["Result"] == "Pass").sum()
failed_students = (df["Result"] == "Fail").sum()

print("Total Students:", len(df))
print("Passed Students:", passed_students)
print("Failed Students:", failed_students)

pass_percentage = (passed_students / len(df)) * 100

print("Class Pass Percentage:", round(pass_percentage, 2), "%")


# 7. Student performance ranking

print("\n========== STUDENT RANKING ==========")

ranking = df.sort_values( by="Percentage", ascending=False).copy()
ranking["Rank"] = range(1, len(ranking) + 1)

print(ranking[["Rank", "Student_Name", "Percentage", "Grade"]].to_string(index=False))


# 8. Find students who need improvement

print("\n========== STUDENTS NEEDING IMPROVEMENT ==========")

improvement_students = df[(df["Percentage"] < 60) | (df["Result"] == "Fail")]

if improvement_students.empty:
    print("No students need improvement.")
else:
    print(improvement_students[["Student_Name", "Percentage", "Result"]].to_string(index=False))


# 9. Basic data validation

print("\n========== DATA VALIDATION ==========")

print("Student IDs are unique:", df["Student_ID"].is_unique)
print("Marks are between 0 and 100:", ((df[subjects] >= 0) & (df[subjects] <= 100)).all().all())
print("No missing values:", df.isnull().sum().sum() == 0)


# 10. Export reports

df.to_csv("output/student_results.csv", index=False)
subject_summary.to_csv("output/subject_performance.csv", index=False)
ranking.to_csv("output/student_ranking.csv", index=False)
improvement_students.to_csv("output/students_needing_improvement.csv", index=False)

print("\n========== PROJECT COMPLETED ==========")
print("All student performance reports are saved in output folder.")