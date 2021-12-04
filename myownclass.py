# Diego Soriano 
# For this project I will be acting as a computer science instructor accessing my sutdent files 
# I will be creating a class of student information and a second class as a class subject 

class Student:
    def __init__(self, name, age, grade): 
        self.name = name 
        self.age = age 
        self.grade = grade 

s1 = Student("Joe", 14, 78)
s2 = Student("Blake", 15, 87) 
s3 = Student("Lexi", 16, 95) 

# To return indivdual student's grade 
def get_grade(self): 
    return self.grade  

class Subject: 
    def __init__(self, name, max_students): 
        self.name = name 
        self.max_students = max_students 
        self.student = []

# To add a student to the class
def add_student(self, student): 
# If amount of students is less than max amount of students let them in, if not deny them 
    if len(self.students) < self.max_students: 
        self.students.append(student) 
        return True 
    return False 

# To get class grade average
def get_average_grade(self): 
    value = 0 
    for students in self.students: 
        value += student.get_grade()
    return value / len(self.students) 

def lowest_grade(self): 
# list of grades in the class
list1 = [78, 87, 95] 
print ("list = ", list1)
 
# Finding the lowest grade in class
s_num = min (list1)
print ("The lowest grade in the class is ", s_num)

def get_oldest_age(self): 
# list of student's age 
list2 = [14, 15, 16] 
print ("list = ", list2)
 
# Finding oldest student 
s_num = min (list2)
print ("The age of the oldest student in the class is ", s_num)




  