import pymssql
import pandas as pd
from datetime import datetime


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
csv_file_path = 'test_data1.csv'  # Update this path
df = pd.read_csv(csv_file_path)

# Check the dataframe to ensure it is read correctly
#print(df)

now = datetime.now()
year = now.year
last_year = year - 1

# Insert data into the existing table
for index, row in df.iterrows():
    insert_query = '''
    INSERT INTO ElectricityOptimization (month, lastyear_usage, thisyear_usage) 
    VALUES (%s, %d, %d)
    '''
    cursor.execute(insert_query, (
        row['月份'], 
        row[f'{last_year}年用电量'], 
        row[f'{year}年用电量'], 
    ))

conn.commit()
print("Data inserted successfully!")
# Close the connection
conn.close()