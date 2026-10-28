from brezyweather.alerts import wind_alert
from brezyweather.units import celsius_to_fahrenheit, kmh_to_mph


def build_forecast(city, temp_c, wind_kmh):
    return {
        "city": city,
        "temp_c": temp_c,
        "temp_f": celsius_to_fahrenheit(temp_c),
        "wind_mph": kmh_to_mph(wind_kmh),
        "alert": wind_alert(wind_kmh),
    }
