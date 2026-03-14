from Recur import storage


print('''
    === RECUR IS RUNNING ===
    1. Create Unit
    2. Add Instance
    3. Delete Unit
    4. Remove Instance
    5. List Units
    6. List Instances
    7. Launch Unit
    q. Quit
''')


while True:
    identifier = input("Enter (identifier): ")

    # Create Unit
    if identifier == "1":
        units = storage.load_units()
        while True:
            unit = input("Unit to create: ")
            if unit in units:
                print(f"Unit {unit} already exists.")
                continue
            else:
                storage.create_unit(unit)
                print(f"Unit {unit} is created.")
                break

    # Add Instance
    elif identifier == "2":
        units = storage.load_units()
        while True:
            unit = input("Unit name: ")
            if unit in units: 
                instance = input("Instance to add: ")
                storage.add_instance(unit, instance)
                print(f"Instance {instance} added to unit {unit}")
                break
            else:
                print(f"Unit {unit} does not exist.")
                continue

    # Delete Unit
    elif identifier == "3":
        units = storage.load_units()
        while True:
            unit = input("Unit to delete: ")
            if unit in units:
                storage.delete_unit(unit)
                print(f"Unit {unit} is deleted.")
                break
            else: 
                print(f"Unit {unit} does not exist.")
                continue

    # Remove Instance
    elif identifier == "4":
        units = storage.load_units()
        while True:
            unit = input("Unit name: ")
            if unit in units: 
                instances = storage.load_instances(unit)
                while True:
                    instance = input("Instance to remove: ")
                    if instance in instances:
                        storage.remove_instance(unit, instance)
                        print(f"Instance {instance} removed from unit {unit}")
                        break
                    else:
                        print(f"Instance {instance} does not exist.")
                        continue
            else:
                print(f"Unit {unit} does not exist.")
                continue

    # List Units
    elif identifier == "5":
        units = storage.load_units()
        storage.list_units()

    # List Instances
    elif identifier == "6":
        units = storage.load_units()
        while True:
            unit = input("Unit name: ")
            if unit in units:
                storage.list_instances(unit)
                break
            else:
                print(f"Unit {unit} does not exist.")
                continue

    # Launch Unit
    elif identifier == "7":
        units = storage.load_units()
        while True:
            unit = input("Unit to launch: ")
            if unit in units:
                storage.launch_unit(unit)
                print(f"Unit {unit} launched.")
                break
            else:
                print(f"Unit {unit} does not exist.")
                continue

    # Quit
    elif identifier == "q":
        print("Quitting Recur...")
        break

    # ...
    else:
        print("Please enter a correct identifier.")