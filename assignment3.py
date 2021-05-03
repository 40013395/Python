
def find_first_repeated(my_str):
    a=[]
    for i in my_str:
        if(i in a):
            return i
        else:
            a.append(i)


if __name__ == "__main__":
    my_str = input("Enter your string: ")
    print(find_first_repeated(my_str))