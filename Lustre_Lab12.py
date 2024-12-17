def display_menu(menu):
    print("\n--- Mang Inasal Food Menu ---")
    print("Code\tItem\t\t\t\tPrice (₱)")
    print("-" * 40)
    for item in menu:
        print(f"{item['code']}\t{item['item']} - ₱{item['price']}")
    print("-" * 40)

def get_order(menu):
    selected_items = []  
    total_price = 0  

    while True:
        order_code = input("Enter the menu code of the item you want to order (Type 'done' to finish): ").upper()
        
        if order_code == "DONE":
            print("Order process finished.")
            break  
        
        item_found = False  

        for item in menu:
            if item['code'] == order_code:
                print(f"You selected: {item['item']} - ₱{item['price']}")
                selected_items.append(item)
                total_price += item['price'] 
                item_found = True
                break 

        if not item_found:
            print("Invalid menu code. Please try again.")  

    return selected_items, total_price 


def process_payment(price):
    while True:
        cash = input(f"Please enter cash amount (₱) to pay for ₱{price}: ")
        if cash.isdigit(): 
            cash = float(cash)
            if cash < price:
                print("Insufficient cash. Please try again.")
            else:
                change = cash - price
                print(f"Payment successful! Your change is: ₱{change:.2f}")
                break
        else:
            print("Invalid input. Please enter a valid numeric amount.")
menu = [
    {"code": "PM1", "item": "Paa Large (Chicken Leg and Thigh) with Rice", "price": 154},
    {"code": "PM2", "item": "Pecho Large (Chicken Breast and Wing) with Rice", "price": 184},
    {"code": "PM3", "item": "2 pcs Pork BBQ with Rice", "price": 118},
    {"code": "PM4", "item": "Bangus Sisig with Rice", "price": 154},
    {"code": "PM5", "item": "Pork Sisig with Rice", "price": 118},
    {"code": "PM6", "item": "Grilled Liempo with Rice", "price": 129},
    {"code": "PM7", "item": "Sizzling Liempo with Rice", "price": 154},
    {"code": "PM8", "item": "Palabok with 1 pc Pork BBQ", "price": 94},
    {"code": "PM9", "item": "Palabok with Chicken Inasal Regular", "price": 94},
    {"code": "PM10", "item": "1 pc Pork BBQ with Java Rice and Peanut Sauce", "price": 154},
]

display_menu(menu)
selected_items, total_price = get_order(menu)
process_payment(total_price)
print("\nThank you for ordering at Mang Inasal! Enjoy your meal!")
