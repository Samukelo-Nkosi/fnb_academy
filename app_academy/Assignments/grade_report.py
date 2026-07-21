# Collect learner name and marks for three subjects (as floats) using input()
# Calculate the average mark across the three subjects
# Assign a letter grade: A (80+), B (70-79), C (60-69), D (50-59), F (below 50) using if/elif/else
# Assign Pass status if the average is 50 or above, Fail otherwise
# Flag any individual subject mark below 40 as ‘needs intervention’
# Display a formatted report card showing all inputs, the average, the grade, the status, and any intervention flags

students = [
    {'name': 'Samukelo Nkosi', 'maths': 79, 'english': 59, 'science': 69},
    {'name': 'Thabani Zwane', 'maths': 49, 'english': 80, 'science': 59},
    {'name': 'Kelvin Letwaba', 'maths': 50, 'english': 70, 'science': 65},
    {'name': 'Sanele Zulu', 'maths': 60, 'english': 49, 'science': 52},
    {'name': 'Manqoba Nkosi', 'maths': 82, 'english': 62, 'science': 60},
]

results = []
all_marks = []

for student in students:
    math = student['maths']
    english = student['english']
    science = student['science']

    average = (maths + english + science) / 3
    
    if average >= 80:
        grade = "A"
        status = "Pass"

    elif average >= 70 and average <= 79:
        grade = "B"
        status = "Pass"

    elif average >= 60 and average <= 69:
        grade = "C"
        status = "Pass"

    elif average >= 50 and average <= 59:
        grade = "D"
        status = "Pass"

    else:
        grade = "F-Z"
        status = "Fail"

    results.append({
        'name': student['name']
        'average': round(average, 2)
        'grade': grade,
        'status': status
    })    

    all_marks.extend([maths, english, science])

class_average = sum(r['average'] for r in results) / len(results)
highest_mark = max(all_marks)
lowest_mark = min(all_marks)

print("\n-----------------------------------------------")
print("                CLASS GRADE REPORT               ")
print("\n-----------------------------------------------")

for r in results:
    