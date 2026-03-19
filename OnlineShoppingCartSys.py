# Shopping Cart System

cart = []  # list (sequence)

def add_item():
    name = input("Enter item name: ")
    price = float(input("Enter price: "))
    
    # tuple (fixed item data)
    item = (name, price)
    
    cart.append(item)
    print("Item added!\n")


def view_cart():
    if not cart:
        print("Cart is empty\n")
    else:
        total = 0
        for item in cart:
            print(f"Item: {item[0]}, Price: {item[1]}")
            total += item[1]
        print(f"Total: {total}\n")


def remove_item():
    name = input("Enter item name to remove: ")
    
    for item in cart:
        if item[0] == name:
            cart.remove(item)
            print("Item removed\n")
            return
    
    print("Item not found\n")


def unique_items():
    # set (unique item names)
    names = {item[0] for item in cart}
    print("Unique items:", names, "\n")


def main():
    while True:
        print("1.Add 2.View 3.Remove 4.Unique 5.Exit")
        choice = input("Enter choice: ")
        
        if choice == "1":
            add_item()
        elif choice == "2":
            view_cart()
        elif choice == "3":
            remove_item()
        elif choice == "4":
            unique_items()
        elif choice == "5":
            break
        else:
            print("Invalid choice\n")

main()