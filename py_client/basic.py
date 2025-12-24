import requests

# endpoint="https://httpbin.org/anything"
endpoint="http://localhost:8000/api/"
get_response=requests.get(endpoint , json={"product_id" :123})

print(get_response.headers)
print(get_response.text)
# print(get_response.text)  #this gives response in json format

#print(get_response.json())   #this gives the response as puthon dictionary

# print("/////////////********************/////////////////////")
# #this method echoes back the data which was sent by us to it 
#get_response=requests.get(endpoint,json={"query" : "hello world"}) #here the data comes with key as data , json
# print(get_response.text)
# print(get_response.json())
# print("/////////////********************/////////////////////")


# #this method echoes back the data which was sent by us to it 
# get_response=requests.get(endpoint,data={"query" : "hello world"}) #here the data comes with key as form , json
# print(get_response.text)
# print(get_response.json())
# print("/////////////********************/////////////////////")
