# list datastructures, it is ordered and changeable ie can add different value
cars = ["Mercedes", "Nissan", "Toyota", "Land Rover"]
cars[1] = "Subaru"
cars.append("Mistubishi")
cars.insert(2, "BMW")
cars.pop(3)
cars.sort()

print(cars)
# this is a tuple, ordered, its unchangeable
fruits = ("Mangoes", "Apples", "Oranges", "Avocados", "Pineapples")
fruits.count("Avocados")
for x in fruits:
    print(x)

# sets datastructures, unordered
countries = {"Kenya", "Uganda", "Tanzania", "Ethiopia", "Burundi"}
print(countries)

# dictionaries
matunda = {
    "amount": 40,
    "jina": "Ndizi",
    "rangi": "Yellow",
}
matunda["size"] = "Large"
matunda.pop("rangi")
print(matunda)
