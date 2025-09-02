#1
# and - აბრუნებს true მაშინ როცა ორივე მხარე true არის 
#or აბრუნებს true -ს მაშინაც როცა ერთ მაიც true არის

# 2
name = input("შეიყვანეთ შენი სახელი")

if name == "ixvi":
    print("სახელი სწორია")

else: 
    print("სახელი არ ემთხვევა")

# 3

number = int(input("შეიყვანე რიცხვი: "))

if number > 50:
    print("რიცხვი მეტია 50-ზე")
else:
    print("რიცხვი არ არის 50 ზე მეტი")

#4 
my_favorite_toy = "lego"

user_toy = input("შეიყვანეთ თქვენი საყვარელი სათამაშო")

if user_toy == my_favorite_toy: 
    print("ჩვენ ორივეს ერთი რამ ვიყვარს")
else:
    print("ცვენ სხვა და სხვა სათამაშო გვიყვარს")

#5 
print(True and False and True or False and True and False and True and False or True and False or True or False)

print(5 > 3)    
print(10 < 2)  
print(7 >= 7)   
print(8 <= 6)   
print(4 == 4)  




#7)

print(5 > 3 and 10 > 2)   
print(7 < 5 or 2 == 2)