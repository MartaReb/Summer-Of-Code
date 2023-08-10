import requests

try:
    response = requests.get('https://jsonplaceholder.typicode.com/users')
    response.raise_for_status()
except requests.exceptions.RequestException as err:
    print(f"Error occurred: {err}")
else:
    print("GET response status code: " + str(response.status_code))
    print("GET response headers: " + str(response.headers))
    print("GET response content : " + str(response.json()))


new_user = {"id": 11,"name":"John Lennon","username":"JL","email":"JohnLennon@gmail.com"}
try:
    response = requests.post('https://jsonplaceholder.typicode.com/users', data=new_user)
    response.raise_for_status()
except requests.exceptions.RequestException as err:
    print(f"Error occurred: {err}")
else:
    print("POST response status code: " + str(response.status_code))
    print("POST response headers: " + str(response.headers))
    print("POST response content : " + str(response.json()))

try:
    response = requests.put('https://jsonplaceholder.typicode.com/posts/1', data={"id":1, "title":"foo", "body":"bar"})
    response.raise_for_status()
except requests.exceptions.RequestException as err:
    print(f"Error occurred: {err}")
else:
    print("PUT response status code: " + str(response.status_code))
    print("PUT response headers: " + str(response.headers))
    print("PUT response content : " + str(response.json()))

try:
    response = requests.delete('https://jsonplaceholder.typicode.com/posts/1')
    response.raise_for_status()
except requests.exceptions.RequestException as err:
    print(f"Error occurred: {err}")
else:
    print("DELETE response status code: " + str(response.status_code))
    print("DELETE response headers: " + str(response.headers))
    print("DELETE response content : " + str(response.json()))