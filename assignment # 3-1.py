marks=int(input("please enter the marks"))
grade=""
if(marks>=80):
   grade = "A Grade"
elif(marks>=60):
    grade = "B Grade"
elif(marks>=35):
      grade= "C Grade"
else:
    grade="fail"
print("Marks:",marks)
print("Grade:",grade)

