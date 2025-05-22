def add_item(inventory):
    name = input("Enter item name: ")
    quantity = int(input("Enter item quantity(Whole number): "))
    unit_price = float(input("Enter item unit price(float): "))
    item={
        "name": name,
        "quantity": quantity,
        "unit_price": unit_price
    }
    for item in inventory:
        if item['name'].lower() == name.lower():
            print("Updating item quantity")
            item['quantity'] += quantity
            return
    else:
        inventory.append(item)
        print("Item added to inventory")

def remove_item(inventory):
    name = input("Enter item name to remove: ")
    for item in inventory:
        if item['name'].lower() == name.lower():
            quantity = int(input("Enter item quantity(Whole number): "))
            if quantity > item['quantity']:
                print("Quantity exceeds available stock")
                return
            item['quantity'] -= quantity
            print("Item updated accordingly")
            return
    print("Item not found in inventory")

def display_invetory(inventory):
    for inv_item in inventory:
        print(inv_item['name'] + " -> " + str(inv_item['quantity']) + " -> Ugx. " + str(inv_item['unit_price']) + " each\n")
        print("-------------------------------------------")

inventory = []
# add_item(inventory, "Apples", 10, 0.5)
# display_invetory(inventory)

while True:
    try:
        choice = input("""Enter action to perform 
(1-Add Item, 2-Display Inventory list, 3-Remove item, 4-Exit): """)
        if int(choice) == 1:
            print("Adding Item")
            add_item(inventory)
        elif int(choice) == 2:
            if not inventory:
                print("No inventory")
            display_invetory(inventory)
        elif int(choice) == 3:
            print("Removing Item")
            remove_item(inventory)
        elif int(choice) == 4:
            print("Exiting program")
            break
        else:
            print("Invalid choice")
    except ValueError:
        print("Invalid input. Please enter a number(1,2 or 3).")


