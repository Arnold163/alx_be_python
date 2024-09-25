def display_menu():
    print("Shopping List Manager")
    print("1. Add Item")
    print("2. Remove Item")
    print("3. View List")
    print("4. Exit")

def add_item(shopping_list):
    """Add an item to shopping list"""
    item=input("Enter the item to add: ").strip()
    shopping_list.append(item)
    print(f"'{item}' has been added to your shopping list.")

def remove_item(shopping_list):
    """" Remove an item from the shopping list."""
    item = input("Enter the name of the item to remove:").strip()
    if item in shopping_list:
        shopping_list.remove(item)
        print(f"'{item}' is not in your shopping list.")
    else:
        print(f"'{item}' is not in your shopping list.")

def view_list(shopping_list):
    """" display all items in the shopping list:"""
    if shopping_list:
        print("\nYour shopping list:")
        for index, item in enumerate(shopping_list, start=1):
            print(f"{index}. {item}")
    else:
        print("your shopping list is currently empty.")

def main():
    shopping_list = []
    while True:
        display_menu()
        choice = input("Enter your choice: ")

        if choice == '1':
            # Prompt for and add an item
            pass
        elif choice == '2':
            # Prompt for and remove an item
            pass
        elif choice == '3':
            # Display the shopping list
            pass
        elif choice == '4':
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()