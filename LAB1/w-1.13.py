cities = {
    'New York': [32, 25, 30, 28, 35],
    'Los Angeles': [75, 68, 72, 70, 80],
    'New York': [20, 18, 22, 25, 15]
}

averages = {city: sum(temps) / len(temps) for city, temps in cities.items()}
print("Average temperatures:", averages)