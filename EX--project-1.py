'''Student Grade Management System
Program that records, updates, and deletes student grades. 
Handle exceptions like invalid student ID, empty grade inputs, and type 
mismatches.''' 

students = {}

while True:
    print("\nStudent Grade Management System")
    print("1. Add Student")
    print("2. Update Grade")
    print("3. Delete Student")
    print("4. Show Students")
    print("5. Exit")
    choice = input("Enter choice: ")
    try:
        if choice == "1":
            sid = input("Enter Student ID: ")
            if sid == "":
                raise ValueError("Student ID cannot be empty")

            grade = float(input("Enter Grade: "))
            students[sid] = grade
            print("Student added successfully")

        elif choice == "2":
            sid = input("Enter Student ID to update: ")
            if sid not in students:
                raise KeyError("Invalid Student ID")

            grade = float(input("Enter new Grade: "))
            students[sid] = grade
            print("Grade updated")

        elif choice == "3":
            sid = input("Enter Student ID to delete: ")
            if sid not in students:
                raise KeyError("Invalid Student ID")

            del students[sid]
            print("Student deleted")

        elif choice == "4":
            print("Student Records:")
            for i in students:
                print("ID:", i, "Grade:", students[i])

        elif choice == "5":
            print("Program Ended")
            break

        else:
            print("Invalid choice")

    except ValueError:
        print("Error: Grade must be a number or ID empty")

    except KeyError as e:
        print("Error:", e)
