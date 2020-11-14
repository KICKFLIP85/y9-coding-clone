#Area of rectangle, triangle, circle
#Options 
print("1) Circle")
print("2) Rectangle")
print("3) Triangle")

print("--------------------------------")

#User enters the corresponding number for shape - stored in option
option = int(input("Choose your shape \n"))
print("--------------------------------")


#Length/width/radius/base/height depending on the shape
#Calculates area and stores in each variable before printing it out.
	if option == 1:
		print("To calculate area of circle, enter the radius length. Pi is 3.14")
		radius = float(input("What is the radius?"))
		area1 = radius*radius*3.14
		print("The area of the circle is:", area1, " sq. units")
		print("--------------------------------")
	elif option == 2:
		print("To calculate area of rectangle, enter length and width")
		length = float(input("What is the length?"))
		width = float(input("What is the width?"))
		area2 = length*width
		print("The area of the rectangle is:", area2, " sq. units")
		print("--------------------------------")
	elif option == 3:
		print("To calculate area of triangle, enter length and width")
		base = float(input("What is the base?"))
		height = float(input("What is the height?"))
		area3 = 0.5*base*height
		print("The area of the triangle is:", area3, " sq. units")
		print("--------------------------------")
	else:
		print("ERROR! Not a valid choice!")

#Quits program	
input("Press ENTER to quit the program")





