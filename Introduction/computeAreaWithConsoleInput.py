#calculate area of circle

#prompt  the user to enter a radius

radius=eval(input("Enter a radius")) #though this is poor prompt

#self note : understand how input, print and eval function works
#compute area
area=radius * radius * 3.14159 #python is dynamically typed, so we don't need to declare type of variables

#display results using print
print("The are of circle of radius", radius, "is", area)
