students = {}

def add_student():
    name = input("Enter student name: ")
    
    if name in students:
        print("Student already exists!")
        return
    
    score = int(input("Enter score: "))
    students[name] = score
    print("Student added successfully!")

def show_students():
    if not students:
        print("No students found.")
        return
    
    print("\n Student List:")
    for name, score in students.items():
        print(name, "->", score)

def average_score():
    if not students:
        print("No data to calculate.")
        return
    
    total = 0
    for score in students.values():
        total += score
    
    avg = total / len(students)
    print("Average score is:", avg)

def best_student():
    if not students:
        print("No data available.")
        return
    
    best = max(students, key=students.get)
    print("Best student is:", best, "with score", students[best])

def menu():
    print("\n🎓 Student Score Manager")
    print("1. Add Student")
    print("2. Show Students")
    print("3. Average Score")
    print("4. Best Student")
    print("5. Exit")

while True:
    menu()
    choice = input("Choose an option: ")

    if choice == "1":
        add_student()
    elif choice == "2":
        show_students()
    elif choice == "3":
        average_score()
    elif choice == "4":
        best_student()
    elif choice == "5":
        print("Goodbye!")
        break
    else:
        print("Invalid choice!")
