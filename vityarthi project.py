#taking inputs from user
print("**** STUDENT RESULT PROCESSING SYSTEM ****")
name = input("Enter student name: ")
subjects = ["English", "Maths", "Science", "Social", "Hindi"]
marks = []


for sub in subjects:
    while True:
            mark = int(input(f"Enter marks in {sub}: "))
            if 0 <= mark <= 100:
                marks.append(mark)
                break # jump to the next stbject once input given correctly
            else:
                print(" X--Error--X : Marks must be between 0 and 100.")
       

average = sum(marks) / len(marks)
status = ""
grade = ""

# conditions to calculate grade according to percentage
if any(m < 30 for m in marks):
    status, grade = "Failed", "F"
elif average < 35:
    status, grade = "Failed", "F"
elif average < 55:
    status, grade = "Passed", "D"
elif average < 60:
    status, grade = "Passed", "C"
elif average < 75:
    status, grade = "Passed", "B"
elif average < 90:
    status, grade = "Passed", "A"
elif average <= 100:
    status, grade = "Passed", "A+"
else:
    status, grade = "Invalid", "NA"


# report card - final output 
print("\n****** STUDENT REPORT CARD ******")
print("---------------------------------")
print("Name:",name.capitalize())
print("---------------------------------")

for s, m in zip(subjects, marks):
    print(f"{s}: {m}")

print("---------------------------------")
print(f"Percentage : {average}%")
print(f"Result     : {status}")
print(f"Grade      : {grade}")
print("*********************************")





