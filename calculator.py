def add(a,b):
    return a+b

def sub(a,b):
    return a-b

def mult(a,b):
    return a*b

def div(a,b):
    if b != 0:
        return a/b
    else: 
        print("error: invalid operation(division by zero)")

def menu():
    print("choose your operation")
    print("1. addition")
    print("2. substruction")
    print("3. multiplication")
    print("4. division")
    print("5. exit")


menu()
operation=int(input("enter your operation"))
while operation!=5:
    a=float(input("enter a"))
    b=float(input("enter b"))
    if operation ==1:
        print(f"result= {add(a,b)}")
    elif operation==2:
        print(f"result= {sub(a,b)}")
    elif operation==3:
        print(f"result= {mult(a,b)}")
    elif operation==4:
        print(f"result= {div(a,b)}") 
        
    else:
        print("invalide operation")  
   

    menu()
    operation=int(input("enter your operation"))

print("thanks for using this program")   

            