def display_menu():
    print("Shopping List Manager")
    print("1. Add Item")
    print("2. Remove Item")
    print("3. View List")
    print("4. Exit")

def main():
    shopping_list = []
    while True:
        display_menu()
        choice = input("Enter your choice: ")

        if choice == '1':
            added_item = input("Enter the item to add: ")
            shopping_list.append(added_item)
            print("Item added successfully!")
            # Prompt for and add an item
            pass
        elif choice == '2':
            # here I will use the try/except for robust removal
            removed_item = input("What item would you delete? ")
            try: 
                shopping_list.remove(removed_item)
                print("Item deleted successfully.")
            except ValueError:
                print("Sorry! The item is not in the shopping list.")
            
                # Prompt for and remove an item
            pass
        elif choice == '3':
            print(f"Your current shopping list includes: {shopping_list}")
            # Display the shopping list
            pass
        elif choice == '4':
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()