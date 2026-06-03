import os
try:
    import numpy as np
    import pandas as pd
    import matplotlib.pyplot as plt
except ImportError as e:
    print(f"Error importing modules: {e}")


def student_registration():
    print("\n========================================")
    print("  1: Student Registration")
    print("========================================")

    student_name = input("Enter student name: ")
    score = float(input("Enter exam score (0-100): "))

    if score >= 90 and score <= 100:
        grade = "A"
        remark = "Excellent"
    elif score >= 75:
        grade = "B"
        remark = "Very Good"
    elif score >= 60:
        grade = "C"
        remark = "Good"
    elif score >= 40:
        grade = "D"
        remark = "Average"
    else:
        grade = "F"
        remark = "Needs Improvement"

    print("\n--- Student Report ---")
    print("Name:", student_name)
    print("Score:", score)
    print("Grade:", grade)
    print("Performance Remark:", remark)

    return student_name, score, grade, remark


# -------------------- LAB 2 -------------------
#          Course Enrollment Management System

def course_enrollment():
    print("\n========================================")
    print("   2: Course Enrollment")
    print("========================================")

    courses = []
    max_courses = 5

    print("=== Course Enrollment System ===")
    while True:
        if len(courses) >= max_courses:
            print("Maximum course limit reached!")
            break

        course_name = input("Enter course name (or 'done' to finish): ")
        if course_name.lower() == "done":
            break

        credits = input("Enter credit value: ")

        if not credits.isdigit():
            print("Invalid credit value! Skipping entry...")
            continue

        credits = int(credits)
        if credits <= 0:
            print("Credit must be positive! Skipping entry...")
            continue

        courses.append((course_name, credits))
        print(f"Course '{course_name}' with {credits} credits added.\n")

    print("\n--- Enrollment Report ---")
    for course, credit in courses:
        print(f"Course: {course}, Credits: {credit}")
    print("Total courses enrolled:", len(courses))

    return courses


# -------------------- LAB3---------------------
#       Student Record Data Management using Data Structures

def student_records():
    print("\n========================================")
    print("   3: Student Record Management")
    print("========================================")

    students = []
    students.append({"name": "Priya",  "age": 20, "grades": [85, 90, 78]})
    students.append({"name": "Rahul",  "age": 21, "grades": [72, 88, 91]})
    students.append({"name": "Anita",  "age": 19, "grades": [95, 89, 92]})

    print("=== Student Records ===")
    for student in students:
        print("Name:", student["name"])
        print("Age:", student["age"])
        print("Grades:", student["grades"])
        print("-----------------------")

    event_A = {"Priya", "Rahul", "Anita", "Kiran"}
    event_B = {"Rahul", "Anita", "Sneha"}

    common_participants = event_A & event_B
    all_participants   = event_A | event_B
    only_event_A       = event_A - event_B

    print("\n=== Event Participation Analysis ===")
    print("Common Participants:", common_participants)
    print("All Participants:", all_participants)
    print("Only Event A Participants:", only_event_A)

    return students


# -------------------- LAB4---------------------
#          Sorting and Searching of Student IDs

def search_sort_students():
    print("\n========================================")
    print("   4: Search and Sort Students")
    print("========================================")

    student_ids = [105, 102, 110, 108, 101, 115]
    print("Original IDs:", student_ids)

    # Bubble Sort
    n = len(student_ids)
    for i in range(n):
        for j in range(0, n - i - 1):
            if student_ids[j] > student_ids[j + 1]:
                temp = student_ids[j]
                student_ids[j] = student_ids[j + 1]
                student_ids[j + 1] = temp
    print("Sorted IDs (Bubble Sort):", student_ids)

    # Selection Sort
    student_ids2 = [105, 102, 110, 108, 101, 115]
    n = len(student_ids2)
    for i in range(n):
        min_index = i
        for j in range(i + 1, n):
            if student_ids2[j] < student_ids2[min_index]:
                min_index = j
        temp = student_ids2[i]
        student_ids2[i] = student_ids2[min_index]
        student_ids2[min_index] = temp
    print("Sorted IDs (Selection Sort):", student_ids2)

    # Linear Search
    target = int(input("Enter Student ID to search: "))
    found_index = -1
    for i in range(len(student_ids)):
        if student_ids[i] == target:
            found_index = i
            break

    if found_index != -1:
        print("Linear Search: ID", target, "found at index", found_index)
    else:
        print("Linear Search: ID not found")

    # Binary Search
    low = 0
    high = len(student_ids) - 1
    found_index = -1
    while low <= high:
        mid = (low + high) // 2
        if student_ids[mid] == target:
            found_index = mid
            break
        elif student_ids[mid] < target:
            low = mid + 1
        else:
            high = mid - 1

    if found_index != -1:
        print("Binary Search: ID", target, "found at index", found_index)
    else:
        print("Binary Search: ID not found")


