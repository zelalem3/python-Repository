import requests
pixela_url = " https://pixe.la/v1/users"
USERNAME = "hello zelalem"
TOKEN = "zelalemgetnet"
user_Params = {
    "token": TOKEN,
    "username": USERNAME,
    "agreeTermsOfService": "yes",
    "notMInor": "yes"
}
# response = requests.post(pixela_url, json=user_Params)
# print(response.text)https://pixe.la/v1/users/a-know/graphs
graph_endpoint = f"{pixela_url}/{USERNAME}/graphs"
graph_config = {
    "id": "graph1",
    "name": "cycling Graph",
    "unit": "Km",
    "type": "float",
    "color": "ajisai"
}
headers = {
    "X-USER-TOKEN": TOKEN,

}
answer = requests.post(url=graph_endpoint, json=graph_config, headers=headers)
print(answer.text)
my_request = {
    "date":"20231521",
    "quantity": 9.74,
}
pixels = f"{pixela_url}/{USERNAME}/graphs/graph1"
pixel_response = requests.post(url=pixels, json=my_request, headers=headers)