my_str = input("Enter your string: ")
n = int(input("Enter the index at which you want to remove the character: "))
print(my_str[0:n]+my_str[n+1:len(my_str)])
