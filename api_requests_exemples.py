import requests

response= requests.get('https://api.github.com')

print(response.status_code)




response= requests.get('https://jsonplaceholder.typicode.com/posts')

print("GET",response.status_code)


response= requests.post(
    'https://jsonplaceholder.typicode.com/posts',
    data={'title':'foo', 'body':'bar', 'userId':1} 
    )

print("POST",response.status_code)



response= requests.put(
    'https://jsonplaceholder.typicode.com/posts/1',
    data={'title':'foo', 'body':'bar', 'userId':1} 
    )

print("PUT",response.status_code)



response= requests.delete(
    'https://jsonplaceholder.typicode.com/posts/1',
    data={'title':'foo', 'body':'bar', 'userId':1} 
    )

print("DELETE",response.status_code)




response= requests.get('http://www.omdbapi.com/?apikey=87c6f947&t=Titanic')

print(response.status_code)

print(response.json())




response= requests.get('https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid={API key}')

print(response.status_code)

print(response.json())






