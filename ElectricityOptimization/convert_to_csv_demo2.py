import json
import csv

# 打开JSON文件并加载数据
with open('response.json', 'r', encoding='utf-8') as f:
    data = json.load(f)

count = 0
# 打开CSV文件准备写入
with open('output_demo3.csv', 'w', newline='', encoding='utf-8') as csvfile:
    fieldnames = ['name', 'total', 'recordTime', 'theDateStr', '_Value', 'isValid_尖', 'value_尖', 'isValid_feng','value_feng']
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

    writer.writeheader()

    # 遍历JSON数据并写入CSV文件
    for result in data['result']:
        name = result['name']
        total = result['total']
        for item in result['dtoList']:
            row = {
                'name': name,
                'total': total,
                'recordTime': item['recordTime'],
                'theDateStr': item['theDateStr'],
                '_Value': item['_Value'],
                'isValid': item['isValid'],
                'value': item['value']
            }
            writer.writerow(row)
            # if count < 96 :
            #     row = {
            #     'recordTime': item['recordTime'],
            #     'theDateStr': item['theDateStr'],
            #     'isValid_尖': item['isValid'],
            #     'value_尖': item['value']
            #     }
            #     writer.writerow(row)
            
            # elif count >= 96 and count < 192:
            #     row = {
            #     'isValid_feng': item['isValid'],
            #     'value_feng': item['value']
            #     }
            #     writer.writerow(row)
            count = count + 1
        print(count)
print("JSON文件已成功转换为CSV文件")

