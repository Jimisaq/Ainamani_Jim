students = []
staff = []

class Member:
    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name


class Student(Member):
    def __init__(self, first_name, last_name,student_no, course):
        super().__init__(first_name, last_name)
        self.student_no = student_no
        self.course = course

    def __str__(self):
        return f'''
First Name: {self.first_name} 
Last Name: {self.last_name} 
Student Number: {self.student_no} 
Program: {self.course}
----------------------------------------------------------------------------------------------------
        '''
class Staff(Member):
    def __init__(self, first_name, last_name,staff_no, salary):
        super().__init__(first_name, last_name)
        self.staff_no = staff_no
        self.salary = salary

    def __str__(self):
        return f'''
First Name: {self.first_name} 
Last Name: {self.last_name} 
Staff Number: {self.staff_no} 
Salary: {self.salary} 
----------------------------------------------------------------------------------------------------
'''

# x = Student("Ainamani","Jim",2300723038,"Software Engineering")
# print(x)

#Adding a new student to the list
def add_student(first_name, last_name, student_no, course):
    student = Student(first_name, last_name, student_no, course)
    students.append(student)

#Add a new staff member
def add_staff_member(first_name,last_name,staff_no,salary):
    staff_member = Staff(first_name, last_name, staff_no, salary)
    staff.append(staff_member)

#Displaying all students or staff
def display(list_of_members):
    if len(list_of_members)==0:
        print("No members found")
    for member in list_of_members:
        print(member)

#display(students)
def register_student():
    first_name = input("Enter First Name: ")
    last_name = input("Enter Last Name: ")
    student_no = input("Enter Student Number: ")
    course = input("Enter Course: ")
    add_student(first_name, last_name, student_no, course)
    print("Student Registered Successfully")

#register staff member
def register_staff_member():
    first_name = input("Enter First Name: ")
    last_name = input("Enter Last Name: ")
    staff_no = input("Enter Staff Number: ")
    salary = input("Enter Salary: ")
    add_staff_member(first_name, last_name, staff_no, salary)
    print("Staff Registered Successfully")

def delete_staff_member():
    staff_no = input("Enter Staff Number: ")
    found = False
    for member in staff:
        if member.staff_no == staff_no:
            print(member)
            comfirm = input("Do you want to delete the staff? (y/n): ")
            if comfirm == "y":
                staff.remove(member)
            else:
                print("Cancelled")

    if not found:
        print("Staff Not Found")


def delete_student():
    student_no = input("Enter Student Number: ")
    found = False
    for stdnt in students:
        if stdnt.student_no == student_no:
            print(stdnt)
            confirm = input("Do you want to delete this student? (y/n): ")
            if confirm == "y":
                staff.remove(stdnt)
            else:
                print("Cancelled")

    if not found:
        print("Staff Not Found")


while(True):
    try:
        choice=int(input('''
1-View Staff
2-View Students
3-Register Staff Member
4-Register Student
5-Exit
Enter your choice:
        '''))
        match choice:
            case 1:
                display(staff)
            case 2:
                display(students)
            case 3:
                register_staff_member()
            case 4:
                register_student()
            case 5:
                print("Exiting...Thank You!!")
                break
    except ValueError:
        print("Invalid Choice")


