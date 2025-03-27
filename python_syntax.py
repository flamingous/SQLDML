print("Welcome to Python Pizza Deliveries")
total_bill = 0

pizza_order = {"small_pizza": 15, "medium_pizza": 20, "large_pizza": 25, "pepperoni_small": 2, 
               "pepperoni_medium": 3, "pepperoni_large": 3}
size = input("what size of pizza do you want?: ")
add_pepperoni = input("do you want pepperoni?: ")
extra_cheese = input(" do you want extra cheese?: ")

if size not in ["small_pizza", "medium_pizza", "large_pizza"]:
    print("we only over small_pizza, medium_pizza and large_pizza")


#checking user peperoni options
if add_pepperoni == "yes" and size == "small_pizza":
    total_bill = pizza_order["pepperoni_small"] + pizza_order["small_pizza"]
elif add_pepperoni == "yes" and size == "medium_pizza":
    total_bill= pizza_order["pepperoni_medium"] + pizza_order["medium_pizza"]
elif add_pepperoni == "yes" and size == "large_pizza":
    total_bill = pizza_order["pepperoni_large"] + pizza_order["large_pizza"]

#check if user wants cheese
if extra_cheese == "yes":
    total_bill = total_bill + 1
    print(f"Your total bill is {total_bill}")
else:
    print(f"Your total bill is {total_bill}")

