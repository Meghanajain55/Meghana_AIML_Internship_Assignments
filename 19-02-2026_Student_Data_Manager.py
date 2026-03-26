# Student Data Manager

# Storing student data (Name : Marks)
students = {
    "Alice": 85,
    "Bob": 92,
    "Charlie": 78,
    "David": 88,
    "Eva": 95
}

# Finding topper
topper = max(students, key=students.get)
top_marks = students[topper]

# Calculating class average
average = sum(students.values()) / len(students)

# Function to assign grade
def assign_grade(marks):
    if marks >= 90:
        return "A"
    elif marks >= 75:
        return "B"
    elif marks >= 50:
        return "C"
    else:
        return "F"

# Printing results
print("--- Student Report ---")

for name, marks in students.items():
    grade = assign_grade(marks)
    print(f"{name}: Marks = {marks}, Grade = {grade}")

print("\nTopper:", topper, "with", top_marks, "marks")
print("Class Average:", round(average, 2))