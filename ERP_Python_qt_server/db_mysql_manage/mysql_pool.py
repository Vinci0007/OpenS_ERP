from flask import Flask, jsonify
from dbutils.pooled_db import PooledDB
import pymysql
import requests
import socket
import threading
from concurrent.futures import ThreadPoolExecutor

# from mysql_manage import users_manage as usersm

app = Flask(__name__)

class MySQLPool:
    __pool = None
    __lock = threading.Lock()

    @classmethod
    def get_connection(cls):
        with cls.__lock:
            if cls.__pool is None:
                cls.__pool = PooledDB(creator=pymysql, mincached=5, maxcached=10, maxshared=3, maxconnections=20, blocking=True, host='localhost', user='root', password='123', database='erp_data', charset='utf8mb4')
            return cls.__pool.connection()

def query_table(table_name):
    conn = MySQLPool.get_connection()
    cursor = conn.cursor()
    sql = "SELECT * FROM `{}`".format(table_name)
    cursor.execute(sql)
    result = cursor.fetchall()
    if cursor.rowcount == 0:
        cursor.close()
        conn.close()
        return None   
    else:
        cursor.close()
        conn.close()
        return result

def query_fields(table_name, fields_name, fields):
    conn = MySQLPool.get_connection()
    cursor = conn.cursor()
    sql = "SELECT * FROM `{}` WHERE `{}` = %s".format(table_name, fields_name)
    cursor.execute(sql, (fields,))
    result = cursor.fetchall()
    if cursor.rowcount == 0:
        cursor.close()
        conn.close()
        return None   
    else:
        cursor.close()
        conn.close()
        return result
    
def saveAllDataToTable_withTable(query, datalist):
    conn = MySQLPool.get_connection()
    cursor = conn.cursor()
    # sql = "SELECT * FROM `{}` WHERE `{}` = %s".format(table_name, fields_name)
    try:
        for data in datalist:
            cursor.execute(query, (data))
        # for data in datalist:
        #     cursor.execute(data)
        conn.commit()
        cursor.close()
        conn.close()
        return True
    except:
        conn.commit()
        cursor.close()
        conn.close()
        return False

        
# def updateAllDataToTable_withTable(table_name, fields_name, fields):
#     conn = MySQLPool.get_connection()
#     cursor = conn.cursor()
#     sql = "SELECT * FROM `{}` WHERE `{}` = %s".format(table_name, fields_name)
#     cursor.execute(sql, (fields,))
#     result = cursor.fetchall()
#     if cursor.rowcount == 0:
#         cursor.close()
#         conn.close()
#         return None   
#     else:
#         cursor.close()
#         conn.close()
#         return result  

# def saveAllDataToTable_withTable():
#     conn = MySQLPool.get_connection()
#     cursor = conn.cursor()
#     # sql = "SELECT * FROM `{}` WHERE `{}` = %s".format(table_name, fields_name)
#     warehouseSaveData_query = """
#         INSERT INTO `warehouse_product_infos` (
#                     `product_id`,
#                     `product_name`,
#                     `product_type`,
#                     `supplier`,
#                     `destination`,
#                     `isoutbound`,
#                     `inbound_time`,
#                     `outbound_time`,
#                     `receive_time`,
#                     `price`,
#                     `price_unit`,
#                     `quality`,
#                     `quality_unit`,
#                     `operator`,
#                     `productCheckID`
#                     )
#                     VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
#     """
#     data = ('fd', 'sdf', 'sdf', 'sdf', '', '', '2024-05-21 22:24:29', '', 'sdf', '无权限', 'sdf', '1', 'dsf', 'admin1101051091009720240501000159863', 'RZQOORL32J2FVRX3HPNPORG3RMVF5U5RZU6QJYZGLWTMBAGURCJA====')
    
#     try:
#         # for data in datalist:
#         #     cursor.execute(query, (data))
#         # for data in datalist:
#         #     cursor.execute(data)
#         cursor.execute(warehouseSaveData_query, data)
#         conn.commit()
#         cursor.close()
#         conn.close()
#         return True
#     except:
#         conn.commit()
#         cursor.close()
#         conn.close()
#         return False  
  
 
# saveAllDataToTable_withTable()  
  
  
  
  
  
  
  
  
  
    



#                     `id`,
# # @app.route('/query_erp_account', methods=['GET'])
# @app.route('/query_erp_account', methods=['GET'])
# def handle_query_erp_account():
#     with ThreadPoolExecutor(max_workers=5) as executor:
#         results = list(executor.map(query_table, ['erp_account'] * 5))  # 同时并发5个线程进行查询
#         # json_result = [result[0][i] for i in range(len(result[0]))]
#         keys = ['id', 'username', 'name', 'password', 
#                 'phone', 'role', 'department', 'dir_lead', 
#                 'permission_group', 'online_status', 
#                 'employeed_status', 'permissions_info', 
#                 'user_check_id', 'logo', 'note', 'backup0', 'backup1']  # 假设这里列出了所有字段名
#         json_results = [dict(zip(keys, result[0])) for result in results]
#     return jsonify(json_results)
#     # return json_result

# @app.route('/query_workflow_infos', methods=['GET'])
# def handle_query_another_table():
#     with ThreadPoolExecutor(max_workers=5) as executor:
#         result = list(executor.map(query_table, ['workflow_infos'] * 5))
#     return jsonify(result)




# class MySQLPool:
#     __pool = None
#     __lock = threading.Lock()

#     def __enter__(self):
#         self.conn = self.__get_conn()
#         self.cursor = self.conn.cursor()
#         return self
    
#     def __exit__(self, exc_type, exc_val, exc_tb):
#         self.cursor.close()
#         self.conn.close()

#     @classmethod
#     def __get_conn(cls):
#         with cls.__lock:
#             if cls.__pool is None:
#                 cls.__pool = PooledDB(creator=pymysql, mincached=5, maxcached=10, maxshared=3, maxconnections=20, blocking=True, host='localhost', user='root', password='123', database='erp_data', charset='utf8mb4')
#             return cls.__pool.connection()


# def erp_account_query_database():
#     with MySQLPool() as mysql:
#         sql = "SELECT * FROM erp_account;"
#         mysql.cursor.execute(sql)
#         erp_account_result = mysql.cursor.fetchall()
#         print(erp_account_result)
# def work_flow_infos_query_database():
#     with MySQLPool() as mysql:
#         sql = "SELECT * FROM work_flow_infos;"
#         mysql.cursor.execute(sql)
#         work_flow_infos_result = mysql.cursor.fetchall()
#         print(work_flow_infos_result)
#     # with MySQLPool() as mysql:
#     #     sql = "SELECT * FROM erp_account;"
#     #     mysql.cursor.execute(sql)
#     #     result = mysql.cursor.fetchall()
#     #     print(result)
# @app.route('/query', methods=['GET'])
# def handle_query():
#     with ThreadPoolExecutor(max_workers=5) as executor:
#         results = list(executor.map(erp_account_query_database, range(5)))  # 同时并发5个线程进行查询
#     return jsonify(results)
