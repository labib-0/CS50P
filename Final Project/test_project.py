from project import create_ID, check_file, file_name
import os
import csv

# test_project will delete the data of the csv file for checking purpose which will not be recoverd after.

# Remove test file if it exists, it will delete the file.
def setup_module(module):
    if os.path.isfile(file_name):
        os.remove(file_name)

# checking if name is in the message
def test_add_student():
    msg = create_ID("Labib", "01", "10")
    assert "Student added successfully" in msg
    assert "Labib" in msg

# same roll and grade will be rejected
def test_no_duplicate():
    create_ID("Jack", "22", "9")
    msg = create_ID("Nick", "22", "9")
    assert "already exists" in msg


# checking the header names
def test_csv_header():
    check_file()
    with open(file_name, "r") as f:
        reader = csv.reader(f)
        headers = next(reader)
    expected = ["Name", "Roll", "Grade", "ID"]
    assert headers == expected

# checking if test file is created properly or not
def test_file_create():
    if os.path.isfile(file_name):
        os.remove(file_name)
    check_file()
    assert os.path.isfile(file_name)


