# 1
grade = int(input("your grade (0-100): "))

if grade >= 90 and grade <= 100:
    print("ნიშანი: A")
else:
    if grade >= 80:
        print("ნიშანი: B")
    else:
        if grade >= 70:
            print("ნიშანი: C")
        else:
            if grade >= 60:
                print("ნიშანი: D")
            else:
                if grade >= 0:
                    print("ნიშანი: F")
                else:
                    print("შეყვანილი ქულა არასწორია!")

# 2
num = float(input("შეიყვანეთ რიცხვი: "))  #float ი იმიტომ დავუზერ რომ შეიძლება წილადი რიცხვი შემოეტანა მაგ. 2,5 ერორს დწერს

if num > 0:
    print("რიცხვი დადებითია")
else:
    if num < 0:
        print("რიცხვი უარყოფითია")
    else:
        print("რიცხვი ნულის ტოლია ")

# 3

num1 = float(input("Enter your number №1: "))
num2 = float(input("Enter your number №2: "))

if num1 > num2 :
    print("First Number is Greater than  second one")
else:
    print("Second Number is Greater than first one")

# 4
num = int(input("შეიყვანეთ რიცხვი: "))

if num % 2 == 0:
    print("რიცხვი ლუწია")
else:
    print("რიცხვი კენტია")

# 5

temp = float(input("Enter temperature in Celsius: "))

if temp<0:
    print( "Cold ❄️")
else:
    if temp <= 30:
        print("Normal 🌤️")
    else:
        print("Hot ☀️")
