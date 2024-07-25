import json
import csv
import requests
import yaml

def ElectricityOptimization(accessToken,base_url):
    ########
    # # 方式一：直接打开JSON文件并加载数据
    # with open('response.json', 'r', encoding='utf-8') as f:
    #     data = json.load(f)

    # # 方式二：使用url请求数据
    # # Define the API URL and headers
    # url = "http://27.148.193.68:9089/api/services/app/ElectricityOptimization/ElectricityOptimizationSearch"
    # headers = {
    #     "accept": "text/plain",
    #     "Content-Type": "application/json-patch+json",
    #     "Authorization": "Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJodHRwOi8vc2NoZW1hcy54bWxzb2FwLm9yZy93cy8yMDA1LzA1L2lkZW50aXR5L2NsYWltcy9uYW1laWRlbnRpZmllciI6IjIiLCJodHRwOi8vc2NoZW1hcy54bWxzb2FwLm9yZy93cy8yMDA1LzA1L2lkZW50aXR5L2NsYWltcy9uYW1lIjoiZGV2X2FkbWluIiwiQXNwTmV0LklkZW50aXR5LlNlY3VyaXR5U3RhbXAiOiIyNzMzYzAzMy02YzFjLTgwYzEtMGMzMC0zYTEwNThjNWM4MzEiLCJodHRwOi8vc2NoZW1hcy5taWNyb3NvZnQuY29tL3dzLzIwMDgvMDYvaWRlbnRpdHkvY2xhaW1zL3JvbGUiOiJEZXZfQWRtaW4iLCJodHRwOi8vd3d3LmFzcG5ldGJvaWxlcnBsYXRlLmNvbS9pZGVudGl0eS9jbGFpbXMvdGVuYW50SWQiOiIxIiwic3ViIjoiMiIsImp0aSI6IjdlYzUzMWI1LTJiZmYtNDRlMy1iNjM2LTQyZDY3NmUxODRlMyIsImlhdCI6MTcyMTI2MzcwNCwidG9rZW5fdmFsaWRpdHlfa2V5IjoiYTY4Zjg0MTktZTUzZC00MjZjLTg2ODctMzA3N2Q1Yjc5NzI2IiwidXNlcl9pZGVudGlmaWVyIjoiMkAxIiwibmJmIjoxNzIxMjYzNzA0LCJleHAiOjE3NTI3OTk3MDQsImlzcyI6IkV3YXlXZWJBcGlCYXNlIiwiYXVkIjoiRXdheVdlYkFwaUJhc2UifQ.PORpitZ7V9OEq_TN2-erBADCAMd4XHdm5nUfiPDM834"
    # }

    # # Define the payload
    # payload = {
    #     "showMain": "公司",
    #     "companyCodeList": ["string"],
    #     "deptCodeList": ["string"],
    #     "regionCodeList": ["string"],
    #     "classificationCodeList": ["string"],
    #     "dateRangeType": "Day",
    #     "year": 2024,
    #     "month": 7,
    #     "day": 18
    # }

    # # Send the API request
    # response = requests.post(url, headers=headers, json=payload)
    # data = response.json()

    # 方式三：使用配置文件
    with open('ElectricityOptimization/config.yaml', 'r', encoding='utf-8') as f:
        config = yaml.safe_load(f)

    url = f"{base_url}/api/services/app/ElectricityOptimization/ElectricityOptimizationSearch"
    headers = {
        "accept": "text/plain",
        "Content-Type": "application/json-patch+json",
        "Authorization": f"Bearer {accessToken}"
    }
    payload = config['payload']

    # Send the API request
    response = requests.post(url, headers=headers, json=payload)
    data = response.json()

    ########

    count = 0
    aa = 0
    bb= 0
    cc =0
    dd = 0
    ee = 0
    a = []
    b = []
    c = []
    d = []
    e = []
    # 打开CSV文件准备写入
    with open('ElectricityOptimization_demo3_output1.csv', 'w', newline='', encoding='utf-8') as csvfile:
        fieldnames = ['recordTime', 'theDateStr', 'value_jian','value_feng','value_ping', 'value_gu', 'value_optimize_recommendation']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

        writer.writeheader()

        # 遍历JSON数据并写入CSV文件
        for result in data['result']:
            name = result['name']
            total = result['total']
            for item in result['dtoList']:
                if name == "尖":
                    a.append(item['_Value'])
                    aa += 1
                elif name == "峰":
                    b.append(item['_Value'])
                    bb += 1
                elif name == "平":
                    c.append(item['_Value'])
                    cc += 1
                elif name == "谷":
                    d.append(item['_Value'])
                    dd += 1
                elif name == "优化建议":
                    e.append(item['_Value'])
                    ee += 1

        # 检查列表长度
        max_len = min(len(a), len(b), len(c), len(d), len(e))

        for i in range(max_len):
            row = {
                # 'name': name,
                # 'total': total,
                'recordTime': data['result'][0]['dtoList'][i]['recordTime'],
                'theDateStr': data['result'][0]['dtoList'][i]['theDateStr'],
                'value_jian': a[i],
                'value_feng': b[i],
                'value_ping': c[i],
                'value_gu': d[i],
                'value_optimize_recommendation': e[i]
            }
            writer.writerow(row)
            count += 1
            if count == 96:
                break

    print("ElectricityOptimization-JSON文件已成功转换为CSV文件")
