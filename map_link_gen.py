#https://www.google.com/maps/search/pizza+near+New+York,+NY
all_cities = ["New York, NY", "Los Angeles, CA"]
base = "https://www.google.com/maps/search/"
term = "pizza"
for i in range(len(all_cities)):
    city = ("+").join(all_cities[i].split(" "))
    link = base+term+"+near+"+city
    print(link)
