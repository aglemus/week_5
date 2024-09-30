# dictionary = a collection of {key:value} pairs ordered and changeable. No duplicates.
capitals = {"USA": "Washington D.C.", 
            "India": "New Delhi",
            "China": "Beijing",
            "Russia": "Moscow"}
# print(dir(capitals))
# print(help(capitals))
# print(capitals.get("Japan"))
# if capitals.get("Japan"):
#    print("That capital exsists")
# else:
#    print("That capital doesnt exist")

# capitals.update({"Germanty": "Berlin"})
# capitals.update({"Germanty": "Detroit"})
# capitals.pop("China")
# capitals.popitem()
# capitals.clear()

# keys = capitals.keys()
# for key in capitals.keys():
#     print(key)

# value = capitals.values()
# for value in capitals.values():
#     print(value)

items = capitals.items()
for key, value in capitals.items():
    print(f"{key}: {value}")