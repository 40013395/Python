#finding the second smallest elemt in the list
def find_second_smallest(a):
    a.sort()
    return a[1]

if __name__ == "__main__":
    a=[]
    n = int(input("Enter the length of list: "))
    for i in range(n):
        a.append(int(input("Enter the element at index "+str(i))))
    print("The second smallest element is: {}".format(find_second_smallest(a)))
