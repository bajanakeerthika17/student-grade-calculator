# ==========================================================
# Project Name : Student Grade Calculator
# Author       : Beginner Python Developer
# Description  : A simple and clean Python project to calculate 
#                total marks, percentage, and grade for 5 subjects.
# ==========================================================

# ----------------------------------------------------------
# Step 1: Display Welcome Banner & Ask for Student Name
# ----------------------------------------------------------
print("=" * 48)
print("         STUDENT GRADE CALCULATOR SYSTEM        ")
print("=" * 48)

# Input student name
student_name = input("Enter student name: ")

print("\nPlease enter marks obtained (out of 100) for 5 subjects:")

# ----------------------------------------------------------
# Step 2: Input marks for 5 subjects
# ----------------------------------------------------------
# float() allows entering both whole numbers (e.g., 85) and decimals (e.g., 85.5)
subject1 = float(input("1. Enter marks for English         : "))
subject2 = float(input("2. Enter marks for Mathematics     : "))
subject3 = float(input("3. Enter marks for Science         : "))
subject4 = float(input("4. Enter marks for Social Studies  : "))
subject5 = float(input("5. Enter marks for Computer Science: "))

# ----------------------------------------------------------
# Step 3: Calculate Total Marks & Average Percentage
# ----------------------------------------------------------
# Maximum marks for each subject = 100. For 5 subjects = 500.
total_marks = subject1 + subject2 + subject3 + subject4 + subject5
max_marks = 500.0

# Calculate average percentage: (total_marks / max_marks) * 100
percentage = (total_marks / max_marks) * 100

# ----------------------------------------------------------
# Step 4: Determine Grade (A, B, C, D or Fail)
# ----------------------------------------------------------
# Grading Criteria:
# 90% and above  --> Grade A
# 75% to 89.99%  --> Grade B
# 60% to 74.99%  --> Grade C
# 40% to 59.99%  --> Grade D
# Below 40%      --> Fail

if percentage >= 90:
    grade = "A"
    status = "Passed with Distinction"
elif percentage >= 75:
    grade = "B"
    status = "Passed with First Class"
elif percentage >= 60:
    grade = "C"
    status = "Passed with Second Class"
elif percentage >= 40:
    grade = "D"
    status = "Passed"
else:
    grade = "Fail"
    status = "Needs Improvement"

# ----------------------------------------------------------
# Step 5: Display the Final Result Clearly
# ----------------------------------------------------------
print("\n" + "=" * 48)
print("               STUDENT REPORT CARD              ")
print("=" * 48)
print(f" Student Name        : {student_name}")
print("-" * 48)
print(" Subject-wise Marks Breakdown:")
print(f"  - English          : {subject1:.1f} / 100")
print(f"  - Mathematics      : {subject2:.1f} / 100")
print(f"  - Science          : {subject3:.1f} / 100")
print(f"  - Social Studies   : {subject4:.1f} / 100")
print(f"  - Computer Science : {subject5:.1f} / 100")
print("-" * 48)
print(f" Total Marks Obtained: {total_marks:.1f} / {int(max_marks)}")
print(f" Average Percentage  : {percentage:.2f}%")
print(f" Final Grade         : Grade {grade}" if grade != "Fail" else f" Final Grade         : {grade}")
print(f" Result Status       : {status}")
print("=" * 48)

# Friendly encouragement message
if grade == "Fail":
    print(" Advice: Don't give up! Consistent practice brings success.")
else:
    print(f" Well done, {student_name}! Keep aiming high!")
print("=" * 48)
