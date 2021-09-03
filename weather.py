#!C:\Users\DELL\AppData\Local\Programs\Python\Python39\python.exe
import requests
import cgi, os
from datetime import datetime

print('content-type:text/html\r\n\r\n')

form=cgi.FieldStorage()
cn=str(form.getvalue("cityname"))

api_key = '87d845b0b6cf29baa1a73cc34b067a95'
location = str(form.getvalue("cityname"))

complete_api_link = "https://api.openweathermap.org/data/2.5/weather?q="+location+"&appid="+api_key
api_link = requests.get(complete_api_link)
api_data = api_link.json()

#create variables to store and display data
temp_city = ((api_data['main']['temp']) - 273.15)
weather_desc = api_data['weather'][0]['description']
hmdt = api_data['main']['humidity']
wind_spd = api_data['wind']['speed']
date_time = datetime.now().strftime("%d %b %Y | %I:%M:%S %p")

print('<body><center style="color:red; border: 5px solid black; margin: 10% 20%; padding: 5%;">')
print('<h1>Weather Stats for</br>(%s)</h1>' %cn, "</br>")
print ("--------------------------------------------------------------------------" "</br>")
print ("Weather Stats for - {} </br> {}".format(location.upper(), date_time),"</br>")
print ("--------------------------------------------------------------------------" "</br>")

print ("Current temperature is: {:.2f} deg C" '</br>' .format(temp_city,"</br>"))
print ("Current weather desc  :",weather_desc, "</br>")
print ("Current Humidity      :",hmdt, '%'"</br>")
print ("Current wind speed    :",wind_spd ,'kmph')

print('<html>')
print('</center></body></html>')