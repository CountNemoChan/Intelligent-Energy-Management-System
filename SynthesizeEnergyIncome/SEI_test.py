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
csv_file_path = 'SynthesizeEnergyIncome_demo1_output1.csv'  # Update this path
df = pd.read_csv(csv_file_path)

# Check the dataframe to ensure it is read correctly
#print(df)

# Insert data into the existing table
for index, row in df.iterrows():
    insert_query = '''
    INSERT INTO SynthesizeEnergyIncome (date, zifaziyong, yudianshangwang, chunengshangwang) 
    VALUES (%s, %s, %s, %s)
    '''
    cursor.execute(insert_query, (
        row['日期'], 
        row['自发自用'], 
        row['余电上网'], 
        row['储能上网']
    ))

conn.commit()
print("Data inserted successfully!")
# Close the connection
conn.close()