import webbrowser
import math
import time

kerbinDay = int(input("Kerbin day: "))
number = kerbinDay / 426.0
earthDay = math.floor(number * 365)
print(str(earthDay) + "th day of year")
webbrowser.open("https://www.google.com/search?q=" + str(earthDay) + "th+day+of+the+year")
time.sleep(5)