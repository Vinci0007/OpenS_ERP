import mysql.connector
from dbutils.pooled_db import PooledDB
#import Config

config_file_path = 'Config/config.erpconfig'


def load_sql_config(file_path):
    config_data = {}
    with open(file_path, 'r') as file:
        for line in file:
            if 'erp_sql_host' in line:
                erp_sql_host = line.split('=')[1].strip().strip("'")
                config_data.update({'erp_sql_host': erp_sql_host})
            if 'erp_sql_port' in line:
                erp_sql_port = line.split('=')[1].strip().strip("'")
                config_data.update({'erp_sql_port': erp_sql_port})
            if 'erp_sql_account' in line:
                erp_sql_account = line.split('=')[1].strip().strip("'")
                config_data.update({'erp_sql_account': erp_sql_account})
            if 'erp_sql_password' in line:
                erp_sql_password = line.split('=')[1].strip().strip("'")
                config_data.update({'erp_sql_password': erp_sql_password})
            if 'erp_sql_database_name' in line:
                erp_sql_database_name = line.split('=')[1].strip().strip("'")
                config_data.update({'erp_sql_database_name': erp_sql_database_name})
                break
    return config_data


def mysql_connect():
    config_data = load_sql_config(config_file_path)
    conn = mysql.connector.connect(
        # host="127.0.0.1",
        host=config_data['erp_sql_host'],
        user=config_data['erp_sql_account'],
        password=config_data['erp_sql_password'],
        database=config_data['erp_sql_database_name']
    )
    # 创建一个游标对象
    # cursor = conn.cursor()
    # cursor.execute("SELECT * FROM `work_flow_infos` WHERE `flow_number` = %s", ('123456789',))
    return conn

# # 数据库连接池配置
# pool_config = {
#     'host': 'localhost',
#     'user': 'your_username',
#     'password': 'your_password',
#     'database': 'your_database',
#     'charset': 'utf8',
#     'cursorclass': mysql.connector.cursors.DictCursor,  # 使用字典游标
#     'maxconnections': 20,  # 连接池允许的最大连接数
#     'mincached': 5,  # 初始化时，连接池至少创建的空闲连接数
#     'maxcached': 5,  # 连接池中最多闲置的连接数
#     'maxshared': 5,  # 连接池最大可共享连接数
#     'blocking': True,  # 连接池中如果没有可用连接后，是否阻塞等待
#     'maxusage': None,  # 一个连接最多被重复使用的次数，None表示无限制
#     'setsession': [],  # 开始会话前执行的命令列表
# }

# # 创建连接池
# pool = PooledDB(mysql.connector, **pool_config)
# # 从连接池中获取一个连接
# connection = pool.connection()
# mysql_connect()
