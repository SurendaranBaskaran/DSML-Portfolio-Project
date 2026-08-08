import requests

url = "http://127.0.0.1:5000/predict"

data = {
    "Store_id": 1,
    "Store_Type": "S1",
    "Location_Type": "L1",
    "Region_Code": "R1",
    "Holiday": 0,
    "Discount": "No",
    "#Order": 100,
    "Date": "2023-08-15"
}

response = requests.post(url, json=data)

print("Status:", response.status_code)
print("Response:", response.json())
