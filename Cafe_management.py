# Define the menu of restaurant
menu={
    "Pizza" : 40,
    "Pasta" : 50,
    "Burger" : 60,
    "Salad" : 50,
    "Coffee" : 10
}

#Greet
print("Welcome to PYHTON Restaurant")
print("Pizza : 40\nPasta : 50\nBurger : 60\nSalad : 50\nCoffee : 10")

order_total = 0

item_1=input("Enter the name of item: ")
if item_1 in menu:
    order_total += menu[item_1]
    print("Your item {item_1} has been selected")
else:
    print("Ordered item {item_1} is not available")
    print("Please select something from the menu")

another_order=input("Do you want to order anything else (Yes/No): ")
if another_order == "Yes":
    item_2=input("Enter the name of item: ")
    if item_2 in menu:
        order_total += menu[item_2]
    print("Your item {item_2} has been selected")
else:
    print("Ordered item {item_2} is not available")
    print("Please select something from the menu")

print("Total Amount of Your Order: ", order_total)