def is_temperature_warm(temperature : float)  -> str:
    if temperature >= 20:
        return True
    if temperature < 20:
        return False

print(is_temperature_warm(19))