import json
import csv

file = open('page1_25games.json')
stats = json.load(file)



for item in range(len(stats['data'])):
    print('Map:',str(stats['data'][item]['details']['map']['name']),
    "Gametype:",str(stats['data'][item]['details']['category']['name']),
    "Kills:",str(stats['data'][item]['stats']['summary']['kills']),
    "Deaths:",str(stats['data'][item]['stats']['summary']['deaths']),
    "Assists:",str(stats['data'][item]['stats']['summary']['assists']),
    "KDR:",str(stats['data'][item]['stats']['kdr']),
    "Proficiency:",round(stats['data'][item]['stats']['damage']['dealt'])/
    (stats['data'][item]['stats']['damage']['taken']),
    "Accuracy:",str(stats['data'][item]['stats']['shots']['accuracy']))
