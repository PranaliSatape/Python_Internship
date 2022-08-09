'''___Program for assigning values to the variables___'''

#Assigning Multiple Values to Multiple Variables

a = 50 ; b = "ABC" ; c = 5.45

print(a)
print(b)
print(c)

col1, col2, col3 = "red", "orange", "green"

print(col1)
print(col2)
print(col3) 

#Assigning one value to multiple variables

col1 = col2 = col3 = "Yellow"

print(col1)
print(col2)
print(col3) 

#Assigning values from list to variables

colours = ["Yellow", "Green", "Red"]

print("Assigning values from list to variables")

col1, col2, col3 = colours

print(col1)
print(col2)
print(col3)

#Multiple variables in one statement

x = "Have "
y = "Happy "
z = "Thoughts..!!"

print(x + y + z)
print(x , y , z)

'''
#In case of '+' operator 
x = 100
y = "ABC"
print(x + y) 
'''