import pymssql
import pandas as pd


class database_interface():
    # Database connection parameters
    server = '192.168.1.200'
    database = 'DESKTOP-NT5O7EF'
    username = 'ZEE600'
    password = 'Aa123456'

    # Connect to the database
    conn = pymssql.connect(server=server, user=username, password=password, database=database)
    cursor = conn.cursor()
    print('连接成功！')

    # Function to check if table exists and create it if not
    def create_table_if_not_exists():
        check_table_query = """
        IF NOT EXISTS (SELECT * FROM INFORMATION_SCHEMA.TABLES WHERE TABLE_NAME = 'monthly_electricity_usage')
        BEGIN
            CREATE TABLE monthly_electricity_usage (
                月份 VARCHAR(10),
                usage_2023 INT,
                usage_2024 INT
            )
        END
        """
        cursor.execute(check_table_query)
        conn.commit()
        print("Table checked and created if not exists.")

    # Call the function to ensure table exists
    create_table_if_not_exists()

    # Read the CSV file
    csv_file_path = '/mnt/data/path_to_your_csv_file.csv'  # Update this path
    df = pd.read_csv(csv_file_path)

    # Insert data into the existing table
    for index, row in df.iterrows():
        insert_query = '''
        INSERT INTO monthly_electricity_usage (月份, usage_2023, usage_2024) 
        VALUES (%s, %d, %d)
        '''
        cursor.execute(insert_query, (row['月份'], row['2023年用电量'], row['2024年用电量']))

    conn.commit()
    print("Data inserted successfully!")

    # Close the connection
    conn.close()