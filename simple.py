from weather import Weather, Unit

weather = Weather(unit=Unit.CELSIUS)

lookup = weather.lookup_by_location('boulder')
condition = location.condition
print(condition.text)
