name = str(input("Enter Student Name:"))
roll = int(input("Enter Roll Number:"))
maths = int(input("Enter Maths Mark:"))
science = int(input("Enter Science Mark:"))
english = int(input("Enter English Mark:"))

print("------ STUDENT REPORT ------")
print("Student Name :", name )
print("Student Roll Number :", roll )
Total = maths + science + english
print("Total :", Total)
Average = Total / 3
print("Average :", Average)

if Total >= 60:
    print("Pass")
else:
    print("Fail")