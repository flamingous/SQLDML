# userName = input("what is your userName: ")
# age = input("what is your age: ")

# print(userName, "you are", age, "years old!")


# user_name = input ("what's your name:")
# user_age = input("how old are you?:")

# """
# Concatenations allows you to combine strings together using the + symbol
# """

# greeting = "Hey! " + user_name + " You are " + user_age + " years old"
# print(greeting)

# print("Welcome to my band name generator program")
# user_city = input("What is the name of your city?:")
# pet_name = input("What is your pet name")
# band_name = user_city + pet_name


# greeting = " Hey!, your band name is, " + band_name
# print(greeting)

# number = "3.14"
# number_float = float(number)
# print(number)

# number_1 = "3.14"
# number_2 = "3.15"
# #convert string to float
# number_1_float = float(number_1)
# number_2_float = float(number_2)
# #add the floats
# result = number_1_float + number_2_float
# print(result)

#Add these two integers following the steps above
# first_number = "2"
# second_number = "5"
# first_number_1 = float(first_number)
# second_number_2 = float(second_number)
# result = first_number_1 + second_number_2
# print(result)

# first_number = "2"
# second_number = "5"
# first_number_1 = int(first_number)
# second_number_2 = int(second_number)
# result = first_number_1 + second_number_2
# print(result)

# first_number = 2
# second_number = 5
# first_number_str = str(first_number)
# second_number_str = str(second_number)
# result = first_number_str + second_number_str
# print(result)


# print("calculator 1.0. psst! It can only add numbers")
# first_number = int(input("Enter first number: "))
# second_number = int(input("Enter second number: "))
# addition_result = first_number + second_number
# print(addition_result)
# print("The result of your input is: ", addition_result)

# first_number = float(input("Enter first number: "))
# second_number = float(input("Enter second number: "))
# multiplication_result = first_number * second_number
# print(multiplication_result)

# age = 18

# #allow users who are greater than or equal to 18 to use our app
# if age >= 18: 
#     print("You can register")
# else:
#     print("Get out, you can't register")

# country = "Nigeria"
# user_country = "France"
# if user_country == country:
#     print("You can register")
# else:
#     print("You have to be a Nigerian to register")

# country = "Nigeria"
# user_country = input("what is your county: ")
# if user_country == country:
#     print("You can register")
# else:
#     print("Get out!")

# 

#Ask the user 

# password = "odimma"
# user_password = input("Login password: ").lower()
# if user_password == password:
#     print("You are in")
# else:
#     print("Incorrect passoword")

#Logical operators with if statements
#AND operator evaluates to true if both conditions are true (or met)

# age = 15
# country = "nigeria"
# state = "abuja"
# if age >= 18 and country == "nigeria" and state == "abuja":
#     print("You can register")
# else:
#     print("You cannot register")

#or statement
# age = 18
# country = "nigeria"
# state = "abuja"
# if age >= 18 or country == "nigeria":
#     print("You can register")
# else:
#     print("You cannot register")


"""
use logical operators to check if  a student is from nigeria and is above 18 years 
might not neccessarily need to be in abuja. 
print, yes you can register if a student meets these requirements.
else, print, get out
"""

# age = 18
# country = "nigeria"
# state = "abuja"
# if age >= 18 and country == "nigeria" and state == "abuja":
#     print("You can register")
# else:
#     print("get out")

# age = 18
# country = "france"
# state = "lagos"
# if age >= 18 and country == "nigeria" or state == "abuja":
#     print("You can register")
# else:
#     print("get out")

# user_country = input("what country are you from?: ").capitalize()

# if user_country == "Nigeria":
#     print("welcome to Nigeria")

# elif user_country == "Ghana":
#     print("welcome to Ghana")

# elif user_country == "Mali":
#     print("Welcome to mali")

# else:
#     print("Get Lost")

# user_id = input("what id do you have? (bvn/nin/passport id)").lower()

# if user_id == "bvn":
#     print("Ok great, let's set up your account with your bvn")
#     user_bvn = int(input("Type in your bvn: "))
#     phone_number = int(input("Type in your phone number: "))
#     full_name = input("Type in your first name and last name: ")
#     bank_name = "Adaeze bank"

