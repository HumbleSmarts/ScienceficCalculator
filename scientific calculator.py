import math as mylib
 #ComplexFunLibrary 
print("Select among the following Calculation Operation:")
print("1. Addition Operation")
print("2. Subtraction Operation")
print("3. Division Operation")
print("4. Multiplication Operation")
print("5. Scientific Operation")

userSelection=int(input("Enter your choice:"))


if(userSelection==1):
    first=int(input("Enter 1st operand: "))
    second=int(input("Enter 2nd operand: "))
    result=first+second
    print("addition of {:d} and {:d} is {:d}" .format(first,second,result))

elif(userSelection==2):
    first=int(input("Enter 1st operand: "))
    second=int(input("Enter 2nd operand: "))
    result=first-second
    print("subtraction of {:d} and {:d} is {:d}" .format(first,second,result))


elif(userSelection==3):
    if(second==0):
        print("divisor can't be zero, please try again")
    else:
        first=int(input("Enter 1st operand: "))
        second=int(input("Enter 2nd operand: "))
        result=first/second
        print("division of {:d} and {:d} is {:d}" .format(first,second,result))

elif(userSelection==4):
    first=int(input("Enter 1st operand: "))
    second=int(input("Enter 2nd operand: "))
    result=first*second
    print("multiplication of {:d} and {:d} is {:d}" .format(first,second,result))

elif(userSelection==5):
    
    while True:
        print("1. Sine Operation")
        print("2. Cos Operation")
        print("3. Tan Operation")
        print("4. Power Operation")
        print("5. Log10 Operation")

        userScientificSelection=int(input("Enter your choice: "))

        if(userScientificSelection==1):
            angle=int(input("Enter angle: "))
            print("Sin value of {} is {}" .format(angle,mylib.sincalc(angle)))

        elif(userScientificSelection==2):
            angle=int(input("Enter angle: "))
            print("cos value of {} is {}" .format(angle,mylib.coscalc(angle)))

        elif(userScientificSelection==3):
            angle=int(input("Enter angle: "))
            print("tan value of {} is {}" .format(angle,mylib.tancalc(angle)))

        elif(userScientificSelection==4):
            base=int(input("Enter base: "))
            power=int(input("Enter power: "))
            print("{} power of {} is {}" .format(power,base,mylib.powercalc(base,power)))

        elif(userScientificSelection==5):
            logval=int(input("Enter log value: "))
            print("log value of {} is {}" .format(logval,mylib.log10calc(logval)))

        user_choose=input("Do you want to continue?: ")
        if(user_choose!='y'):
             break
    #Humblesmarts
