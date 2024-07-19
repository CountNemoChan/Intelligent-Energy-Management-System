import json
import csv
import requests
import yaml

def EnergyTuning(accessToken, base_url):
    # 使用配置文件获取数据
    with open('EnergyTuning/config.yaml', 'r', encoding='utf-8') as f:
        config = yaml.safe_load(f)

    url = f"{base_url}/api/services/app/EnergyTuning/EnergyTuningSearch"
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

    a = []
    b = []

    # 打开CSV文件准备写入
    with open('EnergyTuning_demo1_output1.csv', 'w', newline='', encoding='utf-8') as csvfile:
        fieldnames = ['今日', '本月']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

        writer.writeheader()

        # 遍历JSON数据并写入CSV文件
        for result in data['result']:
            name = result['name']
            
            if name == '当日':
                a.append(result['currentValue'])
                aa += 1
            elif name == '当月':
                b.append(result['currentValue'])
                bb += 1

        # 检查列表长度
        max_len = min(len(a), len(b))

        for i in range(max_len):
            row = {
                # 'name': name,
                # 'total': total,
                '今日': a[i],
                '本月': b[i]  
            }
            writer.writerow(row)
            

    print("JSON文件已成功转换为CSV文件")
