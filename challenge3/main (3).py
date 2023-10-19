class student:
  
   def __init__(self,name,r_no,cgpa):
     self.name = name
     self.r_no = r_no
     self.cgpa = cgpa

def sort_stu(stu_list):
  sorted_stu = sorted(stu_list,key=lambda student: 
                      student.cgpa,reverse=True)
  return sorted_stu

students = [student("Nandy","A101",9.9),
            student("Jasra","A102",8.9),
            student("Kandy","A103",9.8),
            student("Sandy","A104",7.8)]

sorted_stu = sort_stu(students)
for student in sorted_stu:
  print("Name : {},Roll NO : {},CGPA : {}".format(student.name, student.r_no, student.cgpa))