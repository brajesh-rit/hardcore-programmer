import requests
response = requests.get('http://api.open-notify.org/astros.json', timeout=5)
response.content() # Return the raw bytes of the data payload
response.text() # Return a string representation of the data payload
response.json()


try:
    response = requests.get('http://api.open-notify.org/astros.json', timeout=5)
    response.raise_for_status()
    # Code here will only run if the request is successful
except requests.exceptions.HTTPError as errh:
    print(errh)
except requests.exceptions.ConnectionError as errc:
    print(errc)
except requests.exceptions.Timeout as errt:
    print(errt)
except requests.exceptions.RequestException as err:
    print(err)