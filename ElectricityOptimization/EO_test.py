import pymssql
import pandas as pd

# Database connection parameters
server = 'localhost'
database = "ZEE600Data_Ins_SKDS"
username = 'ZEE600'
password = 'Aa123456'

# Connect to the database
conn = pymssql.connect(server=server, user=username, password=password, database=database)
cursor = conn.cursor()
print('连接成功！')


# Read the CSV file
csv_file_path = 'ElectricityOptimization_demo3_output1.csv'  # Update this path
df = pd.read_csv(csv_file_path)

# Check the dataframe to ensure it is read correctly
print(df)

# Insert data into the existing table
for index, row in df.iterrows():
    insert_query = '''
    INSERT INTO ElectricityOptimization (recordTime, theDateStr, value_jian, value_feng, value_ping, value_gu, value_optimize_recommendation) 
    VALUES (%s, %s, %s, %s, %s, %s, %s)
    '''
    cursor.execute(insert_query, (
        row['recordTime'], 
        row['theDateStr'], 
        row['value_jian'], 
        row['value_feng'], 
        row['value_ping'], 
        row['value_gu'], 
        row['value_optimize_recommendation']
    ))

conn.commit()
print("Data inserted successfully!")
# Close the connection
conn.close()