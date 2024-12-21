capitals = {
    "France": "Paris",
    "Germany": "Berlin",
}

# Nested List in Dictionary

travel_log = {
    "France": ["Paris", "Lille", "Dijon"],
    "Germany": ["Berlin", "Hamburg", "Stuttgart"],
}

print(travel_log["France"][1])

nested_lst = ['A', 'B', ['C', 'D']]

print(nested_lst[-1][-1])

travel_log_dict = {
    "France": {'num_visited': 12, 
               "cities_visited": ["Paris", "Lille", "Dijon"]
              },
    "Germany": {'num_visited': 5,
                "cities_visited": ["Berlin", "Hamburg", "Stuttgart"]
               },
}

print(travel_log_dict["France"]["cities_visited"])
