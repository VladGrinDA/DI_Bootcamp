# 🌟 Exercise 3: Zara
# Instructions
# Here is some information about a brand.
# name: Zara 
# creation_date: 1975 
# creator_name: Amancio Ortega Gaona 
# type_of_clothes: men, women, children, home 
# international_competitors: Gap, H&M, Benetton 
# number_stores: 7000 
# major_color: 
#     France: blue, 
#     Spain: red, 
#     US: pink, green


# 2. Create a dictionary called brand which value is the information from part one (turn the info into keys and values).
# The values type_of_clothes and international_competitors should be a list. The value of major_color should be a dictionary.
# 3. Change the number of stores to 2.
# 4. Print a sentence that explains who Zaras clients are.
# 5. Add a key called country_creation with a value of Spain.
# 6. Check if the key international_competitors is in the dictionary. If it is, add the store Desigual.
# 7. Delete the information about the date of creation.
# 8. Print the last international competitor.
# 9. Print the major clothes colors in the US.
# 10. Print the amount of key value pairs (ie. length of the dictionary).
# 11. Print the keys of the dictionary.
# 12. Create another dictionary called more_on_zara with the following details:

# creation_date: 1975 
# number_stores: 10 000


# 13. Use a method to add the information from the dictionary more_on_zara to the dictionary brand.
# 14. Print the value of the key number_stores. What just happened ?

# 1
brand = {
    "name": "Zara",
    "creation_date": 1975,
    "creator_name": "Amancio Ortega Gaona",
    "type_of_clothes": ["men", "women", "children", "home"],
    "international_competitors": ["Gap", "H&M", "Benetton"],
    "number_stores": 7000,
    "major_color": {
        "France": "blue",
        "Spain": "red",
        "US": ["pink", "green"]
    }
}

# 2
brand["number_stores"] = 2

# 3
print("3: Zara's clients are men, women, children, and home shoppers.")

# 4
brand["country_creation"] = "Spain"

# 5
if "international_competitors" in brand:
    brand["international_competitors"].append("Desigual")

# 6
del brand["creation_date"]

# 7
print("7: The last international competitor is:", brand["international_competitors"][-1])

# 8
print("8: The major clothes colors in the US are:", brand["major_color"]["US"])

# 9
print("9: The number of key-value pairs in the dictionary is:", len(brand))

# 10
print("10: The keys of the dictionary are:", brand.keys())

# 11
more_on_zara = {
    "creation_date": 1975,
    "number_stores": 10000
}

# 12
brand.update(more_on_zara)

# 13
print("13: The value of the key number_stores is:", brand["number_stores"])
