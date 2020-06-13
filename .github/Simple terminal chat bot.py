#! usr/bin/env/python3

#welcome note and request name of user
print("Hello! What is your name?")
name=input()
print()

#request age of user
print("Hi, " + name + "." " How old are you?")
age=input()
print()

#requests confirmation
print("Ok, " + name + "." + " So you're " + age + " years old?")
print("Y for yes\N for no")
confirmation=input ()
print()

if confirmation==Y:
   print("Great. I am Royal bot, made by Royal CyberIntelligence")
elif confirmation==N:
   print("Restart the program")
else:
   print("Input a valid reply")