# -------------------- LAB 5---------------------
#          Student Fee Calculation using Functions

def calculate_fee(tuition_fee, hostel_fee=0, transportation_fee=0):
    total_fee = tuition_fee + hostel_fee + transportation_fee
    return total_fee

def fee_calculation():
    print("\n========================================")
    print("   5: Fee Calculation")
    print("========================================")

    tuition    = float(input("Enter tuition fee: "))
    hostel     = float(input("Enter hostel fee (0 if not applicable): "))
    transport  = float(input("Enter transportation fee (0 if not applicable): "))

    total = calculate_fee(tuition, hostel_fee=hostel, transportation_fee=transport)

    print("\n--- Fee Report ---")
    print(f"Tuition Fee       : {tuition}")
    print(f"Hostel Fee        : {hostel}")
    print(f"Transportation Fee: {transport}")
    print(f"Total Fee         : {total}")

    return total


# -------------------- LAB 6---------------------
#       File Handling for Student Academic Records

def file_management():
    print("\n========================================")
    print("  6: File Management")
    print("========================================")

    # Write student details to a file
    with open("student_records.txt", "w") as file:
        file.write("ID,Name,Marks\n")
        file.write("101,Arjun,85\n")
        file.write("102,Meera,92\n")
        file.write("103,Ravi,76\n")
        file.write("104,Anita,89\n")
    print("Student records written to file successfully.")

    # Read stored records from the file
    print("\nReading stored records:")
    with open("student_records.txt", "r") as file:
        records = file.readlines()
        for record in records:
            print(record.strip())

    # Process stored data to generate a simple report
    print("\nGenerating Report:")
    total_students = 0
    total_marks = 0
    highest_marks = -1
    top_student = ""

    for record in records[1:]:
        parts = record.strip().split(",")
        name  = parts[1]
        marks = int(parts[2])

        total_students += 1
        total_marks += marks
        if marks > highest_marks:
            highest_marks = marks
            top_student = name

    average_marks = total_marks / total_students
    print("Total Students:", total_students)
    print("Average Marks:", average_marks)
    print("Top Student:", top_student, "with", highest_marks, "marks")


# -------------------- LAB 7---------------------
#         Directory Scanning with Exception Handling

class MissingFileOrFolderError(Exception):
    """Raised when a required file or folder is missing in the directory."""
    pass

def scan_directory(path):
    try:
        if not os.path.exists(path):
            raise FileNotFoundError(f"Invalid directory path: {path}")

        print(f"\nScanning directory: {path}\n")

        for root, dirs, files in os.walk(path):
            level      = root.replace(path, "").count(os.sep)
            indent     = " " * 4 * level
            sub_indent = " " * 4 * (level + 1)
            print(f"{indent}{os.path.basename(root)}/")
            for f in files:
                print(f"{sub_indent}{f}")

            if not files and not dirs:
                raise MissingFileOrFolderError(f"Empty folder detected: {root}")

    except FileNotFoundError as e:
        print(f"Error: {e}")
    except MissingFileOrFolderError as e:
        print(f"Custom Error: {e}")
    except Exception as e:
        print(f"Unexpected Error: {e}")

