#change the first character occurence in a string to "$", except the first character itself

my_str = input("Enter the string: ")
print((my_str.replace(my_str[0], "$")).replace("$", my_str[0], 1))