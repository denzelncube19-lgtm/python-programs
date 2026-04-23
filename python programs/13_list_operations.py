# List Operations Demo
my_list = []
print("List Operations Menu:")
print("1. Add element  2. Remove element  3. Display list  4. Exit")
while True:
    choice = input("Choose option: ")
    if choice == '1':
        item = input("Enter item to add: ")
        my_list.append(item)
        print(f"Added '{item}'")
    elif choice == '2':
        item = input("Enter item to remove: ")
        if item in my_list:
            my_list.remove(item)
            print(f"Removed '{item}'")
        else:
            print("Item not found")
    elif choice == '3':
        print(f"List: {my_list}")
    elif choice == '4':
        break