def directory_scanner():
    print("\n========================================")
    print("   MODULE 7: Directory Scanner")
    print("========================================")

    directory_path = input("Enter the directory path to scan: ")
    scan_directory(directory_path)


# -------------------- LAB 8---------------------
#   Student Performance Analysis using NumPy, Pandas, Matplotlib

def performance_analytics():
    print("\n========================================")
    print("   MODULE 8: Performance Analytics")
    print("========================================")

    # Create a sample CSV if it doesn't exist
    sample_data = "Name,Math,Science,English\nArjun,85,78,88\nMeera,92,95,90\nRavi,76,82,70\nAnita,89,91,85\nKiran,70,68,75\n"
    if not os.path.exists("student_performance.csv"):
        with open("student_performance.csv", "w") as f:
            f.write(sample_data)
        print("Sample CSV created: student_performance.csv")

    try:
        df = pd.read_csv("student_performance.csv")

        print("\n--- Raw Data ---")
        print(df.head())

        print("\n--- Statistical Summary ---")
        print(df.describe())

        scores = df[["Math", "Science", "English"]].to_numpy()

        mean_scores   = np.mean(scores,   axis=0)
        median_scores = np.median(scores, axis=0)
        std_dev_scores = np.std(scores,   axis=0)

        print("\n--- NumPy Analysis ---")
        print(f"Mean Scores   (Math, Science, English): {mean_scores}")
        print(f"Median Scores (Math, Science, English): {median_scores}")
        print(f"Standard Dev  (Math, Science, English): {std_dev_scores}")

        top_math    = df.loc[df["Math"].idxmax(),    "Name"]
        top_science = df.loc[df["Science"].idxmax(), "Name"]
        top_english = df.loc[df["English"].idxmax(), "Name"]

        print("\n--- Top Performers ---")
        print(f"Math   : {top_math}")
        print(f"Science: {top_science}")
        print(f"English: {top_english}")

        # Bar chart – average scores per subject
        subjects = ["Math", "Science", "English"]
        plt.figure()
        plt.bar(subjects, mean_scores, color=["blue", "green", "orange"])
        plt.title("Average Scores per Subject")
        plt.xlabel("Subjects")
        plt.ylabel("Average Score")
        plt.tight_layout()
        plt.savefig("avg_scores.png")
        plt.show()
        print("Chart saved as avg_scores.png")

        # Student-wise performance comparison
        df.plot(x="Name", y=["Math", "Science", "English"], kind="bar")
        plt.title("Student Performance Comparison")
        plt.ylabel("Scores")
        plt.tight_layout()
        plt.savefig("student_performance.png")
        plt.show()
        print("Chart saved as student_performance.png")

    except FileNotFoundError:
        print("Error: The CSV file was not found. Please check the file path.")
    except Exception as e:
        print(f"Unexpected Error: {e}")


# -------------------- INTEGRATION----------------
#         Main System Application Dashboard
# ============================================================

def main():
    print("\n" + "=" * 50)
 import os
try:
    import numpy as np
    import pandas as pd
    import matplotlib.pyplot as plt
except ImportError as e:
    print(f"Error importing modules: {e}")


def student_registration():
    print("\n========================================")
    print("  1: Student Registration")
    print("========================================")

    student_name = input("Enter student name: ")
    score = float(input("Enter exam score (0-100): "))

    if score >= 90 and score <= 100:
        grade = "A"
        remark = "Excellent"
    elif score >= 75:
        grade = "B"
        remark = "Very Good"
    elif score >= 60:
        grade = "C"
        remark = "Good"
    elif score >= 40:
        grade = "D"
        remark = "Average"
    else:
        grade = "F"
        remark = "Needs Improvement"

    print("\n--- Student Report ---")
    print("Name:", student_name)
    print("Score:", score)
    print("Grade:", grade)
    print("Performance Remark:", remark)

    return student_name, score, grade, remark


# -------------------- LAB 2 -------------------
#          Course Enrollment Management System

