import requests

response = requests.post(
    "http://localhost:8080/predict",
    json={"input": ["This movie was amazing", "I hated this movie"]},
)

print("Status Code:", response.status_code)
print("Response:", response.json())
