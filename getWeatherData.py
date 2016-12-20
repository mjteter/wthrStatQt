import urllib.request
import json
import time
import os

DEGREE_SIGN = u'\N{DEGREE SIGN}'

def getCurrentData():
    print('start connection at', time.time())
    json_string = urllib.request.urlopen('http://api.wunderground.com/api/aa8135d64b32f422/geolookup/conditions/q/PA/West_chester.json').read().decode('utf8')
    # print('between urllib and json at', time.time())
    parsed_json = json.loads(json_string)
    # location = parsed_json['location']['city']
    # temp_f = parsed_json['current_observation']['temp_f']
    # print "Current temperature in %s is: %s" % (location, temp_f)
    print('fired at', time.time(), 'from', parsed_json['current_observation']['observation_location']['city'])
    return parsed_json


def getRadar(radius=7.1, lat=39.973401, lon=-75.563591):
    urllib.request.urlretrieve('http://api.wunderground.com/api/aa8135d64b32f422/radar/image.gif?centerlat=' + str(lat)
                               + '&centerlon=' + str(lon) + '&radius=' + str(radius) +
                               '&width=300&height=300&newmaps=1', os.getcwd() + '/resources/temp/radar.gif')

def data2string(parsed_json, jsonId, units='imperial'):
    # converts weather data to string, making it all pretty
    data = ''
    if units=='imperial':
        if jsonId in ('temp_f', 'dewpoint_f', 'heat_index_f', 'windchill_f', 'feelslike_f', 'wetbulb_f'):
            if jsonId in ('wetbulb_f'):
                pass
            else:
                data = parsed_json['current_observation'][jsonId]

            return '%.0f' % data + ' ' + DEGREE_SIGN + 'F'
        elif jsonId in ('wind_mph', 'wind_gust_mph'):
            pass
        elif jsonId in ('pressure_in'):
            pass
        elif jsonId in ('enthalpy_btu-lb'):
            pass
    else:  # if metric
        if jsonId in ('temp_c', 'dewpoint_c', 'heat_index_c', 'windchill_c', 'feelslike_c'):
            pass
        elif jsonId in ('wind_kph', 'wind_gust_kph'):
            pass
        elif jsonId in ('pressure_mb'):
            pass
        elif jsonId in ('enthalpy_kj-kg'):
            pass


    if jsonId in ('relative_humidity'):
        pass
    elif jsonId in ('wind_dir'):
        pass
    elif jsonId in ('wind_degrees'):
        pass
    elif jsonId in ('UV'):
        pass
    elif jsonId in ('humidity_ratio'):
        pass

