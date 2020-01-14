import json
seattle_stationcode = 'GHCND:US1WAKG0038'
# Loading the .json file into python
with open('ucaccmet2j_python/precipitation.json', encoding='utf8') as file:
    data = json.load(file)
month_dict = {}
for measurement in data:
    if (measurement['station']) == seattle_stationcode:
        month = measurement['date'][5:7]
        precipitation = int(measurement['value'])
    # Creating a dictionary with 'key' = month and 'value' = values
        if month in month_dict.keys():
            month_dict[month] += precipitation
        else:
            month_dict[month] = precipitation
month_list = list(month_dict.values())

with open('seattlerainfall.json', 'w', encoding='utf8') as file:
    json.dump(month_list, file)
    
     # Part 2
precipitation_year = sum(month_list)
print(precipitation_year)
    # relative precipitation per month
precipitation_month = [x / precipitation_year for x in month_list] 
print(precipitation_month)
# Saving part 2 as .json file
with open('seattle_rainfall_year.json', 'w', encoding='utf8') as file:
    json.dump(precipitation_month, file)