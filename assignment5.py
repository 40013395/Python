#nth element is changed to (n+1)th element

def jump(a,n):
    last = a[0]
    for i in range(n):
        if(i == n-1):
            a[i] = last
        else:
            a[i] = a[i+1]
    return a

if __name__ == "__main__":
    a=[]
    n = int(input("Enter the length of list: "))
    for i in range(n):
        a.append(int(input("Enter the element at index "+str(i))))
    print("The updated list is: {}".format(jump(a, n)))