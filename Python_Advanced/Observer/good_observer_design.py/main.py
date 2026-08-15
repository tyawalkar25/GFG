from weather_station import WeatherStation
from mobile import Mobile
from tv_display import TVDisplay

ws = WeatherStation()
mobile = Mobile()
tv = TVDisplay()
ws.add_observer(mobile)
ws.add_observer(tv)

ws.remove_observer(mobile)

ws.update_temperature(35)
