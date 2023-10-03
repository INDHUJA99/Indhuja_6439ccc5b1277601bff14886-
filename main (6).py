
class student:
  def __init__(self, name, roll_number,cgpa):
    self.name = name
    self.roll_number = roll_number
    self.cgpa = cgpa 
def sort_students(students_list):  
#Sort the list of students in depending order of CGPA 
sorted_students = sorted(students_list, 
key = lambda student:student.cgpa,reverse = True)
#syntax_lamda arg:exp
return sorted_students
#Example usage:
students = [student("hari", "A123", 7.8),student("srikanth","A124",8.9),student("saumya","A125",9.9),student("mahidhar","A126",9.9)]
sorted_students = sort_students (students)
#print the sorted list of students 
for student in sorted_students:
  print("Name:{}, Roll number:{}, CGPA:{}".format(student.namestudent.roll number,student.CGPA))