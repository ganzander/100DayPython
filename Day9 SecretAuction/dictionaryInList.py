country = input("Enter the country name: ") 
visits = int(input("Enter the number of visits: "))
list_of_cities = eval(input("Enter the list of cities: "))

travel_log = [
  {
    "country": "France",
    "visits": 12,
    "cities": ["Paris", "Lille", "Dijon"]
  },
  {
    "country": "Germany",
    "visits": 5,
    "cities": ["Berlin", "Hamburg", "Stuttgart"]
  },
]

def add_new_country(country, visits, list_of_cities):
    travel_log.append({
        "country":country,
        "visits":visits,
        "cities":list_of_cities
    })


add_new_country(country, visits, list_of_cities)

# country = Brazil
# visits = 2
# list_of_cities = ["Sao Paulo", "Rio de Janeiro"]

print(f"I've been to {travel_log[2]['country']} {travel_log[2]['visits']} times.")
print(f"My favourite city was {travel_log[2]['cities'][0]}.")