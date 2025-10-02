def display_menu():
    print("\nShopping List Manager")
    print("1. Add an item")
    print("2. Remove an item")
    print("3. View the list")
    print("4. Exit")


def add_item(shopping_list):
    item = input("Enter item to add: ").strip()
    if item:
        shopping_list.append(item)
        print(f"'{item}' added to the shopping list.")
    else:
        print("No item entered; nothing added.")


def remove_item(shopping_list):
    if not shopping_list:
        print("Shopping list is empty. Nothing to remove.")
        return
    item = input("Enter item to remove: ").strip()
    if not item:
        print("No item entered; nothing removed.")
        return
    # Case-insensitive search for the first matching item
    lower_list = [s.lower() for s in shopping_list]
    try:
        idx = lower_list.index(item.lower())
    except ValueError:
        print(f"'{item}' not found in the shopping list.")
    else:
        removed = shopping_list.pop(idx)
        print(f"Removed '{removed}' from the shopping list.")


def view_list(shopping_list):
    if not shopping_list:
        print("Shopping list is empty.")
        return
    print("\nCurrent shopping list:")
    for i, item in enumerate(shopping_list, 1):
        print(f"{i}. {item}")


def main():
    shopping_list = []
    while True:
        display_menu()
        choice = input("Choose an option (1-4): ").strip()
        if choice == "1":
            add_item(shopping_list)
        elif choice == "2":
            remove_item(shopping_list)
        elif choice == "3":
            view_list(shopping_list)
        elif choice == "4":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 4.")


if __name__ == "__main__":
    try:
        main()
    except (KeyboardInterrupt, EOFError):
        print("\nExiting. Goodbye!")

#create a shoplist
#!/usr/bin/env python3
"""
shopping_list_manager.py
A simple shopping list manager using a Python list and a text-menu interface.

Features:
- Start with an empty shopping_list list
- Menu to add, remove, view items, or exit
- Graceful handling of invalid menu choices
- Case-insensitive removal (removes first matching item)
- Handles KeyboardInterrupt/EOF gracefully
"""
