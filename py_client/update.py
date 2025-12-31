import requests

data={
    "title":"Hello jupiter",
    "price":299.1
}

endpoint="http://localhost:8000/api/products/8/update/"
get_response=requests.put(endpoint ,json=data)

