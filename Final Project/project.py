import os
import csv
import sys
import uuid

file_name = "students.csv"
field_names = ["Name", "Roll", "Grade", "ID"]


def main():
    #Main menu for student information system
    os.system('cls' if os.name == 'nt' else 'clear')
    print("""
    --------------------------------
    Student Information Management
    --------------------------------
    1. Add Student Info
    2. Search Student Info
    3. Edit Student Info
    4. Remove Student Info
    5. Show All Students Info
    6. remove All student Info
    7. Exit
    --------------------------------""")

    # Menu options calling
    {
    1: add_student,
    2: search_student,
    3: edit_student,
    4: delete_student,
    5: display_all,
    6: delete_all,
    7: exit_program
    }[get_option()]()


def get_option():
    #Get valid menu selection from user
    while True:
        choice = input("\n==> Choose an option from 1-7: ").strip()
        if choice in ['1','2','3','4','5','6','7']:
            return int(choice)
        print("--- Invalid input! Choose a digit from 1 to 7 ---")



def add_student():
    #Add student information(Name, Grade, Roll, Unique ID) to the csv file
    while True:
        print("\n\n--- Left Name blank for Exit ---")
        name = input("==> Type student Name: ").strip()
        if not name:
            main()
        roll = input("==> Type student Roll: ").strip()
        grade = input("==> Type student Grade: ").strip()
        print(create_ID(name, roll, grade))


def search_student():
    #Search for a student in the csv file by ID or Name and Roll(show multiple result if found)
    print("\n\n--- Left ID blank for searching by Name and Roll ---")
    ID = input("\nEnter Student ID: ").strip()
    if ID:
        match(ID=ID)
    else:
        name = input("Enter student Name: ").strip()
        grade = input(f"Enter {name}'s Grade: ").strip()
        match(name=name, grade=grade)
    if not input("\n--- Press Enter for main Menu ---"):
        main()


def edit_student():
    #Edit a student information in csv file
    print("\n\n--- Left ID blank for editing by Grade and Roll ---")
    ID = input("\nEnter Student ID: ").strip()
    if ID:
        edit(ID=ID)
    else:
        grade = input("Enter student Grade: ").strip()
        roll = input("Enter student Roll: ").strip()
        edit(grade=grade, roll=roll)
    if not input("\n--- Press Enter for main Menu ---"):
        main()


def delete_student():
    #remove a student information from csv file including ID
    print("\n\n--- Left ID blank for deleting by Grade and Roll ---")
    ID = input("\nEnter Student ID: ").strip()
    if ID:
        delete(ID=ID)
    else:
        grade = input("Enter student Grade: ").strip()
        roll = input("Enter student Roll: ").strip()
        delete(grade=grade, roll=roll)
    if not input("\n--- Press Enter for main Menu ---"):
        main()


def display_all():
    #Print all the student information saved in csv file
    all()
    if not input("\n---Press Enter for main Menu---"):
        main()


def delete_all():
    #remove all student information by deleting the entire csv file
    check_file()
    os.remove("students.csv")
    print("\n===> All student information deleted successfully!")
    if not input("\n---Press Enter for main Menu---"):
        main()


def exit_program():
    #Cleanly exit the program
    print("\n\n--- Exited Successfully ---\n\n")
    sys.exit()


def check_file():
    #Check in the folder for the csv file, if not found then it will creat one
    if not os.path.exists("students.csv"):
        with open(file_name, mode='w', newline='') as file:
            write = csv.DictWriter(file, fieldnames=field_names)
            write.writeheader()


def create_ID(name, roll, grade):
    #Creat a unique ID number for a student starts with his grade and roll(the once which is used first time)
    check_file()
    with open(file_name, mode="r") as file:
        read = list(csv.DictReader(file))
        for row in read:
            if row["Roll"] == roll and row["Grade"] == grade:
                return f"\n===> Student not added!\n===> A student named {row["Name"]} with Roll {roll} already exists in Grade {grade}"

    # If no duplicate found, creat an ID and add student in file
    ID = grade + roll + str(uuid.uuid4())[:4]
    with open(file_name, mode="a", newline='') as file:
        write = csv.DictWriter(file, fieldnames=field_names)
        write.writerow({
            "Name": name,
            "Roll": roll,
            "Grade": grade,
            "ID": ID
        })
    return f"\n===> Student added successfully!\n===> Student Id for {name}: {ID}"


