q=[]
def first():
    fund=input("enter your fund:")
    q.append(fund)
    print("your fund is:",fund)
def second():
    if not q:
        print("your balance is 500000")
    else:
        fund=q.pop(0)
    print("fundtransferring cancelled:",fund)
def display():
    if not q:
        print("your balance is 500000")
    else:
        print(q)
    while True:
        choice=int(input("1,insert 2.delete 3.display 4.enter your choice"))
        if choice==1:
            first()
        elif choice==2:
            second()
        elif choice==3:
            display()
        else:
            break
        
    