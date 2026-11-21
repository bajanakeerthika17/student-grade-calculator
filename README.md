# Student Grade Calculator 🎓

A clean, beginner-friendly Python Mini Project that calculates a student's total marks, average percentage, and final grade based on marks obtained in 5 subjects.

---

## 📋 Features

- 👤 **Student Name Input**: Personalizes the final report card.
- 📚 **5 Subjects Marks Entry**: Accepts marks (supports whole numbers and decimals like `85.5`).
- ➕ **Total Marks Calculation**: Sums up marks across all 5 subjects out of 500.
- 📊 **Average Percentage**: Calculates accurate percentage formatted to 2 decimal places.
- 🏅 **Grade Determination**: Automatically assigns grades based on standard academic performance criteria (`A`, `B`, `C`, `D`, or `Fail`).
- 🖨️ **Neat Report Card**: Prints a clean, formatted terminal report card.

---

## 🎯 Grading System

| Percentage Range | Grade | Result Status |
| :--- | :---: | :--- |
| **90% - 100%** | **A** | Passed with Distinction |
| **75% - 89.99%** | **B** | Passed with First Class |
| **60% - 74.99%** | **C** | Passed with Second Class |
| **40% - 59.99%** | **D** | Passed |
| **Below 40%** | **Fail** | Needs Improvement |

---

## 🧠 Python Concepts Used (Beginner-Friendly)

1. **Variables & Data Types**: Storing strings (`str`) for names, and floating-point numbers (`float`) for marks.
2. **User Input (`input()`)**: Interactively collecting information from the user.
3. **Type Casting (`float()`)**: Converting raw string inputs into numeric format so mathematical calculations can be performed.
4. **Arithmetic Operators (`+`, `/`, `*`)**:
   - `total_marks = subject1 + subject2 + ...`
   - `percentage = (total_marks / max_marks) * 100`
5. **Conditional Branching (`if`, `elif`, `else`)**: Evaluating which grade bucket the student falls into.
6. **Formatted Strings (`f-strings`)**: Neat alignment and rounding decimals using syntax like `{percentage:.2f}%`.

---

## 🚀 How to Run in Visual Studio Code (VS Code)

Follow these simple steps to run this project in **VS Code**:

### Step 1: Open the Project Folder in VS Code
1. Open **Visual Studio Code**.
2. Click on **File** > **Open Folder...** (or press `Ctrl + K, Ctrl + O`).
3. Select this project folder (`module 2`).

### Step 2: Ensure Python Extension is Installed
1. In VS Code, click the **Extensions** icon on the left sidebar (or press `Ctrl + Shift + X`).
2. Search for **Python** (by Microsoft) and make sure it is installed and enabled.

### Step 3: Open `grade_calculator.py`
1. In the file explorer on the left, click on `grade_calculator.py` to open the file.

### Step 4: Run the Script
You can run the script using either of these two methods:

- **Method A (Easiest - Run Button):**
  - Look at the top-right corner of the editor window.
  - Click the **▶ (Play)** button labeled *Run Python File*.
  - A terminal will open at the bottom and ask for input.

- **Method B (Using the Integrated Terminal):**
  - Open the terminal in VS Code: Press ``Ctrl + ` `` (Backtick) or go to **Terminal** > **New Terminal**.
  - Type the following command and press **Enter**:
    ```bash
    python grade_calculator.py
    ```
  - *(Note: If your system uses `py`, run `py grade_calculator.py`)*.

### Step 5: Enter the Required Inputs
Follow the prompts shown in the terminal:
1. Type the student's name and hit **Enter**.
2. Enter the marks for each of the 5 subjects (English, Mathematics, Science, Social Studies, Computer Science) and hit **Enter** after each subject.
3. View the generated report card!

---

## 💻 Sample Program Run

```text
================================================
         STUDENT GRADE CALCULATOR SYSTEM        
================================================
Enter student name: Sophia

Please enter marks obtained (out of 100) for 5 subjects:
1. Enter marks for English         : 92
2. Enter marks for Mathematics     : 95.5
3. Enter marks for Science         : 89
4. Enter marks for Social Studies  : 91
5. Enter marks for Computer Science: 97.5

================================================
               STUDENT REPORT CARD              
================================================
 Student Name        : Sophia
------------------------------------------------
 Subject-wise Marks Breakdown:
  - English          : 92.0 / 100
  - Mathematics      : 95.5 / 100
  - Science          : 89.0 / 100
  - Social Studies   : 91.0 / 100
  - Computer Science : 97.5 / 100
------------------------------------------------
 Total Marks Obtained: 465.0 / 500
 Average Percentage  : 93.00%
 Final Grade         : Grade A
 Result Status       : Passed with Distinction
================================================
 Well done, Sophia! Keep aiming high!
================================================
```

---

## 📁 Project Structure

```text
module 2/
│
├── grade_calculator.py    # Main Python script with line-by-line comments
└── README.md              # Project documentation and guide
```
