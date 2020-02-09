dic={}
while True:
    print('1.Enter Data')
    print('2.Check birthday')
    print('3.exit')
    m=int(input("Enter a choice to perform "))
    if(m==1):
        k=input("enter name ")
        n=input("enter bday date ")
        dic[k]=n
        print("bday added")
    elif(m==2):
        if(len(dic.keys())==0):
            print("Nothing to show")
        else:
            name= input("enter name to look for birthday ")
            birthday=dic.get(name,"Nothing to show")
            print(birthday)
    elif(m==3):
        break
    else:
        print("enter some right choice")
