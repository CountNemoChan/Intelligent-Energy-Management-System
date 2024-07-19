import csv
import requests
import json

# Define the API URL and headers
url = "http://27.148.193.68:9089/api/services/app/ElectricityOptimization/ElectricityOptimizationSearch"
headers = {
    "accept": "text/plain",
    "Content-Type": "application/json-patch+json",
    "Authorization": "Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJodHRwOi8vc2NoZW1hcy54bWxzb2FwLm9yZy93cy8yMDA1LzA1L2lkZW50aXR5L2NsYWltcy9uYW1laWRlbnRpZmllciI6IjIiLCJodHRwOi8vc2NoZW1hcy54bWxzb2FwLm9yZy93cy8yMDA1LzA1L2lkZW50aXR5L2NsYWltcy9uYW1lIjoiZGV2X2FkbWluIiwiQXNwTmV0LklkZW50aXR5LlNlY3VyaXR5U3RhbXAiOiIyNzMzYzAzMy02YzFjLTgwYzEtMGMzMC0zYTEwNThjNWM4MzEiLCJodHRwOi8vc2NoZW1hcy5taWNyb3NvZnQuY29tL3dzLzIwMDgvMDYvaWRlbnRpdHkvY2xhaW1zL3JvbGUiOiJEZXZfQWRtaW4iLCJodHRwOi8vd3d3LmFzcG5ldGJvaWxlcnBsYXRlLmNvbS9pZGVudGl0eS9jbGFpbXMvdGVuYW50SWQiOiIxIiwic3ViIjoiMiIsImp0aSI6IjdlYzUzMWI1LTJiZmYtNDRlMy1iNjM2LTQyZDY3NmUxODRlMyIsImlhdCI6MTcyMTI2MzcwNCwidG9rZW5fdmFsaWRpdHlfa2V5IjoiYTY4Zjg0MTktZTUzZC00MjZjLTg2ODctMzA3N2Q1Yjc5NzI2IiwidXNlcl9pZGVudGlmaWVyIjoiMkAxIiwibmJmIjoxNzIxMjYzNzA0LCJleHAiOjE3NTI3OTk3MDQsImlzcyI6IkV3YXlXZWJBcGlCYXNlIiwiYXVkIjoiRXdheVdlYkFwaUJhc2UifQ.PORpitZ7V9OEq_TN2-erBADCAMd4XHdm5nUfiPDM834"
}

# Define the payload
payload = {
    "showMain": "公司",
    "companyCodeList": ["string"],
    "deptCodeList": ["string"],
    "regionCodeList": ["string"],
    "classificationCodeList": ["string"],
    "dateRangeType": "Day",
    "year": 2024,
    "month": 7,
    "day": 18
}

# Send the API request
response = requests.post(url, headers=headers, json=payload)
data = response.json()

# Extract data
records = data["result"][0]["dtoList"]

# Define CSV file name
csv_file = "electricity_optimization_data.csv"

# Write data to CSV
with open(csv_file, mode='w', newline='', encoding='utf-8') as file:
    writer = csv.writer(file)
    # Write header
    writer.writerow(["recordTime", "theDateStr", "_Value", "isValid", "value"])
    # Write records
    for record in records:
        writer.writerow([record["recordTime"], record["theDateStr"], record["_Value"], record["isValid"], record["value"]])

print(f"Data saved to {csv_file}")