def course_enrollment():
    print("\n========================================")
    print("   2: Course Enrollment")
    print("========================================")

    courses = []
    max_courses = 5

    print("=== Course Enrollment System ===")
    while True:
        if len(courses) >= max_courses:
            print("Maximum course limit reached!")
            break

        course_name = input("Enter course name (or 'done' to finish): ")
        if course_name.lower() == "done":
            break

        credits = input("Enter credit value: ")

        if not credits.isdigit():
            print("Invalid credit value! Skipping entry...")
            continue

        credits = int(credits)
        if credits <= 0:
            print("Credit must be positive! Skipping entry...")
            continue

        courses.append((course_name, credits))
        print(f"Course '{course_name}' with {credits} credits added.\n")

    print("\n--- Enrollment Report ---")
    for course, credit in courses:
        print(f"Course: {course}, Credits: {credit}")
    print("Total courses enrolled:", len(courses))

    return courses


# -------------------- LAB3---------------------
#       Student Record Data Management using Data Structures

def student_records():
    print("\n========================================")
    print("   3: Student Record Management")
    print("========================================")

    students = []
    students.append({"name": "Priya",  "age": 20, "grades": [85, 90, 78]})
    students.append({"name": "Rahul",  "age": 21, "grades": [72, 88, 91]})
    students.append({"name": "Anita",  "age": 19, "grades": [95, 89, 92]})

    print("=== Student Records ===")
    for student in students:
        print("Name:", student["name"])
        print("Age:", student["age"])
        print("Grades:", student["grades"])
        print("-----------------------")

    event_A = {"Priya", "Rahul", "Anita", "Kiran"}
    event_B = {"Rahul", "Anita", "Sneha"}

    common_participants = event_A & event_B
    all_participants   = event_A | event_B
    only_event_A       = event_A - event_B

    print("\n=== Event Participation Analysis ===")
    print("Common Participants:", common_participants)
    print("All Participants:", all_participants)
    print("Only Event A Participants:", only_event_A)

    return students


# -------------------- LAB4---------------------
#          Sorting and Searching of Student IDs

def search_sort_students():
    print("\n========================================")
    print("   4: Search and Sort Students")
    print("========================================")

    student_ids = [105, 102, 110, 108, 101, 115]
    print("Original IDs:", student_ids)

    # Bubble Sort
    n = len(student_ids)
    for i in range(n):
        for j in range(0, n - i - 1):
            if student_ids[j] > student_ids[j + 1]:
                temp = student_ids[j]
                student_ids[j] = student_ids[j + 1]
                student_ids[j + 1] = temp
    print("Sorted IDs (Bubble Sort):", student_ids)

    # Selection Sort
    student_ids2 = [105, 102, 110, 108, 101, 115]
    n = len(student_ids2)
    for i in range(n):
        min_index = i
        for j in range(i + 1, n):
            if student_ids2[j] < student_ids2[min_index]:
                min_index = j
        temp = student_ids2[i]
        student_ids2[i] = student_ids2[min_index]
        student_ids2[min_index] = temp
    print("Sorted IDs (Selection Sort):", student_ids2)

    # Linear Search
    target = int(input("Enter Student ID to search: "))
    found_index = -1
    for i in range(len(student_ids)):
        if student_ids[i] == target:
            found_index = i
            break

    if found_index != -1:
        print("Linear Search: ID", target, "found at index", found_index)
    else:
        print("Linear Search: ID not found")

    # Binary Search
    low = 0
    high = len(student_ids) - 1
    found_index = -1
    while low <= high:
        mid = (low + high) // 2
        if student_ids[mid] == target:
            found_index = mid
            break
        elif student_ids[mid] < target:
            low = mid + 1
        else:
            high = mid - 1

    if found_index != -1:
        print("Binary Search: ID", target, "found at index", found_index)
    else:
        print("Binary Search: ID not found")


# -------------------- LAB 5---------------------
#          Student Fee Calculation using Functions

def calculate_fee(tuition_fee, hostel_fee=0, transportation_fee=0):
    total_fee = tuition_fee + hostel_fee + transportation_fee
    return total_fee

