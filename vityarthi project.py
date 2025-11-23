#taking marks as a input from user which should be in range 0 - 100

def get_mark(subjects):

    while True:
        mark = int(input(f"Enter marks in {subjects}: "))
        if 0 <= mark <= 100:
            return mark
        else:
            print(" X Marks must be between 0 and 100. Try again.")

# checking the conditions for pass or failed based on average marks

def calculate(avg, marks):
    
    if any(m < 30 for m in marks):
        return "Failed", "F"
    if avg < 35:
        return "Failed", "F"
    elif avg < 55:
        return "Just Pass", "D"
    elif avg < 60:
        return "Pass", "C"
    elif avg < 75:
        return "Average", "B"
    elif avg < 90:
        return "Good", "A"
    elif avg < 100:
        return "Excellent", "A+"
    else:
        return "Invalid", "NA"

# processing for generating final report card

def report_card(name, marks, avg, grade, status):
    
    print("\n======= STUDENT REPORT CARD =======")
    print("-----------------------------------")
    print("Name:", name.capitalize())
    print("-----------------------------------")
    subjects = ["English", "Maths", "Science", "Social", "Hindi"]

    for s, m in zip(subjects, marks):
        print(f"{s}: {m}")

    print("-----------------------------------")
    print(f"Percentage : {avg}%")
    print(f"Result     : {status}")
    print(f"Grade      : {grade}")
    print("===================================")


# taking input from user 

def insert():
    print("==== STUDENT RESULT PROCESSING SYSTEM ====")
    name = input("Enter student name: ")

    subjects = ["English", "Maths", "Science", "Social", "Hindi"]
    marks = [get_mark(s) for s in subjects]

    avg = sum(marks) / len(marks)
    status, grade = calculate(avg, marks)

    report_card(name, marks, avg, grade, status)

insert()



