import requests
from twilio.rest import Client


account_sid = "ACb138b03ac85b2e8eab58da845a00c987"
auth_token = "8a697ac1e460b62ae1dd8d487b89d8f0"
api_key = "13658e6822e5e701f0033a35bfed9a26"
OWM_END = "https://api.openweathermap.org/data/2.5/forecast"   
weather_params = {
    'lat':8.524139,
    'lon':76.936638,
    'appid':api_key,
    'cnt':4
}
l = []
will_rain = False
response = requests.get(OWM_END,params=weather_params)
data = response.json()
for i in range(4):
    id = data['list'][i]['weather'][0]['id']
    l.append(id)
for i in l:
    if i<600:
        will_rain = True 
        break
if will_rain:
    print("Bring an Umberlla") 
else:
    print("No rain in the next few hours 🙂")