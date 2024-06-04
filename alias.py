#In this module, the module which we are importing bears an alias, using the as keyword when importing

import exporter as new_name
#use on the greet function
print(new_name.greet("hello "))
print(new_name.greet("Good morning "))


#use on the my_generator function
rundown = new_name.my_generator(2)

print(type(rundown))

#loop through values with next
print(next(rundown))
print(next(rundown))
print(next(rundown))


#use on b variable
print(new_name.b)