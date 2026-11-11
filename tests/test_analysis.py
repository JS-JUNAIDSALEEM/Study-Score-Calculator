
import unittest
import pandas as pd
import subprocess
import sys

from main import data, subjects, validate_data


class TestStudyScoreCalculator(unittest.TestCase):

    def setUp(self):

        self.df = pd.DataFrame(
            {
            "Student_ID": [1, 2],
            "Student_Name": ["Ali", "Sara"],
            "English": [78, 90],
            "Math": [85, 95],
            "Computer": [92, 96],
            "Physics": [74, 88],
            "Chemistry": [80, 91]
        }
        ).astype(object)


# Test 1: Valid Dataset
    def test_valid_data(self):

        results = validate_data(self.df)
        self.assertTrue(all(results.values()))


# Test 2: Empty Dataset
    def test_empty_data(self):

        df = self.df.iloc[0:0]

        results = validate_data(df)
        self.assertFalse(results["Dataset Not Empty"])


# Test 3: Missing Values
    def test_missing_values(self):

        self.df.loc[0, "English"] = None

        results = validate_data(self.df)
        self.assertFalse(results["No Missing Values"])


# Test 4: Duplicate Student IDs
    def test_duplicate_student_ids(self):

        self.df.loc[1, "Student_ID"] = 1

        results = validate_data(self.df)
        self.assertFalse(results["Unique Student IDs"])


# Test 5: Invalid Student ID
    def test_invalid_student_id(self):

        self.df.loc[0, "Student_ID"] = "ABC"

        results = validate_data(self.df)
        self.assertFalse(results["Valid Student IDs"])


# Test 6: Negative Student ID
    def test_negative_student_id(self):

        self.df.loc[0, "Student_ID"] = -1

        results = validate_data(self.df)
        self.assertFalse(results["Valid Student IDs"])


# Test 7: Empty Student Name
    def test_empty_student_name(self):

        self.df.loc[0, "Student_Name"] = ""

        results = validate_data(self.df)
        self.assertFalse(results["Valid Student Names"])


# Test 8: Missing Required Column
    def test_missing_column(self):

        df = self.df.drop(columns=["English"])

        results = validate_data(df)
        self.assertFalse(results["Required Columns"])


# Test 9: Invalid Numeric Marks
    def test_invalid_marks(self):

        self.df.loc[0, "English"] = "Invalid"

        results = validate_data(self.df)
        self.assertFalse(results["Valid Numeric Marks"])


# Test 10: Negative Marks
    def test_negative_marks(self):

        self.df.loc[0, "Math"] = -10

        results = validate_data(self.df)
        self.assertFalse(results["Marks Between 0 and 100"])


# Test 11: Marks Greater Than 100
    def test_marks_above_100(self):

        self.df.loc[0, "Computer"] = 110

        results = validate_data(self.df)
        self.assertFalse(results["Marks Between 0 and 100"])


# Test 12: Decimal Student ID
    def test_decimal_student_id(self):

        self.df.loc[0, "Student_ID"] = 1.5

        results = validate_data(self.df)
        self.assertFalse(results["Valid Student IDs"])


# Test 13: Whitespace Student Name
    def test_whitespace_student_name(self):

        self.df.loc[0, "Student_Name"] = "   "

        results = validate_data(self.df)
        self.assertFalse(results["Valid Student Names"])


# Test 14: Original Student Dataset
    def test_original_student_data(self):

        df = pd.DataFrame(data)

        results = validate_data(df)

        self.assertTrue(all(results.values()))
        self.assertEqual(len(df), 10)
        self.assertEqual(len(subjects), 5)


# Test 15: Import Does Not Run Main Program
    def test_import_does_not_run_program(self):

        result = subprocess.run(
            [sys.executable, "-c", "import main"],
            capture_output=True,
            text=True
        )

        self.assertEqual(result.returncode, 0)
        self.assertEqual(result.stdout, "")


if __name__ == "__main__":
    unittest.main()