#     #user account info
#     user_account_number = user_bvn + phone_number
#     # print("Congrats your account name is: " + full_name + "\nand your bank name is: "+ bank_name + "\nand your account number is: ", user_account_number)

#     #formatted strings
#     print(f"Congratulations your name is: {full_name}\nand your account number is: {user_account_number}\nand your bank name is: {bank_name}")

# elif user_id == "nin":
#     print("Ok great, let's set up your account with your nin")

# elif user_id == "passport id" or user_id == "passport" or user_id == "pass":
#     print("Ok great, let's set up your account with your passport")

# else:
#     print("You need to have a valid id")

# small_shawarma = 1000
# medium_shawarma = 1500
# large_shawarma = 2000

# one_sausage = 300
# double_sausage = 600

# total_bill = 0
# customer_choice = input("What size of shawarma do you want? (small/medium/large): ").lower()

# if customer_choice == "small":
#     number_of_sausages = int(input("how many sausages do you want? please type 1 or 2: "))
#     if number_of_sausages == 1:
#         total_bill = total_bill + small_shawarma + one_sausage
#     elif number_of_sausages == 2:
#         total_bill = small_shawarma + double_sausage
#     else:
#         print("You can only select two sausages")

#     print(f"Your total bill is: {total_bill} naira")

# elif customer_choice == "medium":
#     number_of_sausages = int(input("how many sausages do you want? please type 1 or 2: "))

#     if number_of_sausages == 1:
#         total_bill = total_bill + medium_shawarma + one_sausage
#     elif number_of_sausages == 2:
#         total_bill = medium_shawarma + double_sausage
#     else:
#         print("You can only select two sausages")
    
#     print(f"Your total bill is: {total_bill} naira")


#list is an ordered collection of items. it is indexeable, mutable, allows duplicates and ordered

# shopping_cart = ["plantain chips", "Youghurt", "Cake", "Youghurt"]
# print(shopping_cart)

# items = ["plantain chips", "Youghurt", "Cake", "Youghurt", 1, 2.3, [1,2,3,4, [5,6,7]]]
# print(items)

#indexing starts from 0
#lets print the second item
# print(items[1])
# print(items[2])

#list slicing is used to select some items out of the entire list
# print(items[0:3])
# print(items[2:4])

# print(items[6])
# print(items[6][2])

# print(items[6][4][1:])

#append method to add elements to a list
# items = []

# items.append("banana")
# items.append("cake")
# items.append("orange")

# items.remove("cake")
# items.insert(0, "pawpaw")
# print(items)

# dict_1 = {"name":"samuel", "age":20, "class":"ss3"}
# print(dict_1["name"])
# print(dict_1["class"])
# print(dict_1["age"])


#create a dict with name, age, country and class
# print all the keys
# print all the values
# change the value of country to france
# remove age from the dictionary
# print the dictionary


# dict_2 = {"name":"adaeze", "age": 29, "country": "australia", "class":"ss2"}
# print(dict_2)
# print(dict_2.values())
# dict_2["country"] = "france"
# dict_2.pop("age")
# print(dict_2)

# set1 ={"orange", "mango", "fikayo", "cat"}  #set is used to store unique items
# #set1.add ("chizey")
# set1.add("chizey")
# set1.remove("orange")
# print(set1)


# my_dict = {"small": 1000, "medium": 1500, "large": 2000, "one_sausage": 300, "two_sausage": 600} 
# print(f"Here is our price list:\n {my_dict}")

# shawarma_size = input("what size of shawarma do you want?: ")
# no_of_sausage = input("how many sausages do you want?: ")

# total_bill = 0
# user_size = my_dict[shawarma_size]
# user_sausage = my_dict[no_of_sausage]
# print(user_size)

# #calculate the total bill
# total_bill = user_size + user_sausage 
# print(f"your total bill is: {total_bill} naira")

#creating conditions




#in python we have "for" loops and "while" loops, loops allows you to run something repeatedly
#you can repeat a code over and over again
#when you want to craete a range or define how many times you want a code to run, 
#you use the range function

# for a in range(100):
#     print("my name is adaeze")

# for b in range(20, 51):
#     print(b)

# for a in range(100, 301):
#     print(a)

