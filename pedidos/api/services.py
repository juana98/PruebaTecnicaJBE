from pedidos.api.models import Driver
import requests

url = 'https://gist.githubusercontent.com/CesarF/41958f4bc34240b75a83fce876836044/raw/ae2989ab69b230b913b90ef6b80a932970f3aa26/points.json'
response = requests.get(url)
data_json = response.json()
for data in range(len(data_json)):
    drivers = Driver(
        id = data_json[data]['id'], 
        x = data_json[data]['x'],
        y = data_json[data]['y'], 
        last_update = data_json[data]['last-update']
        )
    drivers.save()