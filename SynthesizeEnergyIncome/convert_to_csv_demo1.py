import json
import csv
import requests
import yaml

# 使用配置文件获取数据
with open('config.yaml', 'r', encoding='utf-8') as f:
    config = yaml.safe_load(f)

url = config['url']
headers = config['headers']
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
with open('demo1_output1.csv', 'w', newline='', encoding='utf-8') as csvfile:
    fieldnames = ['日期', '自发自用', '余电上网', '储能上网']
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

    writer.writeheader()

    # 遍历JSON数据并写入CSV文件
    for result in data['result']:
        name = result['name']
        total = result['total']
        for item in result['dtoList']:
            if name == "自发自用":
                a.append(item['_Value'])
                aa += 1
            elif name == "余电上网":
                b.append(item['_Value'])
                bb += 1

    # 检查列表长度
    max_len = min(len(a), len(b))

    for i in range(max_len):
        row = {
            # 'name': name,
            # 'total': total,
            '日期': data['result'][0]['dtoList'][i]['theDateStr'],
            '自发自用': a[i],
            '余电上网': b[i]  
        }
        writer.writerow(row)
        

print("JSON文件已成功转换为CSV文件")
