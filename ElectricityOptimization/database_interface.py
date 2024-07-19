import pandas as pd
from sqlalchemy import create_engine

# 读取CSV文件
csv_file_path = 'csv_file.csv'
df = pd.read_csv(csv_file_path)

# 数据库连接信息
db_user = 'user'
db_password = 'password'
db_host = 'db_host'
db_port = 'db_port'
db_name = 'db_name'

# 创建数据库连接
engine = create_engine(f'mysql+mysqlconnector://{db_user}:{db_password}@{db_host}:{db_port}/{db_name}')

# 将数据写入数据库
table_name = 'table_name'
df.to_sql(table_name, engine, if_exists='replace', index=False)

print("数据已成功写入数据库")