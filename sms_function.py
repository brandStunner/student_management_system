
student_directory = {}

def main():
    while True:
        print(F"=" * 40)
        add_new_record = input("Do you want to add a new record? Press enter to add or q to quit ")
        if add_new_record.lower() =="q":
            break
        name = input("What's your name: ")
       
        age = int(input("What's your age: "))
       
        subject = input("What subject are you studying: ")
      
        grade = float(input("what grade did you obtain: "))
   
        add_new_student(name,age,subject,grade)
    
    display_record = input("Press enter to view student records or q to skip it? ")
    if display_record.lower() != "q":
        display_records()
    display_scholars = input("Press enter to view scholarship winning students or q to skip it? ")
    if display_scholars.lower() != "q":
        deserve_scholarship()

    display_class_average = input("Press enter to view class average score or q to skip it? ")
    if display_class_average.lower() != "q":
        class_average()

def add_new_student(name,age,subject,grade):
    student_profile = {}
    student_profile[name] = {"age": age,"subject": subject,"grade": grade}
    student_directory.update(student_profile)
    return student_directory
    

def display_records():
    print("Student Records: ")
    for name, values in student_directory.items():
        print(f"Name: {name}")
        print(f"Age: {values['age']}")
        print(f"Subject: {values['subject']}")
        print(f"Grade: {values['grade']} \n")

def deserve_scholarship():
    scholarship_age = 14
    scholarship_grade = 70
    for name,values in student_directory.items():
        age = values['age']
        grade = values['grade']
        if grade >= scholarship_grade and age >= scholarship_age:
            print(f"{name} is {age} years and had {grade} so deserves scholarship")

def class_average():
    total_score = 0
    total_count = 0
    for name,values in student_directory.items():
        grade = values['grade']
        total_score += grade
        total_count += 1
    grade_average = total_score / total_count
    print(f"Class average: {grade_average: .2f}%")
    return(grade_average)

# add_new_student("Kofi",21,"python",98)
# display_record()
if __name__ == "__main__":
    main()