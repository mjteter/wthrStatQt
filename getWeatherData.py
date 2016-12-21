import urllib.request
import json
import time
import os
from CoolProp import HumidAirProp  # import HAProps


DEGREE_SIGN = u'\N{DEGREE SIGN}'


class AllWeatherData:
    def __init__(self, key_loc):
        self.metric_units = False
        self.current_data = {'temp': 'Na', 'dewpoint': 'Na', 'heat_index': 'Na', 'wind_chill': 'Na', 'feels_like': 'Na',
                             'wet_bulb': 'Na', 'wind': 'Na', 'wind_gust': 'Na', 'pressure': 'Na', 'enthalpy': 'Na',
                             'rel_hum': 'Na', 'wind_dir': 'Na', 'wind_deg': 'Na', 'uv': 'Na', 'hum_rat': 'Na'}
        self.forecast_data = {'period1': {'high_t': 'Na', 'low_t': 'Na', 'max_wind_spd': 'Na', 'max_wind_dir': 'Na',
                                          'max_wind_deg': 'Na', 'avg_wind_spd': 'Na', 'avg_wind_dir': 'Na',
                                          'avg_wind_deg': 'Na', 'avg_hum': 'Na', 'max_hum': 'Na', 'min_hum': 'Na'},
                              'period2': {'high_t': 'Na', 'low_t': 'Na', 'max_wind_spd': 'Na', 'max_wind_dir': 'Na',
                                          'max_wind_deg': 'Na', 'avg_wind_spd': 'Na', 'avg_wind_dir': 'Na',
                                          'avg_wind_deg': 'Na', 'avg_hum': 'Na', 'max_hum': 'Na', 'min_hum': 'Na'},
                              'period3': {'high_t': 'Na', 'low_t': 'Na', 'max_wind_spd': 'Na', 'max_wind_dir': 'Na',
                                          'max_wind_deg': 'Na', 'avg_wind_spd': 'Na', 'avg_wind_dir': 'Na',
                                          'avg_wind_deg': 'Na', 'avg_hum': 'Na', 'max_hum': 'Na', 'min_hum': 'Na'},
                              'period4': {'high_t': 'Na', 'low_t': 'Na', 'max_wind_spd': 'Na', 'max_wind_dir': 'Na',
                                          'max_wind_deg': 'Na', 'avg_wind_spd': 'Na', 'avg_wind_dir': 'Na',
                                          'avg_wind_deg': 'Na', 'avg_hum': 'Na', 'max_hum': 'Na', 'min_hum': 'Na'},
                              'period5': {'high_t': 'Na', 'low_t': 'Na', 'max_wind_spd': 'Na', 'max_wind_dir': 'Na',
                                          'max_wind_deg': 'Na', 'avg_wind_spd': 'Na', 'avg_wind_dir': 'Na',
                                          'avg_wind_deg': 'Na', 'avg_hum': 'Na', 'max_hum': 'Na', 'min_hum': 'Na'},
                              'period6': {'high_t': 'Na', 'low_t': 'Na', 'max_wind_spd': 'Na', 'max_wind_dir': 'Na',
                                          'max_wind_deg': 'Na', 'avg_wind_spd': 'Na', 'avg_wind_dir': 'Na',
                                          'avg_wind_deg': 'Na', 'avg_hum': 'Na', 'max_hum': 'Na', 'min_hum': 'Na'},
                              'period7': {'high_t': 'Na', 'low_t': 'Na', 'max_wind_spd': 'Na', 'max_wind_dir': 'Na',
                                          'max_wind_deg': 'Na', 'avg_wind_spd': 'Na', 'avg_wind_dir': 'Na',
                                          'avg_wind_deg': 'Na', 'avg_hum': 'Na', 'max_hum': 'Na', 'min_hum': 'Na'},
                              'period8': {'high_t': 'Na', 'low_t': 'Na', 'max_wind_spd': 'Na', 'max_wind_dir': 'Na',
                                          'max_wind_deg': 'Na', 'avg_wind_spd': 'Na', 'avg_wind_dir': 'Na',
                                          'avg_wind_deg': 'Na', 'avg_hum': 'Na', 'max_hum': 'Na', 'min_hum': 'Na'},
                              'period9': {'high_t': 'Na', 'low_t': 'Na', 'max_wind_spd': 'Na', 'max_wind_dir': 'Na',
                                          'max_wind_deg': 'Na', 'avg_wind_spd': 'Na', 'avg_wind_dir': 'Na',
                                          'avg_wind_deg': 'Na', 'avg_hum': 'Na', 'max_hum': 'Na', 'min_hum': 'Na'},
                              'period10': {'high_t': 'Na', 'low_t': 'Na', 'max_wind_spd': 'Na', 'max_wind_dir': 'Na',
                                           'max_wind_deg': 'Na', 'avg_wind_spd': 'Na', 'avg_wind_dir': 'Na',
                                           'avg_wind_deg': 'Na', 'avg_hum': 'Na', 'max_hum': 'Na', 'min_hum': 'Na'}}
        try:
            self.wu_key = open(key_loc, 'r').read()
        except FileNotFoundError:
            print('NO WEATHER UNDERGROUND API KEY!  PROGRAM HALTED!')
            while True:
                pass

    def update_current_data(self):
        print('start connection at', time.time())
        json_string = urllib.request.urlopen('http://api.wunderground.com/api/' + self.wu_key +
                                             '/conditions/q/PA/West_chester.json').read().decode('utf8')

        parsed_json = json.loads(json_string)
        print('fired at', time.time(), 'from', parsed_json['current_observation']['observation_location']['city'])

        if not self.metric_units:
            self.current_data['temp'] = str_float_2_str(parsed_json['current_observation']['temp_f'], '%.0f')
            self.current_data['dewpoint'] = str_float_2_str(parsed_json['current_observation']['dewpoint_f'], '%.0f')
            self.current_data['heat_index'] = str_float_2_str(parsed_json['current_observation']['heat_index_f'],
                                                              '%.0f')
            self.current_data['wind_chill'] = str_float_2_str(parsed_json['current_observation']['windchill_f'], '%.0f')

            self.current_data['feels_like'] = str_float_2_str(parsed_json['current_observation']['feelslike_f'], '%.0f')
            self.current_data['wind'] = str_float_2_str(parsed_json['current_observation']['wind_mph'], '%.f')
            self.current_data['wind_gust'] = str_float_2_str(parsed_json['current_observation']['wind_gust_mph'], '%.f')
            self.current_data['pressure'] = str_float_2_str(parsed_json['current_observation']['pressure_in'], '%.f')

            self.current_data['rel_hum'] = str_float_2_str(parsed_json['current_observation']['relative_humidity'],
                                                           '%.f')
            self.current_data['wind_dir'] = str_float_2_str(parsed_json['current_observation']['wind_dir'], '%.f')
            self.current_data['wind_deg'] = str_float_2_str(parsed_json['current_observation']['wind_degrees'], '%.f')
            self.current_data['uv'] = str_float_2_str(parsed_json['current_observation']['UV'], '%.f')

            HumidAirProp.HAProps()
            self.current_data['wet_bulb'] = str_float_2_str(parsed_json['current_observation'][''], '%.f')
            self.current_data['enthalpy'] = str_float_2_str(parsed_json['current_observation'][''], '%.f')
            self.current_data['hum_rat'] = str_float_2_str(parsed_json['current_observation'][''], '%.f')


