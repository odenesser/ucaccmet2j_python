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
print(month_list)
with open('seattlerainfall.json', 'w', encoding='utf8') as file:
    json.dump(month_List, file)
    
        # precipitation_month = precipitation_empty.append(int(measurement['value']))
# print(sum(precipitation_month))
# print(month)

# if statement that looks at month date and go to next set and if it is same month, add the value to the list of precipitation values.