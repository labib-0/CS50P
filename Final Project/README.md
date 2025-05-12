# Student Information Management System
## Video Demo: https://youtu.be/8PWYQKZ0h24
## Description:

This is a command-line Student Information Management System written in Python. It offers functionality to manage student records stored in a CSV file. Users can add, search, edit, delete, and print student records. Each student record contains the Name, Roll, Grade, and an automatically created unique ID when a new student is added. The program focuses on simplicity and usability and is therefore the ideal tool for school administrators or teachers who need to make a minimalist database of students.

The project is implemented with a main function and multiple helper functions on the same level of indentation. Some of the key functions are:

- **`add_student()`**: Prompts the user to enter a new student's details and adds the record to the CSV file. At first it take name, roll and grade as user input then it call a function called `create_ID()`. This function will check if the same grade and roll exist in the csv file or not. If not then it genarates a unique student ID and then adds the following informations name, roll, grade, ID to the **students.csv** file.

- **`search_student()`**: Allows searching for a student either by a unique ID or by their Name and Roll combination.

- **`edit_student()`**: Provides the option to edit existing student records. If no student found as per user inputed roll and grade or ID, it will display a messege that no student found.

- **`delete_student()`**: Removes a student record based on ID or grade and roll.
- **`display_all()`**: Displays all the student records currently saved. It will also show the total number of students that have been saved in the csv file.

- **`delete_all()`**: Deletes all student records by removing the CSV file.
- **`create_ID()`**: Generates a unique ID for each student by combining the student's Grade, Roll, and a randomly generated ID number.

- **`check_file()`**: Checks if **students.csv** exist or not. If not then create one and add a header row that includes Name, Roll, Grade, ID in the csv file.

There are other functions like `get_option`, `match()`, `edit()`, `delete()`, and `all()` to enable various operations.
The ID generation using unique IDs makes every student record identifiable.
## Requirments:
The system relies on Python modules like os, csv, sys, and uuid as they are built-in, so no external libraries are needed for the core function. Testing is performed using pytest for some of the core functions.

## File Structure:
- **`project.py`**: Main program file containing the `main` function and all helper functions.
- **`students.csv`**: CSV file that stores student records (auto-created on first run).
- **`test_project.py`**: Contains minimal pytest functions to test core functionalities of the project.
- **`requirements.txt`**: Currently, it only list `pytest` for testing purposes.

## Authors
### Hi, I'm Labib! 👋

- github [@labib-0](https://github.com/labib-0)
- edx [@mdlhjahin](https://profile.edx.org/u/mdlhjahin)
- X [labib_hasann](https://x.com/labib_hasann)
