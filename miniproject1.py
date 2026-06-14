#Student Management System

students = {}  #empty dictionary

#add student
def add_student():
    roll=int(input("enter the roll number:"))
    if roll in students:
        print("student already exists")
    else:
        name = input("enter name:")
        age  = int(input("enter Age"))
        marks = float(input("enter marks"))
        students[roll] = {
            "name" : name,
            "age" : age,
            "marks" : marks
        }
    print("students succesfully added")

#update marks
def update_marks():
    roll=int(input("enter the roll number:"))
    if roll in students:
        marks= float(input("enter new marks"))
        students[roll]["marks"]= marks
        print("marks updated")
    else:
        print("Student NOT FOUND")

#search student
def search_student():
    roll=int(input("enter the roll number"))
    if roll in students:
        print("\n Students Details")
        print("Roll no." , roll)
        print("Name:" , students[roll]["name"])
        print("Age:" , students[roll]["age"])
        print("Marks:" , students[roll]["marks"])
    else:
        print("Student NOT FOUND")

#delete student
def delete_student():
    roll= int(input("enter the roll number:"))
    if roll in students:
        del students[roll]
        print("student succesfully deleted")
    else:
        print("Student NOT FOUND")


#display all students
def display_students():
    if not students:
        print("NO student record")
    else:
        print("All Students record")
        print("-" * 40)
        for roll, details in students.items():
            print(f"Roll no:{roll}")
            print(f"Name:{details['name']}")
            print(f"Age:{details['age']}")
            print(f"Marks:{details['marks']}")
            print("-" * 40)
#main menu

while True:
    print("\n===== STUDENT MANAGEMENT SYSTEM =====")
    print("1. Add Student")
    print("2. Update Marks")
    print("3. Search Student")
    print("4. Delete Student")
    print("5. Display All Students")
    print("6. Exit")

    choice = input("Enter Your Choice: ")

    if choice == "1":
        add_student()
    elif choice == "2":
        update_marks()
    elif choice == "3":
        search_student()
    elif choice == "4":
        delete_student()
    elif choice == "5":
        display_students()
    elif choice == "6":
        print("Thank You!")
        break
    else:
        print("Invalid Choice! Please Try Again.")

        