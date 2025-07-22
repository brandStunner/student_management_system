
print("Welcome! Fill in the following details to register")
student_directory = {}

# Ask student details
name = input("Enter your full name: ").strip().capitalize()
age = int(input("Enter your age: "))
subject = input("Enter your subject: ").strip().capitalize()
grade = float(input("Enter your grade: "))

student_profile = {
    "name": name,
    "age": age,
    "subject": subject,
    "grade": grade
}

student_key = f"student_{len(student_directory)+1}"
student_directory[student_key] = student_profile
print(student_directory)

print("Press enter to add another student or q to stop")
another_student = input("Do you want to add another student? ").lower()

if another_student != "q":
    name = input("Enter your full name: ").strip().capitalize()
    age = int(input("Enter your age: "))
    subject = input("Enter your subject: ").strip().capitalize()
    grade = float(input("Enter your grade: "))
    
    student_profile = {
        "name": name,
        "age": age,
        "subject": subject,
        "grade": grade
    }
    
    student_key = f"student_{len(student_directory)+1}"
    student_directory[student_key] = student_profile
    print(student_directory)
    
    another_student = input("Do you want to add another student? ").lower()
    if another_student != "q":
        name = input("Enter your full name: ").strip().capitalize()
        age = int(input("Enter your age: "))
        subject = input("Enter your subject: ").strip().capitalize()
        grade = float(input("Enter your grade: "))
        
        student_profile = {
            "name": name,
            "age": age,
            "subject": subject,
            "grade": grade
        }
        
        student_key = f"student_{len(student_directory)+1}"
        student_directory[student_key] = student_profile
        print(student_directory)
        
        another_student = input("Do you want to add another student? ").lower()
        if another_student != "q":
            name = input("Enter your full name: ").strip().capitalize()
            age = int(input("Enter your age: "))
            subject = input("Enter your subject: ").strip().capitalize()
            grade = float(input("Enter your grade: "))
            
            student_profile = {
                "name": name,
                "age": age,
                "subject": subject,
                "grade": grade
            }
            
            student_key = f"student_{len(student_directory)+1}"
            student_directory[student_key] = student_profile
            print(student_directory)

            another_student = input("Do you want to add another student? ").lower()
            if another_student != "q":
                name = input("Enter your full name: ").strip().capitalize()
                age = int(input("Enter your age: "))
                subject = input("Enter your subject: ").strip().capitalize()
                grade = float(input("Enter your grade: "))
                
                student_profile = {
                    "name": name,
                    "age": age,
                    "subject": subject,
                    "grade": grade
                }
                
                student_key = f"student_{len(student_directory)+1}"
                student_directory[student_key] = student_profile
                print(student_directory)

# Display student information
print("\n--- STUDENT DIRECTORY ---")
print(student_directory)

# Calculate grades and average (improved version)
print("\n--- GRADE ANALYSIS ---")
all_grades = []

# Collect grades only for existing students (no "not available" messages)
if "student_1" in student_directory:
    all_grades.append(student_directory["student_1"]["grade"])
if "student_2" in student_directory:
    all_grades.append(student_directory["student_2"]["grade"])
if "student_3" in student_directory:
    all_grades.append(student_directory["student_3"]["grade"])
if "student_4" in student_directory:
    all_grades.append(student_directory["student_4"]["grade"])
if "student_5" in student_directory:
    all_grades.append(student_directory["student_5"]["grade"])

print(f"All grades: {all_grades}")

if len(all_grades) > 0:
    average_grade = sum(all_grades) / len(all_grades)
    print(f"Average grade: {average_grade:.2f}")
    
    # Grade analysis
    if average_grade >= 80:
        print("Class performance: Excellent!")
    elif average_grade >= 70:
        print("Class performance: Good")
    elif average_grade >= 60:
        print("Class performance: Average")
    else:
        print("Class performance: Needs improvement")
else:
    print("No students to analyze")

# Scholarship eligibility (improved)
print("\n--- SCHOLARSHIP ELIGIBILITY ---")
scholarship_grade = 70
minimum_scholarship_age = 14
scholarship_count = 0

if "student_1" in student_directory:
    student_1 = student_directory["student_1"]
    if student_1["grade"] >= scholarship_grade and student_1["age"] >= minimum_scholarship_age:
        print(f"{student_1['name']} deserves scholarship (Grade: {student_1['grade']}, Age: {student_1['age']})")
        scholarship_count += 1

if "student_2" in student_directory:
    student_2 = student_directory["student_2"]
    if student_2["grade"] >= scholarship_grade and student_2["age"] >= minimum_scholarship_age:
        print(f"{student_2['name']} deserves scholarship (Grade: {student_2['grade']}, Age: {student_2['age']})")
        scholarship_count += 1

if "student_3" in student_directory:
    student_3 = student_directory["student_3"]
    if student_3["grade"] >= scholarship_grade and student_3["age"] >= minimum_scholarship_age:
        print(f"{student_3['name']} deserves scholarship (Grade: {student_3['grade']}, Age: {student_3['age']})")
        scholarship_count += 1

if "student_4" in student_directory:
    student_4 = student_directory["student_4"]
    if student_4["grade"] >= scholarship_grade and student_4["age"] >= minimum_scholarship_age:
        print(f" {student_4['name']} deserves scholarship (Grade: {student_4['grade']}, Age: {student_4['age']})")
        scholarship_count += 1

if "student_5" in student_directory:
    student_5 = student_directory["student_5"]
    if student_5["grade"] >= scholarship_grade and student_5["age"] >= minimum_scholarship_age:
        print(f" {student_5['name']} deserves scholarship (Grade: {student_5['grade']}, Age: {student_5['age']})")
        scholarship_count += 1

print(f"\nTotal scholarship recipients: {scholarship_count}")

# Additional statistics
print("\n--- ADDITIONAL STATS ---")
total_students = len(student_directory)
print(f"Total students registered: {total_students}")

if total_students > 0:
    scholarship_percentage = (scholarship_count / total_students) * 100
    print(f"Scholarship rate: {scholarship_percentage:.1f}%")