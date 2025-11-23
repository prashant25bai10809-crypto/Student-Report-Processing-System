# Student-Report-Processing-System

# Student Result Processing System

This project is a simple **Python-based Student Report Card Generator**. It takes marks for five subjects as input, validates them, calculates the average, determines the grade and pass/fail status, and prints a formatted report card.

---

## 📌 Features

* Accepts marks for **English, Maths, Science, Social, Hindi**.
* Validates user input to ensure marks are **between 0 and 100**.
* Checks for **fail/pass conditions**:

  * If any subject mark is below 30 → **Fail**
  * If average is below 35 → **Fail**
* Generates grade based on average:

  | Average Range | Grade          |
  | ------------- | -------------- |
  | < 35          | F (Failed)     |
  | 35–54         | D (Just Pass)  |
  | 55–59         | C (Pass)       |
  | 60–74         | B (Average)    |
  | 75–89         | A (Good)       |
  | 90–100        | A+ (Excellent) |
* Displays a **structured report card**.

---

## 📂 File Structure

```
project/
│-- student_report.py     # Main program file
│-- README.md             # Documentation
```

---

## ▶️ How to Run

1. Ensure Python is installed on your system.
2. Save the code into a file named `student_report.py`.
3. Open a terminal and run:

```
python student_report.py
```

4. Enter student name and marks when prompted.

---

## 🧠 How It Works

### 1. **Input Validation**

The function `get_mark()` ensures marks are integers between 0 and 100.

### 2. **Grade Calculation**

`calculate()` determines the grade and result based on the average and subject marks.

### 3. **Report Card Generation**

`report_card()` prints:

* Student Name
* Marks in each subject
* Percentage
* Result (Pass/Fail)
* Grade

### 4. **Main Driver Function**

`insert()` collects the data and calls all necessary functions.

---

## 📝 Example Output

```
======= STUDENT REPORT CARD =======
-----------------------------------
Name: Rahul
-----------------------------------
English: 85
Maths: 90
Science: 88
Social: 92
Hindi: 80
-----------------------------------
Percentage : 87.0%
Result     : Good
Grade      : A
===================================
```

---

## 🚀 Future Improvements

* Add GUI using Tkinter.
* Export report card as PDF.
* Store multiple students in a file or database.
* Add subject-wise remarks.

---

## 📄 License

This project is free to use and modify for educational purposes.
