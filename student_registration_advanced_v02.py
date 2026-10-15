#PROGRAMME TO REGISTER A NEW UNIVERSITY STUDENT
from abc import ABC, abstractmethod #importing abstractmethod

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

#STEP 2 - Create the abstract Athlete subclass
class Athlete(Student,ABC):

    def __init__(self, first_name, last_name, YOB, sport):
        super().__init__(first_name, last_name,YOB)
        self.sport = sport
    @abstractmethod
    def play(self):
        pass

#STEP 3 - Create subclasses for specific sports
class Boxer(Athlete):
    def play(self):
        return f"{self.first_name} does boxing."

class Cyclist(Athlete):
    def play(self):
        return f"{self.first_name} is a competitive cyclist."

class Skier(Athlete):
    def play(self):
        return f"{self.first_name} is a ski athlete."

class Judoka(Athlete):
    def play(self):
        return f"{self.first_name} is a judoka."

class Gymnast(Athlete):
    def play(self):
        return f"{self.first_name} is a gymnast."


#STEP 4 - Create general subclass for other sports
class GeneralAthlete(Athlete):
    def play(self):
        return f"{self.first_name} plays {self.sport}."


#STEP 5 - Collect Student details
first_name = input("Enter your first name ").strip()
last_name = input("Enter your last name ").strip()
YOB = input("Enter your year of birth ").strip()

answer = input("Do you play a sport? Please answer with Yes or No. ").strip().lower()

#STEP 6 - Create the correct object

if answer == "yes":
    sport = input("Please indicate which sport you play. ").strip().lower()

    if sport == "boxing":
        athlete = Boxer(first_name, last_name, YOB, sport)
    elif sport == "cycling":
        athlete = Cyclist(first_name, last_name, YOB, sport)
    elif sport == "skiing":
        athlete = Skier(first_name, last_name, YOB, sport)
    elif sport == "judo":
        athlete = Judoka(first_name, last_name, YOB, sport)
    elif sport == "gymnastics":
        athlete = Gymnast(first_name, last_name,YOB, sport)
    else:
        athlete = GeneralAthlete(first_name, last_name, YOB, sport)
else:
    student = Student(first_name,last_name, YOB)

#STEP 7 - Display the student information
print("\n")
if isinstance(athlete,Athlete):
    athlete.display()
    print(athlete.play())
else:
    student.display()


    

