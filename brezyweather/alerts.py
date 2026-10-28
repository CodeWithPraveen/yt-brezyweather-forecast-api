WIND_WARNING_KMH = 60


def wind_alert(wind_kmh):
    if wind_kmh > WIND_WARNING_KMH:
        return "wind-warning"
    return None
