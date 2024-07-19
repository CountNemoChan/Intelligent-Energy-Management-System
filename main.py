import requests
import yaml
from SynthesizeEnergyIncome.convert_to_csv_demo1 import SynthesizeEnergyIncome
from ElectricityOptimization.convert_to_csv_demo3 import ElectricityOptimization
from EnergyConservingBenefit.convert_to_csv_demo1 import EnergyConservingBenefit
from EnergyTuning.convert_to_csv_demo1 import EnergyTuning


# Load the configuration
with open('config_main.yaml', 'r', encoding='utf-8') as f:
    config = yaml.safe_load(f)

url = config['url']
headers = config['headers']
payload = config['payload']

# Send the API request
response = requests.post(url, headers=headers, json=payload)

# Print the status code and response text
# print("Status Code:", response.status_code)
# print("Response Text:", response.text)

# Parse the JSON response
try:
    data = response.json()
    # print("Response JSON:", data)
except ValueError:
    print("Response is not in JSON format")
    data = None

# Ensure that data is not None and accessToken is present
if data and 'result' in data:
    result = data['result']
    
    # Check if result is a dictionary and has accessToken
    if isinstance(result, dict) and 'accessToken' in result:
        accessToken = result['accessToken']
        print("Access Token:", accessToken)
    else:
        print("'result' is not a dictionary or does not contain 'accessToken'")
else:
    print("Response JSON does not contain 'result' or the response is not valid JSON")

ElectricityOptimization(accessToken)
EnergyConservingBenefit(accessToken)
EnergyTuning(accessToken)
SynthesizeEnergyIncome(accessToken)