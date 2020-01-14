import json
seattle_stationcode = 'GHCND:US1WAKG0038'
# Loading the .json file into python
with open('ucaccmet2j_python/precipitation.json', encoding='utf8') as file:
    data = json.load(file)

precipitation = []
for measurement in data:
    if (measurement['station']) == seattle_stationcode:
        print(measurement['value'])
            
        # measurement_month = sum(precipitation)
