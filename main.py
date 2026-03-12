from Recur import storage
import sys


print('''
    === RECUR IS RUNNING ===
    1. Create Units 
    2. Delete Units
    3. List Units
    4. Add Instance
    5. Remove Instance
    6. Launch Unit
    q. Quit
''')
while True:
    units = storage.load_unit()
    x = input("Enter (identifier): ")

    if x == "1":
        while True:
            y = input("Enter unit name: ")
            if y in units:
                print(f"{y} already exists.")
                continue
            else:
                storage.create_unit(y)
                sys.exit(f"{y} is created.")
    
    elif x == "2":
        while True:
            y = input("Enter unit name: ")
            if not y in units:
                print(f"{y} does not exists.")
                continue
            else: 
                storage.delete_unit(y)
                sys.exit(f"{y} is deleted.")
    
    elif x == "3":
        print(list(units.keys()))
        break

    # Add instance
    elif x == "4":
        while True:
            y = input("Enter unit: ")
            if y in units: 
                z = input("Enter instance to add: ")
                storage.add_instance(y, z)
                print(f"Instance {z} added to unit {y}")
                break
            print("Not a valid unit.")
            continue

    # Remove instance
    elif x == "5":
        while True:
            y = input("Enter unit: ")
            if y in units: 
                instances = storage.load_instance(y)
                while True:
                    z = input("Enter instance to remove: ")
                    if z in instances:
                        storage.remove_instance(y, z)
                        print(f"Instance {z} removed from unit {y}")
                        break
                    print(f"Instance {z} does not exist.")
            elif y not in units:
                print("Not a valid unit.")
            break

    elif x == "6":
        while True:
            y = input("Enter unit: ")
            if y in units:
                storage.launch_unit(y)
                print(f"Unit {y} launched.")
                break
            else:
                print(f"Unit {y} does not exist.")

    elif x == "q":
        sys.exit("Quitting Recur...")
    
    else:
        print("Please enter a correct identifier.")

    break