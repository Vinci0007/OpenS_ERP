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
                cls.__pool = PooledDB(
                    creator=pymysql, 
                    mincached=5, 
                    maxcached=10, 
                    maxshared=3, 
                    maxconnections=20, 
                    blocking=True, 
                    host='localhost', 
                    user='root', 
                    password='123', 
                    database='erp_data', 
                    charset='utf8mb4')
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

        
