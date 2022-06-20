
import requests

response = requests.get('https://jsonplaceholder.typicode.com/posts/1')

# raspunsul va fi memorat in variabila response

# print(response)           # <Response [200]>
# print(type(response))     # <class 'requests.models.Response'>
# print(dir(response))

# asa extragem informatii din exterios:

if response.status_code == 200:
    print("Connected")
    print(response.json)
else:
    print("Connesction error.")    