def fee_calculation():
    print("\n========================================")
    print("   5: Fee Calculation")
    print("========================================")

    tuition    = float(input("Enter tuition fee: "))
    hostel     = float(input("Enter hostel fee (0 if not applicable): "))
    transport  = float(input("Enter transportation fee (0 if not applicable): "))

    total = calculate_fee(tuition, hostel_fee=hostel, transportation_fee=transport)

    print("\n--- Fee Report ---")
    print(f"Tuition Fee       : {tuition}")
    print(f"Hostel Fee        : {hostel}")
    print(f"Transportation Fee: {transport}")
    print(f"Total Fee         : {total}")

    return total


# -------------------- LAB 6---------------------
#       File Handling for Student Academic Records

def file_management():
    print("\n========================================")
    print("  6: File Management")
    print("========================================")

    # Write student details to a file
    with open("student_records.txt", "w") as file:
        file.write("ID,Name,Marks\n")
        file.write("101,Arjun,85\n")
        file.write("102,Meera,92\n")
        file.write("103,Ravi,76\n")
        file.write("104,Anita,89\n")
    print("Student records written to file successfully.")

    # Read stored records from the file
    print("\nReading stored records:")
    with open("student_records.txt", "r") as file:
        records = file.readlines()
        for record in records:
            print(record.strip())

    # Process stored data to generate a simple report
    print("\nGenerating Report:")
    total_students = 0
    total_marks = 0
    highest_marks = -1
    top_student = ""

    for record in records[1:]:
        parts = record.strip().split(",")
        name  = parts[1]
        marks = int(parts[2])

        total_students += 1
        total_marks += marks
        if marks > highest_marks:
            highest_marks = marks
            top_student = name

    average_marks = total_marks / total_students
    print("Total Students:", total_students)
    print("Average Marks:", average_marks)
    print("Top Student:", top_student, "with", highest_marks, "marks")


# -------------------- LAB 7---------------------
#         Directory Scanning with Exception Handling

class MissingFileOrFolderError(Exception):
    """Raised when a required file or folder is missing in the directory."""
    pass

def scan_directory(path):
    try:
        if not os.path.exists(path):
            raise FileNotFoundError(f"Invalid directory path: {path}")

        print(f"\nScanning directory: {path}\n")

        for root, dirs, files in os.walk(path):
            level      = root.replace(path, "").count(os.sep)
            indent     = " " * 4 * level
            sub_indent = " " * 4 * (level + 1)
            print(f"{indent}{os.path.basename(root)}/")
            for f in files:
                print(f"{sub_indent}{f}")

            if not files and not dirs:
                raise MissingFileOrFolderError(f"Empty folder detected: {root}")

    except FileNotFoundError as e:
        print(f"Error: {e}")
    except MissingFileOrFolderError as e:
        print(f"Custom Error: {e}")
    except Exception as e:
        print(f"Unexpected Error: {e}")

def directory_scanner():
    print("\n========================================")
    print("   MODULE 7: Directory Scanner")
    print("========================================")

    directory_path = input("Enter the directory path to scan: ")
    scan_directory(directory_path)


# -------------------- LAB 8---------------------
#   Student Performance Analysis using NumPy, Pandas, Matplotlib