def get_current_data(key):
    print('start connection at', time.time())
    json_string = urllib.request.urlopen('http://api.wunderground.com/api/' + key + '/conditions/q/PA/'
                                         'West_chester.json').read().decode('utf8')
    # print('between urllib and json at', time.time())
    parsed_json = json.loads(json_string)
    # location = parsed_json['location']['city']
    # temp_f = parsed_json['current_observation']['temp_f']
    # print "Current temperature in %s is: %s" % (location, temp_f)
    print('fired at', time.time(), 'from', parsed_json['current_observation']['observation_location']['city'])
    return parsed_json


def get_radar(key, radius=7.1, lat=39.973401, lon=-75.563591):
    urllib.request.urlretrieve('http://api.wunderground.com/api/' + key + '/radar/image.gif?centerlat=' + str(lat)
                               + '&centerlon=' + str(lon) + '&radius=' + str(radius) +
                               '&width=300&height=300&newmaps=1', os.getcwd() + '/resources/temp/radar.gif')


def cur_data_2_string(parsed_json, json_id, units='imperial', include_units=False):
    # converts weather data to string, making it all pretty
    data = ''
    str_units = ''

    try:
        if units == 'imperial':
            if json_id in ('temp_f', 'dewpoint_f', 'heat_index_f', 'windchill_f', 'feelslike_f', 'wetbulb_f'):
                str_units = ' ' + DEGREE_SIGN + 'F'

                if json_id == 'wetbulb_f':
                    data = 'NA'
                else:
                    data = str_float_2_str(parsed_json['current_observation'][json_id], '%.0f')
            elif json_id in ('wind_mph', 'wind_gust_mph'):
                str_units = ' mph'
                data = str_float_2_str(parsed_json['current_observation'][json_id], '%.0f')
            elif json_id == 'pressure_in':
                str_units = ' in'
                data = str_float_2_str(parsed_json['current_observation'][json_id], '%.2f')
            elif json_id == 'enthalpy_btu-lb':
                str_units = ' Btu/lb'
                data = str_float_2_str(parsed_json['current_observation'][json_id], '%.1f')
        else:  # if metric
            if json_id in ('temp_c', 'dewpoint_c', 'heat_index_c', 'windchill_c', 'feelslike_c', 'wetbulb_c'):
                str_units = ' ' + DEGREE_SIGN + 'C'

                if json_id == 'wetbulb_c':
                    pass
                else:
                    data = str_float_2_str(parsed_json['current_observation'][json_id], '%.1f')
            elif json_id in ('wind_kph', 'wind_gust_kph'):
                str_units = ' kph'
                data = str_float_2_str(parsed_json['current_observation'][json_id], '%.0f')
            elif json_id == 'pressure_mb':
                str_units = ' mb'
                data = str_float_2_str(parsed_json['current_observation'][json_id], '%.0f')
            elif json_id == 'enthalpy_kj-kg':
                str_units = ' kJ/kg'
                data = str_float_2_str(parsed_json['current_observation'][json_id], '%.1f')

        if json_id == 'relative_humidity':
            str_units = ' %'
            data = str_float_2_str(parsed_json['current_observation'][json_id], '%.0f').strip('%')
        elif json_id in ('wind_dir', 'UV'):
            data = str_float_2_str(parsed_json['current_observation'][json_id], '%.0f')
        elif json_id == 'wind_degrees':
            str_units = ' ' + DEGREE_SIGN
            data = str_float_2_str(parsed_json['current_observation'][json_id], '%.0f')
        # elif json_id in ('UV'):
        #     data = parsed_json['current_observation'][json_id]
        elif json_id == 'humidity_ratio':
            data = 'NA'

        if not include_units:
            str_units = ''

        # print('GOOD', json_id, parsed_json['current_observation'][json_id])
    except TypeError:
        data = 'NA'
        if not include_units:
            str_units = ''
        # print('ERROR', json_id, parsed_json['current_observation'][json_id])

    return str(data + str_units)


def str_float_2_str(raw_val, decimal_pts):
    try:
        return decimal_pts % float(raw_val)
    except ValueError:
        return raw_val
