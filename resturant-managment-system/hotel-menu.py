# adding item and price using dictionary
menu={
    "pizza":2000,
    "chicken burger":250,
    "zinger burger":350,
    "chai":40,
    "coffee":100,
    "salad":50,
    "pasta":120,

}

# greeting customer
print("Welcome to PYTHON Resturant!")
for item, price in menu.items():
    print(f" {item:<15}:    Rs.{price}")

order_total=0;
ordered_items=[];

item_1=input("Enter your item you want to order!=")
item_1.lower()
if item_1 in menu:
    order_total+=menu[item_1]
    ordered_items.append(item_1)
    print(f"your order of {item_1} has been placed")
    while True:
        choice = input("Do you want to add another item? (yes or no): ").strip().lower()
        if choice == 'yes':
            item_again=input("Enter another item item you want to order! ")
            if item_again in menu:
                 order_total+=menu[item_again]
                 ordered_items.append(item_again)
                 print(f"your order of {item_1} has been placed")
            else: 
                print(f"Sorry Sir! {item_again} is not available right now") 
        else:         
         break  
            
else:
    print(f"Sorry Sir! {item_1} is not available right now")
        

# creating bill with item ,price of item and total amount
print("ordered Items are:")
for item in ordered_items:
    print(f"{item:<20} Rs.{menu[item]:4.2f}")
GST=(16/100)*order_total

print(f"\n16% General sales tax is:{GST:7.0f}\nyour Total bill including GST is {order_total+GST:4.0f}")     