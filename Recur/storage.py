import json

def save_unit(name):
    with open("units.json", "w") as f:
        json.dump(name, f)

def load_unit():
    with open("units.json", "r") as f:
        return json.load(f)

def load_instance(unit):
    units = load_unit()
    return units[unit]["instances"]

def create_unit(name):
    x = load_unit()
    x[name] = {"instances": []}
    save_unit(x)

def delete_unit(name):
    x = load_unit()
    del x[name]
    save_unit(x)

def list_units():
    x = load_unit()
    print(**x)

def add_instance(unit, app):
    units = load_unit()
    units[unit]["instances"].append(app)
    save_unit(units)

def remove_instance(unit, app):
    units = load_unit()
    units[unit]["instances"].remove(app)
    save_unit(units)