def performance_analytics():
    print("\n========================================")
    print("   MODULE 8: Performance Analytics")
    print("========================================")

    # Create a sample CSV if it doesn't exist
    sample_data = "Name,Math,Science,English\nArjun,85,78,88\nMeera,92,95,90\nRavi,76,82,70\nAnita,89,91,85\nKiran,70,68,75\n"
    if not os.path.exists("student_performance.csv"):
        with open("student_performance.csv", "w") as f:
            f.write(sample_data)
        print("Sample CSV created: student_performance.csv")

    try:
        df = pd.read_csv("student_performance.csv")

        print("\n--- Raw Data ---")
        print(df.head())

        print("\n--- Statistical Summary ---")
        print(df.describe())

        scores = df[["Math", "Science", "English"]].to_numpy()

        mean_scores   = np.mean(scores,   axis=0)
        median_scores = np.median(scores, axis=0)
        std_dev_scores = np.std(scores,   axis=0)

        print("\n--- NumPy Analysis ---")
        print(f"Mean Scores   (Math, Science, English): {mean_scores}")
        print(f"Median Scores (Math, Science, English): {median_scores}")
        print(f"Standard Dev  (Math, Science, English): {std_dev_scores}")

        top_math    = df.loc[df["Math"].idxmax(),    "Name"]
        top_science = df.loc[df["Science"].idxmax(), "Name"]
        top_english = df.loc[df["English"].idxmax(), "Name"]

        print("\n--- Top Performers ---")
        print(f"Math   : {top_math}")
        print(f"Science: {top_science}")
        print(f"English: {top_english}")

        # Bar chart – average scores per subject
        subjects = ["Math", "Science", "English"]
        plt.figure()
        plt.bar(subjects, mean_scores, color=["blue", "green", "orange"])
        plt.title("Average Scores per Subject")
        plt.xlabel("Subjects")
        plt.ylabel("Average Score")
        plt.tight_layout()
        plt.savefig("avg_scores.png")
        plt.show()
        print("Chart saved as avg_scores.png")

        # Student-wise performance comparison
        df.plot(x="Name", y=["Math", "Science", "English"], kind="bar")
        plt.title("Student Performance Comparison")
        plt.ylabel("Scores")
        plt.tight_layout()
        plt.savefig("student_performance.png")
        plt.show()
        print("Chart saved as student_performance.png")

    except FileNotFoundError:
        print("Error: The CSV file was not found. Please check the file path.")
    except Exception as e:
        print(f"Unexpected Error: {e}")


# -------------------- INTEGRATION----------------
#         Main System Application Dashboard
# ============================================================

def main():
    print("\n" + "=" * 50)
    print("   SMART CAMPUS INFORMATION SYSTEM")
    print("   Main Application Dashboard")
    print("=" * 50)

    while True:
        print("\n--- Main Menu ---")
        print("1. Student Registration and Grade Evaluation")
        print("2. Course Enrollment Management")
        print("3. Student Record Data Management")
        print("4. Search and Sort Student Data")
        print("5. Fee Calculation")
        print("6. File Management – Academic Records")
        print("7. Directory Scanner")
        print("8. Performance Analytics (NumPy/Pandas/Matplotlib)")
        print("9. Exit")

        choice = input("\nEnter your choice (1-9): ")

        if choice == "1":
            student_registration()
        elif choice == "2":
            course_enrollment()
        elif choice == "3":
            student_records()
        elif choice == "4":
            search_sort_students()
        elif choice == "5":
            fee_calculation()
        elif choice == "6":
            file_management()
        elif choice == "7":
            directory_scanner()
        elif choice == "8":
            performance_analytics()
        elif choice == "9":
            print("\nExiting Smart Campus Information System. Goodbye!")
            break
        else:
            print("Invalid choice! Please enter a number between 1 and 9.")


if __name__ == "__main__":
    main()   print("   SMART CAMPUS INFORMATION SYSTEM")
    print("   Main Application Dashboard")
    print("=" * 50)

    while True:
        print("\n--- Main Menu ---")
        print("1. Student Registration and Grade Evaluation")
        print("2. Course Enrollment Management")
        print("3. Student Record Data Management")
        print("4. Search and Sort Student Data")
        print("5. Fee Calculation")
        print("6. File Management – Academic Records")
        print("7. Directory Scanner")
        print("8. Performance Analytics (NumPy/Pandas/Matplotlib)")
        print("9. Exit")

        choice = input("\nEnter your choice (1-9): ")

        if choice == "1":
            student_registration()
        elif choice == "2":
            course_enrollment()
        elif choice == "3":
            student_records()
        elif choice == "4":
            search_sort_students()
        elif choice == "5":
            fee_calculation()
        elif choice == "6":
            file_management()
        elif choice == "7":
            directory_scanner()
        elif choice == "8":
            performance_analytics()
        elif choice == "9":
            print("\nExiting Smart Campus Information System. Goodbye!")
            break
        else:
            print("Invalid choice! Please enter a number between 1 and 9.")


if __name__ == "__main__":
    main()
