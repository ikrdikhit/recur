from ProjectX import storage

# Test: create some units
print(storage.create_unit("study"))   # Should print: True
print(storage.create_unit("study"))   # Should print: False (already exists)
print(storage.create_unit("work"))    # Should print: True

# Test: list all units
print(storage.list_units())           # Should print: ['study', 'work']

# Test: get one unit
print(storage.get_unit("study"))      # Should print the study dict

# Test: delete a unit
print(storage.delete_unit("work"))    # Should print: True
print(storage.list_units())           # Should print: ['study']