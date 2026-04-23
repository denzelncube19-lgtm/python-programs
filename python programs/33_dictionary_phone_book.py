# Phone Book using Dictionary
phone_book = {}
while True:
    print("\n1. Add Contact  2. Search  3. Delete  4. Show All  5. Exit")
    choice = input("Choose: ")
    if choice == '1':
        name = input("Name: ")
        number = input("Phone: ")
        phone_book[name] = number
        print("Contact added!")
    elif choice == '2':
        name = input("Search name: ")
        print(f"Phone: {phone_book.get(name, 'Not found')}")
    elif choice == '3':
        name = input("Delete name: ")
        if name in phone_book:
            del phone_book[name]
            print("Deleted!")
        else:
            print("Not found")
    elif choice == '4':
        for name, num in phone_book.items():
            print(f"  {name}: {num}")
    elif choice == '5':
        break
