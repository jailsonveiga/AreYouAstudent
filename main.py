STUDENT_NAME = "student"

students = ["Pedro", "Ailton", "Flavio", "Fedra", "Ellen", "Gisela", "Bruno", "Nuno"]

print("\nAre you a " + STUDENT_NAME + " ? Lets find out...\n")


accept = input("Are you a " + STUDENT_NAME + "?\n(yes/no): ").replace(" ", "")
if accept.lower() == "yes" or accept.lower() == "y":
    studentName = input("What is your name?\nName: ").replace(" ", "")
    for student in students:
        if studentName.lower() == student.lower():
            print("Welcome to class " + student)
            exit()
    else:
        print("You're not supposed to be here")

else:
    print("This service is not for you. Exiting program...")
    exit()
