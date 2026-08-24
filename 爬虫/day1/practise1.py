import requests

url = "https://httpbin.org/get"
response = requests.get(url)
print(response.status_code)
print(response.text)
print(response.url)
print(response.headers)