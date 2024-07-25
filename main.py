import requests
import yaml
import schedule
import time

from SynthesizeEnergyIncome.convert_to_csv_demo1 import SynthesizeEnergyIncome
from ElectricityOptimization.convert_to_csv_demo3 import ElectricityOptimization
from EnergyConservingBenefit.convert_to_csv_demo1 import EnergyConservingBenefit
from EnergyTuning.convert_to_csv_demo1 import EnergyTuning

from ElectricityOptimization.EO_database_interface import EO_insert_data
from EnergyConservingBenefit.ECB_database_interface import ECB_insert_data
from EnergyTuning.ET_database_interface import ET_insert_data
from SynthesizeEnergyIncome.SEI_database_interface import SEI_insert_data

def scheduled_task():
    # Load the configuration
    with open('config_main.yaml', 'r', encoding='utf-8') as f:
        config = yaml.safe_load(f)

    url = config['url']
    headers = config['headers']
    payload = config['payload']

    # Etract the IP address in a specific region
    base_url = url.split("/api")[0]
    print(f"Connecting to {base_url}...")

    # Send the API request
    response = requests.post(url, headers=headers, json=payload)

    # Print the status code and response text
    print("Status Code:", response.status_code)
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

    try:
        ElectricityOptimization(accessToken, base_url)
        EnergyConservingBenefit(accessToken, base_url)
        EnergyTuning(accessToken, base_url)
        SynthesizeEnergyIncome(accessToken, base_url)

    except Exception as e:
        # 捕获异常并处理
        print(f"An error occurred: {e}")


    # # Database interface
    server = config['database_server']
    database = config['database_name']
    username = config['username']
    password = config['password']

    try:
        EO_insert_data(server, database, username, password)
        ECB_insert_data(server, database, username, password)
        ET_insert_data(server, database, username, password)
        SEI_insert_data(server, database, username, password)

    except Exception as e:
        # 捕获异常并处理
        print(f"An error occurred: {e}")

#print(server, database, username, password)
schedule.every().minute.do(scheduled_task)

while True:
    try:
        schedule.run_pending()
    except Exception as e:
        print(f"An error occurred during scheduling: {e}")
    time.sleep(1)