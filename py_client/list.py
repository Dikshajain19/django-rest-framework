import requests


endpoint="http://localhost:8000/api/products/"

r=get_response=requests.get(endpoint )
print("Status:", r.status_code)
print("Body:", r.text)
