import webbrowser
import math
import time

earthDay = int(input("Earth day: "))
number = earthDay / 365.0
kerbinDay = math.floor(number * 426)
print(str(kerbinDay) + "th day of year")
time.sleep(5)
