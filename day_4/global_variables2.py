'''___Program for global variables___'''

Name = "ABC"

def myfunc():

  global Name 
  Name = "rutuja" 
  print(Name) 

myfunc()

print("My name is " + Name)