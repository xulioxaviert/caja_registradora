a = 5

b = 10
c = a + b

e,f = 15, 20
g = e + f


print("The sum of a and b is:", c)
print("The sum of e and f is:", g)  

# variables string
foo = "Hello World"
print(foo)

number_as_string1 = 3
number_as_string1 = str(number_as_string1)
second_number_as_string = 4
second_number_as_string = str(second_number_as_string)
concatenated_number_strings = number_as_string1 + second_number_as_string
print("The concatenated string of var1 and var2 is:", concatenated_number_strings)

# existen métodos de cadenas 
print("foo.capitalize():", foo.capitalize())
print("foo.title():", foo.title())
print("foo.replace('World', 'Python'):", foo.replace('World', 'Python'))
print("foo.startswith('Hello'):", foo.startswith('Hello'))
print("foo.endswith('World'):", foo.endswith('World'))
print("foo.find('World'):", foo.find('World'))
print("foo.count('l'):", foo.count('l'))
print("foo.isalpha():", foo.isalpha())
print("foo.isdigit():", foo.isdigit())
print("foo.strip():", foo.strip())
print("La longitud de la cadena es:", len(foo))
print("La cadena en mayúsculas es:", foo.upper())
print("La cadena en minúsculas es:", foo.lower())
print("La cadena contiene 'World':", "World" in foo)

# variables booleanas
is_active = True
is_admin = False
print("Is active:", is_active)
print("Is admin:", is_admin)

foo = True
bar = False
print("foo and bar:", foo and bar)
print("foo or bar:", foo or bar)
print("not foo:", not foo)

print(5 == "5")