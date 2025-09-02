# 1

# ==  (ტოლია თუ არა)
print(5 == 5)   
print(10 == 7)  
print("abc" == "abc")  
print(3.0 == 3) 
print([1,2] == [1,2])  




# >  (მეტია)
print(10 > 5)   
print(3 > 7)    
print(2.5 > 2)  
print(100 > 99) 
print(-1 > -5)  


# <  (ნაკლებია)
print(5 < 10)  
print(7 < 3)    
print(1 < 1.1)  
print(-10 < -2) 
print(100 < 50) 


# >=  (მეტია ან ტოლია)
print(5 >= 5)   
print(10 >= 7)  
print(3 >= 4)   
print(2.0 >= 2) 
print(0 >= -1)  

# <=  (ნაკლებია ან ტოლია)
print(5 <= 5)  
print(2 <= 10)  
print(7 <= 6)   
print(-3 <= -3) 
print(0 <= 100) 

# 2
# Logical Operators (ლოგიკური ოპერატორები)

# 1) and ის შემთხვევაში თუ კი ერთი პირობა მაინც იქნება მცდარი მაშინ გამოიტანს false  ხოლო თუ ორივე იქნება სიმართლე მაშინ True

print(True and True)   # True
print(True and False)  # False
print(False and True)  # False
print(False and False) # False

# 2) or ის დროს თუ კი ერთი პირობა მაინც სიმართლეა მაშინ გამოიტანს true თუ ორივე არ არის სიმართლე მაშინ false

print(True or True)    # True
print(True or False)   # True
print(False or True)   # True
print(False or False)  # False


# 3
# or
print(10>5 or 5<10)
print(5>3 or 5<3)
print(5>4 or 10>8)

# and 

print(15>5 and 20>10)
print(10>5 and 5>10)
print(5<4 and 5>4)

# 4

num1 = int(input("ჩაწერეთ რიცხვი: "))
num2 = 50
print(num1 > num2)

# 5 

name1 = input("ჩაწერეთ თქვენი სახელი: ")
name2 = "nika"
print(name1 == name2 )

# 6 

age1 = int(input("ჩაწერეთ თქვენი ასაკი: "))
age2 = 18
print(age1 > age2)