def match(grade=None, name=None, ID=None):
    #Find for a match for student in csv file
    check_file()
    with open(file_name, mode="r") as file:
        read = list(csv.DictReader(file))  # Read all students

    # Determine search criteria
    if ID:
        result = [s for s in read if s["ID"] == ID]
    elif name and grade:
        result = [s for s in read if (s["Name"] == name) and (s["Grade"] == grade)]
    else:
        result = []  # Invalid search parameters

    # Handle results PROPERLY INDENTED
    if result:
        print(f"\n===> {len(result)} student(s) found.")
        for index, student in enumerate(result, start=1):
            print(f"\n{index}. Name  : {student["Name"]}")
            print(f"   Grade : {student["Grade"]}")
            print(f"   Roll  : {student["Roll"]}")
            print(f"   ID    : {student["ID"]}")
    else:
        print("===> No student found!")


def edit(ID=None, grade=None, roll=None):
    #Edit a student information in csv file
    check_file()
    with open(file_name, mode="r") as file:
        read = list(csv.DictReader(file))
    if ID:
        target_student = [s for s in read if s["ID"] == ID]
        if not target_student:
            print("\n===> No student found!")
            return None
        updated_students = [s for s in read if s["ID"] != ID]
        with open(file_name, mode="w", newline='') as file:
            write = csv.DictWriter(file, fieldnames=field_names)
            write.writeheader()
            write.writerows(updated_students)
            write.writerow({
            "Name": input("\n--- Left blank for keep unchanged ---\n===> Type new Name: ") or target_student[0]["Name"],
            "Roll": input("\n--- Left blank for keep unchanged ---\n===> Type new Roll: ") or target_student[0]["Roll"],
            "Grade": input("\n--- Left blank for keep unchanged ---\n===> Type new Grade: ") or target_student[0]["Grade"],
            "ID": ID
            })
        print("\n===> Student edited successfully")

    elif grade and roll:
        target_student = [s for s in read if (s["Grade"] == grade and s["Roll"] == roll)]
        updated_students = [s for s in read if not (s["Grade"] == grade and s["Roll"] == roll)]
        with open(file_name, mode="w", newline='') as file:
            write = csv.DictWriter(file, fieldnames=field_names)
            write.writeheader()
            write.writerows(updated_students)
            write.writerow({
            "Name": input("\n--- Left blank for keep unchanged ---\nEnter new Name: ") or target_student[0]["Name"],
            "Roll": input("\n--- Left blank for keep unchanged ---\nEnter new Roll: ") or target_student[0]["Roll"],
            "Grade": input("\n--- Left blank for keep unchanged ---\nEnter new Grade: ") or target_student[0]["Grade"],
            "ID": target_student[0]["ID"]
            })
        print("\n===> Student edited successfully" if target_student else "\n===> No student found!")


def delete(ID=None, grade=None, roll=None):
    #remove a student information from csv file
    check_file()
    remove = False
    with open(file_name, mode="r") as file:
        read = list(csv.DictReader(file))

    # Find and remove the student
    if ID:
        updated_students = [s for s in read if s["ID"] != ID]
        with open(file_name, mode="w", newline='') as file:
            write = csv.DictWriter(file, fieldnames=field_names)
            write.writeheader()
            write.writerows(updated_students)
        if len(updated_students) != len(read):
            remove = True

    elif grade and roll:
        updated_students = [s for s in read if not (s["Grade"] == grade and s["Roll"] == roll)]
        with open(file_name, mode="w", newline='') as file:
            writer = csv.DictWriter(file, fieldnames=field_names)
            writer.writeheader()
            writer.writerows(updated_students)
        if len(updated_students) != len(read):
            remove = True

    print("\n===> Student Removed successfully" if remove else "\n===> No student found!")


def all():
    #The function which is called by display_all() to print all the student information
    check_file()
    with open(file_name, mode="r") as file:
        read = list(csv.DictReader(file))
    print(f"\n\n===> Total {len(read)} student(s)")
    for index, student in enumerate(read, start=1):
        print(f"\n{index}. Name  : {student["Name"]}")
        print(f"   Grade : {student["Grade"]}")
        print(f"   Roll  : {student["Roll"]}")
        print(f"   ID    : {student["ID"]}")


if __name__ == "__main__":
    main()
