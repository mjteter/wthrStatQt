# Weather Station GUI for 3.5" PiTFT

This code is for a 3.5" touchscreen for the Raspberry Pi and makes API calls to Weather Underground.

## Table of Contents
[Software](#software)
[Installation](#installation)
[Resources](#resources)

### Software
* [QT 5.7][qt] () - gui framework
* [Python 3.5.2][python]
* [PyQt 5.7][pyqt]
* [PyCharm][pycharm]

### Installation


### Resources

#### Settings
##### labelDict.json
This json contains the dictionary for what the front end should display for both current and next cycle forecasts. The following are options (duplicates are allowed).

| Current    |           |          |
| ---------- | --------- | -------- |
| temp       | wet_bulb  | pressure |
| dewpoint   | wind      | enthalpy |
| heat_index | wind_gust | rel_hum  |
| wind_chill | wind_dir  | hum_rat  |
| feelslike  | wind_deg  | uv       |

| Forecast     |              |              |
| ------------ | ------------ | ------------ |
| high_t       | low_t        |              |
| max_wind_spd | max_wind_dir | max_wind_deg |
| avg_wind_spd | avg_wind_dir | avg_wind_deg |
| avg_hum      | max_hum      | min_hum      |



[qt]: https://www.qt.io/
[python]: https://www.python.org/downloads/release/python-352/
[pyqt]: https://pypi.python.org/pypi/PyQt5
[pycharm]: https://www.jetbrains.com/pycharm/