#PROGRAMME TO REGISTER A NEW UNIVERSITY STUDENT

#STEP 1 - Create the Student class
class Student:

    next_id = 1

    def __init__(self, first_name, last_name, YOB):
        self.first_name = first_name
        self.last_name = last_name
        self.YOB = YOB

#Generate the student ID
        self.studentID = f"ST{Student.next_id:03d}"
        Student.next_id += 1

#Generate the student's email address
        self.email = (f"{self.first_name.lower()}."
        f"{self.last_name.lower()}@uni.edu")

    def display(self):
        print(f"Your new email address is {self.email}")
        print(f"Your new student ID is {self.studentID}.")

#STEP 2 - Create the Athlete subclass
class Athlete(Student):

    def __init__(self, first_name, last_name, YOB, sport):
        super().__init__(first_name, last_name, YOB)
        self.sport = sport

    def play(self):
        print(f"{self.first_name} plays {self.sport}.")

#STEP 3 - Collect Student details
first_name = input("Enter your first name ")
last_name = input("Enter your last name ")
YOB = input("Enter your year of birth ")

answer = input("Do you play a sport?. Please answer with Yes or No. ").strip().lower()

#STEP 4 - Create the correct object

if answer == "yes":
    sport = input("Please indicate which sport you play: ")
    student = Athlete(first_name, last_name,YOB, sport)
else:
    student = Student(first_name,last_name,YOB)
    
#STEP 5 - Display the student information
print("\n")
student.display()
if isinstance(student,Athlete):
    student.play()
    
