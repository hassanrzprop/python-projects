# initial requirments
# default five students
# add a student
# update a student data
# delete any student
# show all students email and id's
from data import students

# ADD ANY STUDENT

new_student={
    "id":len(students)+1,
    "name":input("please enter your name-->"),
    "email":input("Please enter your Email-->"),
    "roll_no":int(input("please enter your roll No-->")),
    "class":input("Please enter your class-->")
}
students.append(new_student)



# UPDATE STUDENT DATA
student_id=input("please Enter the ID of student you want to update-->")
updated_email=input("Please Enter the email of student you want to update-->")
def updatedStudent(student):
    if student["id"]==student_id:
        return{
            "id":student_id,
            "name":student["name"],
            "email":updated_email,
            "roll_no":student["roll_no"],
            "class":student["class"]
        }
    else:
        return student
students=list(map(updatedStudent,students))       
print(students)    


# delete required student
id=input("please enter ID od student you want to delete-->")
students=list(filter(lambda student:student["id"]!= id,students))
print(students)
# show all emails and id's
for t in students:
   print("student Email: " , t["email"],"id:",t["id"])