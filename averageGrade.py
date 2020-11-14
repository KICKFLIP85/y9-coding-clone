#Simple grading system

#Resets total grade point count to 0
total = 0


#Total amount of grades inputted
input_grades = int(input("How many grades will you input?"))


#Iterates until it reaches the max amount of input_grades
#Repeatedly adds the grades inputted into the variable "total" \
#that was set previously
for i in range(input_grades):
	grade = int(input("Enter the grade: "))
	total += grade

#Divides the total with the inputted grades, and stores in the variable 'avg'
avg = total/input_grades

#Prints final grade
print("The student's average grade is: " + str(avg))
