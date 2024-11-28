def display_menu():
    print("\nShopping Cart Menu:")
    print("1. Add item")
    print("2. Remove item")
    print("3. View cart")
    print("4. Exit")

def add_item(cart):
    item = input("Enter the item to add: ").lower()
    if item in ["milk", "eggs", "apples", "bread", "bananas", "grapes"]:
        cart.append(item)
        print(f"{item.capitalize()} added to the cart.")
    else:
        print("Item not available.")

def remove_item(cart):
    item = input("Enter the item to remove: ").lower()
    if item in cart:
        cart.remove(item)
        print(f"{item.capitalize()} removed from the cart.")
    else:
        print("Item not in the cart.")

def view_cart(cart):
    if cart:
        print("\nItems in your cart:")
        for item in cart:
            print(f"- {item.capitalize()}")
    else:
        print("Your cart is empty.")

def main():
    cart = []
    while True:
        display_menu()
        choice = input("Choose an option: ")
        if choice == '1':
            add_item(cart)
        elif choice == '2':
            remove_item(cart)
        elif choice == '3':
            view_cart(cart)
        elif choice == '4':
            print("Exiting the program.")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()