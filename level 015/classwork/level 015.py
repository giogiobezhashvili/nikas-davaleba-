# 1
# == ნიშნავს ტოლია თუ არა 
# != არ უდრის 

print(1==1)
print(1==3)
print(4==4)

print(2!= 3)
print(5!= 5)
print("x" != "y")
# 2
# conditional statement ანუ პირობითი განცხადება (მოკლედ რომ ვთქვათ პირობა)
# keyword ანუ საკვანძო სიტყვა ესენი გვაქვს 3  if elif და else 

# 3
age = int(input("თქვენი ასაკი: "))

if age > 18:
    print("you are an adult")
elif age == 18:
    print("you are 18 yo")
else:
    print("you are teenager")

# 4 
x = 0
while  x < 5:
    print("nika")

    x += 1


# 5

for i in range (1,7):
    print(i)
    sum += i 

print(sum)  
# ვერ გავიგე როგორ შევაჯამო ხან ერორებს მიგდებს ხან 12 ხან sum += i

# 6
user_name = input("enter your name: ")
my_name = "nika"

if user_name == my_name:
    print("the names are same")
else:
    print("the names are different")