# for b in range(2, 11, 3):
#     print(b)

# for b in range(5, 100, 5):
#     print(b)

# total=0
# for number in range(1, 11):
#     print(f"i am adding {number} to total")
#     total = total + number
# print(total)

# total=0
# for number in range(2, 101, 2):
#     print(f"i am adding {number} to total")
#     total = total + number
# print(total)

#create two times table using a for loop, starts from 2 to 30


# "hint use formatted strings for the output, there is muliplication somewhere


# for number in range(2, 31):
#     print(f"5 x {number} = {5*number}")

# while True:
#     state = input("Enter a state: ")
#     if state ==  "hit":
#         print("Game over")
#         break
#     else:
#         print("You are in " + state)

#What are functions? a function is a set of instructions that perfom a specific task
#function to convert dollar to naira. 
#how to write function in python. any function in python has to follow with parathensis()
#float- are decimal numbers, int- are whole numbers

# def convert_to_naira():
#     print("100 dollar is 36,000 naira")

# for i in range(20):
#     convert_to_naira()

# def convert_to_naira():
#     amount = float(input("Enter amount in dollars: "))
#     naira = amount * 1500
#     print(f"${amount} is equivalent to N{naira}")

# convert_to_naira()  #(call out function)

#The function above does not tak in parameters 
#parameter is the name of the input your function accept ( e.g currency)
#while an argument, when you call the function. it's an arguent

# def convert_to_naira(amount):
#     naira = amount * 1500
#     print(f"${amount} is equivalent to N{naira}")
# # convert_to_naira(amount= 120)
# convert_to_naira(100)

# def convert_to_naira(amount, currency):    #two parameters here(amount and currency)
#     if currency == "USD":
#         naira = amount * 1500
#         print(f"${amount} is equivalent to N{naira}")
#     elif currency == "EUR":
#         naira = amount * 1567
#         print(f"€{amount} is equivalent to N{naira}")
#     elif currency == "GBP":
#         naira = amount * 1900
#         print(f"£{amount} is equivalent to N{naira}")

# convert_to_naira(amount= 100, currency="USD")
# convert_to_naira(amount= 100, currency="EUR")
# convert_to_naira(amount= 100, currency="GBP")

#write a python function that will take a number and length and prints 
#the multiplication table of the number up to the given length

# def multiplication_table(number = 2, length = 10):
#     for num in range(1, length+1, 2):
#         print(f"{number} X {num} = {number*num}")
# multiplication_table(2, 10)

# def multiplication_table(a, b):
#     result = a * b
#     return result

# result = multiplication_table(5, 10)
# print(result)


"""
create a python function that will take a number and checks if the number is even or not. 
if the number is even, the functin should return true, otherwise it should return false
"""
# def even_number_checker(number):
#     if number % 2 == 0:               #percentage sign returns the remainder when a number is divided
#         return True
#     else:
#         return False
    
# result = even_number_checker(3)
# print(result)



"""
how do you create an object in python 
"""
class Dog:
    def __init__(self, name, color, gender):
        self.name = name
        self.color = color
        self.gender = gender
    def __str__(self):
        return f"The name of the dog is: {self.name}\n \
              And it is a {self.gender} dog\n \
                and it is {self.color} in color"

    def change_properties(self, new_name, new_color, new_gender):
        self.name = new_name
        self.color = new_color
        self.gender = new_gender 

    
    #dding actions or methods
    def bark(self):
        return f"{self.name} is barking woof! woof!"
    def eat(self):
        return f"{self.name} is eating munch! munch!"
    def walk(self):
        return f"{self.name} is walking"
    

#creating an instance of the class Dog
dog1 = Dog(name="Rotweiler", color="brown", gender="male")
dog2 = Dog(name="German Shepherd", color="black", gender="female")
dog3 = Dog(name="Pitbull", color="white", gender="male")

dog1.change_properties(new_name="pitbull", new_color="red", new_gender="female")

print(dog1)
# print(dog2)
# print(dog3)
# print (dog1.eat())
# print (dog2.eat())

#OOP helps you model real life objects in codes
#when you want custom print messages use  (def __str__(self):) in class
#when you want to initialize a class use __init__(self, name

