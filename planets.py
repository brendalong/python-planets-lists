planet_list = ["Mercury", "Mars"]
planet_list.append("Jupiter")
planet_list.append("Saturn")

# or use insert
planet_list.insert(len(planet_list), "Pluto")

more_planets = ["Mars2", "Pluto2"]
#adds iterable to end
planet_list.extend(more_planets)

planet_list.insert(3, "Earth")
planet_list.insert(2, "Venus")

planet_list.append("Pluto")

#slice is an object applied to list
rocky_planets = planet_list[slice(3, 5, 1)]

print("rocky_planets", rocky_planets)
print("-----------")

del planet_list[len(planet_list)-1]

print("planet_list", planet_list)

#Create another list containing tuples. Each tuple will hold the name of a spacecraft that we have launched, and the names of the planet(s) that it has visited, or landed on. (e.g. ('Cassini', 'Saturn')).
#Iterate over your list of planets, and inside that loop, iterate over the list of tuples. Print, for each planet, which satellites have visited it.


rocket_ships = [("ship1", ('Pluto', 'Saturn')),("ship2",('Venus', 'Earth')), ("ship3",('Saturn', 'Pluto'))]
print("-----------")
print("rocketShips", rocket_ships)

# stuff = [1, "hello", True, "goodbye"]

# if "hello" in stuff:
#   print("Python rocks")

#options
#for each planet, create item in dictionary. loop through rocket_ships items[1] look for match.
#if match, add to newlist item
landing_list = {}
for planet in planet_list:
    #put unique items in dictionary
    landing_list[planet] = []


for item in rocket_ships:
    rocket_name = item[0]

    for planet in item[1]:
        landing_list[planet].append(rocket_name)

print("end landing_list", landing_list)

for item in landing_list:
    print(f"Planet: {item} found by {landing_list[item]}")
# for abbreviation, purchase_list in report.items():
#     total_stock_value = 0
#     for purchase in purchase_list:
#         total_stock_value += purchase[1] * purchase[3]
#         print(f"    {purchase}")
#     print(f"total val of stock {total_stock_value}\n\n")
