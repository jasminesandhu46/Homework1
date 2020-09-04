# Author: Jasmine Sandhu jps6818@psu.ed

grade1 = (input("Enter your course 1 letter grade: "))
credit1 = (input("Enter your course 1 credit: "))

if (grade1 == "A"):
  gradepoint1 = 4.0
  print(f"Grade point for course 1 is: {gradepoint1}") 
elif (grade1 == "A-"):
  gradepoint1 = 3.67 
  print(f"Grade point for course 1 is: {gradepoint1}")
elif (grade1 == "B+"):
  gradepoint1 = 3.33
  print(f"Grade point for course 1 is: {gradepoint1}") 
elif (grade1 == "B"):
  gradepoint1 = 3.0
elif (grade1 == "B-"):
  gradepoint1 = 2.67
  print(f"Grade point for course 1 is: {gradepoint1}") 
elif (grade1 == "C+"):
  gradepoint1 = 2.33
  print(f"Grade point for course 1 is: {gradepoint1}") 
elif (grade1 == "C"):
  gradepoint1 = 2.0
  print(f"Grade point for course 1 is: {gradepoint1}")
elif (grade1 == "D"):
  gradepoint1 = 1.0
  print(f"Grade point for course 1 is: {gradepoint1}") 
else:
  gradepoint1 = 0.0
  print(f"Grade point for course 1 is: {gradepoint1}") 

grade2 = (input("Enter your course 2 letter grade: "))
credit2 = (input("Enter your course 2 credit: "))

if (grade2 == "A"):
  gradepoint2 = 4.0
  print(f"Grade point for course 2 is: {gradepoint2}")
elif (grade2 == "A-"):
  gradepoint2 = 3.67
  print(f"Grade point for course 2 is: {gradepoint2}") 
elif (grade2 == "B+"):
  gradepoint2 = 3.33
  print(f"Grade point for course 2 is: {gradepoint2}")
elif (grade2 == "B"):
  gradepoint2 = 3.0
  print(f"Grade point for course 2 is: {gradepoint2}")
elif (grade2 == "B-"):
  gradepoint2 = 2.67
  print(f"Grade point for course 2 is: {gradepoint2}")
elif (grade2 == "C+"):
  gradepoint2 = 2.33
  print(f"Grade point for course 2 is: {gradepoint2}")
elif (grade2 == "C"):
  gradepoint2 = 2.0
  print(f"Grade point for course 2 is: {gradepoint2}")
elif (grade2 == "D"):
  gradepoint2 = 1.0
  print(f"Grade point for course 2 is: {gradepoint2}")
else:
  gradepoint2 = 0.0
  print(f"Grade point for course 2 is: {gradepoint2}") 

grade3 = (input("Enter your course 3 letter grade: "))
credit3 = (input("Enter your course 3 credit: "))

if (grade3 == "A"):
  gradepoint3 = 4.0
  print(f"Grade point for course 3 is: {gradepoint3}")
elif (grade3 == "A-"):
  gradepoint3 = 3.67
  print(f"Grade point for course 3 is: {gradepoint3}") 
elif (grade3 == "B+"):
  gradepoint3 = 3.33
  print(f"Grade point for course 3 is: {gradepoint3}")
elif (grade3 == "B"):
  gradepoint3 = 3.0
  print(f"Grade point for course 3 is: {gradepoint3}")
elif (grade3 == "B-"):
  gradepoint3 = 2.67
  print(f"Grade point for course 3 is: {gradepoint3}")
elif (grade3 == "C+"):
  gradepoint3 = 2.33
  print(f"Grade point for course 3 is: {gradepoint3}")
elif (grade3 == "C"):
  gradepoint3 = 2.0
  print(f"Grade point for course 3 is: {gradepoint3}")
elif (grade3 == "D"):
  gradepoint3 = 1.0
  print(f"Grade point for course 3 is: {gradepoint3}")
else:
  gradepoint3 = 0.0
  print(f"Grade point for course 3 is: {gradepoint3}") 


GPA = (float(gradepoint1) * float(credit1) + float(gradepoint2) * float(credit2) + float(gradepoint3) * float(credit3) / (float(credit1) + float(credit2) + float(credit3)))
print(f"Your GPA is: {GPA}")

 