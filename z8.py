import ephem
import datetime
now = datetime.datetime.now()
mars = ephem.Venus(now)
print(ephem.constellation(mars))
