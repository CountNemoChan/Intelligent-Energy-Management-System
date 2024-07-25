import pymssql
import pandas as pd


def SEI_insert_data(server, database, username, password):
    # Database connection parameters
    # server = 'localhost'
    # database = "ZEE600Data_Ins_SKDS"
    # username = 'ZEE600'
    # password = 'Aa123456'

    # Connect to the database
    conn = pymssql.connect(server=server, user=username, password=password, database=database)
    cursor = conn.cursor()
    print('连接成功！')


    # Read the CSV file
    csv_file_path = 'SynthesizeEnergyIncome_demo1_output1.csv'  # Update this path
    df = pd.read_csv(csv_file_path)

    # Check the dataframe to ensure it is read correctly
    #print(df)

    # Clear the existing data in the table
    clear_table_query = "DELETE FROM SynthesizeEnergyIncome"
    cursor.execute(clear_table_query)
    conn.commit()
    print("SEI-Existing data cleared successfully!")

    # Insert data into the existing table
    for index, row in df.iterrows():
        insert_query = '''
        INSERT INTO SynthesizeEnergyIncome (date, zifaziyong, yudianshangwang) 
        VALUES (%s, %s, %s, %s)
        '''
        cursor.execute(insert_query, (
            row['日期'], 
            row['自发自用'], 
            row['余电上网']
            
        ))

    conn.commit()
    print("Data inserted successfully!")
    # Close the connection
    conn.close()