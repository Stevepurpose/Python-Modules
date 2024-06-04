import exporter, platform

#use on the greet function
print(exporter.greet("hello "))
print(exporter.greet("Good morning "))


#use on the my_generator function
rundown = exporter.my_generator(2)

print(type(rundown))

#loop through values with next
print(next(rundown))
print(next(rundown))
print(next(rundown))


#use on b variable
print(exporter.b)

#check functions and variable names in module
print(dir(exporter))

#use the built-in platform module to check our system OS
print(platform.system())
print(dir(platform)) #print functions and variable names in module