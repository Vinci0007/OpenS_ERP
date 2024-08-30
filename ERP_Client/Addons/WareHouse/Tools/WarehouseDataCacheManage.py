import sqlite3
import os
import json
import time

from Addons.WareHouse.Tools import WarehouseServerData as whserv

warehouse_database_cache_file = "./Cache/warehouse_database.db"
# warehouse_database_cache_file = "database.db"

warehouseTableKey = """
    CREATE TABLE warehouse_data (
    id INTEGER PRIMARY KEY,
    product_id TEXT NOT NULL,
    product_type TEXT,
    product_name TEXT,
    supplier TEXT,
    destination TEXT,
    isoutbound TEXT,
    inbound_time TEXT,
    outbound_time TEXT,
    receive_time TEXT,
    price TEXT,
    price_unit TEXT,
    quality TEXT
    quality_unit TEXT
    operator TEXT
    productCheckID TEXT
    );
    """

def swStart_DbCacheInit():
    warehouse_data = []
    columns_infos = []
    all_warehouse_data = whserv.showAll_WarehouseData()     ##dict {1:{'id': 'sdads'}, .........}
    if (all_warehouse_data is not None) and (all_warehouse_data != False): #  or all_warehouse_data:
        for jsonkey, warehousevalue in all_warehouse_data.items():
            warehouse_data.append(warehousevalue)       # list [{id: 'sdads'}, {id: 'sdads'}, {id: 'sdads'}]
    else:
        warehouse_data = readDataFromLocal()
        return warehouse_data     
    # 检查硬盘缓存文件是否存在
    if os.path.exists(warehouse_database_cache_file):
        updateSQLData(warehouse_data)
        return warehouse_data  
    else:
        os.makedirs("./Cache", exist_ok=True)
        columns = []
        # 从服务器中读取数据并存储到内存缓存中
        all_warehouse_data = whserv.showAll_WarehouseData()
        conn = sqlite3.connect(warehouse_database_cache_file)
        c = conn.cursor()
        c.execute("SELECT name FROM sqlite_master WHERE type='table' AND name='warehouse_data'")
        if c.fetchone() is None:
            c.execute(warehouseTableKey)
            c.execute("PRAGMA table_info(warehouse_data)")
            columns = [row[1] for row in c.fetchall()]
        else:
            c.execute("PRAGMA table_info(warehouse_data)")
            columns = [row[1] for row in c.fetchall()]
            pass
        # 从服务器中读取数据的逻辑，这里用一个示例代替
        for jsonkey, warehousevalue in all_warehouse_data.items():
            keys = []
            values = []
            # isKeyExist = False
            for key, value in warehousevalue.items():
                if key not in columns:
                    c.execute("ALTER TABLE warehouse_data ADD COLUMN (?) TEXT", (key))
                    # pass
                # 将内存缓存中的数据写入硬盘缓存文件中
                keys.append(key) 
                values.append(value)
                # values = tuple(tempvalue)
            assert len(keys) == len(values), "Keys and values lists must be of the same length."    
            columns = ', '.join(keys)
            placeholders = ', '.join(['?'] * len(keys))  
            whDbQuery = f"INSERT OR REPLACE INTO warehouse_data ({columns}) VALUES ({placeholders})"
            whDbValue = tuple(values)
            c.execute(whDbQuery, whDbValue)
            warehouse_data.append(warehousevalue)
        conn.commit()
        c.close()
        conn.close()
        return warehouse_data        

def readDataFromLocal():
    warehouse_data = []
        
    conn = sqlite3.connect(warehouse_database_cache_file)
    c = conn.cursor()
    c.execute("SELECT name FROM sqlite_master WHERE type='table' AND name='warehouse_data'")
    if c.fetchone() is None:
        return warehouse_data 
    c.execute("SELECT * FROM warehouse_data")
    wh_existDataRows = c.fetchall()
    if c.rowcount == 0:
        c.close()
        conn.close()
        return warehouse_data 
    else:
        for wh_existDataRow in wh_existDataRows:
            if wh_existDataRow is not None:
                keys = ['id', 'product_id', 'product_type', 'product_name', 
                        'supplier', 'inbound_time', 'outbound_time', 'receive_time', 
                        'price', 'price_unit', 
                        'quality', 'quality_unit', 'operator', 'productCheckID']
                json_results = dict(zip(keys, wh_existDataRow)) 
                warehouse_data.append(json_results)
                c.close()
                conn.close()
        return warehouse_data 

def updateSQLData(warehouse_data): 
    # warehouse_data = []  
    isUpdated = False     
    # 将数据写入硬盘缓存文件中，以便下次使用时可以直接从文件中读取数据
    try:
        conn = sqlite3.connect(warehouse_database_cache_file)
    except sqlite3.Error as e:
        return isUpdated
     
    try:        
        c = conn.cursor()
        tableName = c.execute("SELECT name FROM sqlite_master WHERE type='table' AND name='warehouse_data'").fetchone()[0]
        if tableName is None:
            return isUpdated
        # c.execute("SELECT * FROM warehouse_data")
        for dataNum in range(len(warehouse_data)):
            productID = warehouse_data[dataNum]['product_id']
            c.execute("SELECT * FROM warehouse_data WHERE product_id = ?", (productID,))
            data_rows = c.fetchall()
            if c.rowcount == 0:
                keys = []
                values = []
                for key, value in warehouse_data[dataNum].items():
                    keys.append(key) 
                    values.append(value)
                    columns = ', '.join(keys)
                    placeholders = ', '.join(['?'] * len(keys)) 
                    whDbQuery = f"INSERT OR REPLACE INTO warehouse_data ({columns}) VALUES ({placeholders})"
                    whDbValue = tuple(values)
                    c.execute(whDbQuery, whDbValue)
                    conn.commit()
                    c.close()
                    conn.close()
            else:
                # update_whDbQuery = "UPDATE warehouse_data SET ({columns}) = ({placeholders}) WHERE ({columns}) = ({columns})"
                for row in data_rows:
                    keys = []
                    values = []
                    if row[13] == warehouse_data[dataNum]['productCheckID']:
                        pass
                    else:
                        c.execute("UPDATE warehouse_data SET id = ? WHERE id = ?", (warehouse_data[dataNum]['id'], row[0]))
                        c.execute("UPDATE warehouse_data SET product_id = ? WHERE product_id = ?", (warehouse_data[dataNum]['product_id'], row[1]))
                        c.execute("UPDATE warehouse_data SET product_type = ? WHERE product_type = ?", (warehouse_data[dataNum]['product_type'], row[2]))
                        c.execute("UPDATE warehouse_data SET product_name = ? WHERE product_name = ?", (warehouse_data[dataNum]['product_name'], row[3]))
                        c.execute("UPDATE warehouse_data SET supplier = ? WHERE supplier = ?", (warehouse_data[dataNum]['supplier'], row[4]))
                        c.execute("UPDATE warehouse_data SET destination = ? WHERE destination = ?", (warehouse_data[dataNum]['destination'], row[5]))
                        c.execute("UPDATE warehouse_data SET isoutbound = ? WHERE isoutbound = ?", (warehouse_data[dataNum]['isoutbound'], row[6]))
                        c.execute("UPDATE warehouse_data SET inbound_time = ? WHERE inbound_time = ?", (warehouse_data[dataNum]['inbound_time'], row[7]))
                        c.execute("UPDATE warehouse_data SET outbound_time = ? WHERE outbound_time = ?", (warehouse_data[dataNum]['outbound_time'], row[8]))
                        c.execute("UPDATE warehouse_data SET receive_time = ? WHERE receive_time = ?", (warehouse_data[dataNum]['receive_time'], row[9]))
                        c.execute("UPDATE warehouse_data SET price = ? WHERE price = ?", (warehouse_data[dataNum]['price'], row[10]))
                        c.execute("UPDATE warehouse_data SET price_unit = ? WHERE price_unit = ?", (warehouse_data[dataNum]['price_unit'], row[11]))
                        c.execute("UPDATE warehouse_data SET quality = ? WHERE quality = ?", (warehouse_data[dataNum]['quality'], row[10]))
                        c.execute("UPDATE warehouse_data SET quality_unit = ? WHERE quality_unit = ?", (warehouse_data[dataNum]['quality_unit'], row[12]))
                        c.execute("UPDATE warehouse_data SET operator = ? WHERE operator = ?", (warehouse_data[dataNum]['operator'], row[13]))
                        c.execute("UPDATE warehouse_data SET productCheckID = ? WHERE productCheckID = ?", (warehouse_data[dataNum]['productCheckID'], row[14]))
                        conn.commit()
                        isUpdated = True     
        c.close()
        conn.close()
        return isUpdated
    except:
        return isUpdated


def updateInboundLog(inboundLog, userCheckId): 
    isAddedOrUpdated = False
    inboundLogTableKey = """
    CREATE TABLE warehouse_data (
    id INTEGER PRIMARY KEY,
    product_id TEXT NOT NULL,
    product_type TEXT,
    product_name TEXT,
    supplier TEXT,
    destination TEXT,
    isoutbound TEXT,
    inbound_time TEXT,
    outbound_time TEXT,
    receive_time TEXT,
    price TEXT,
    price_unit TEXT,
    quality TEXT
    quality_unit TEXT
    operator TEXT
    productCheckID TEXT
    );
    """
    
    # 检查硬盘缓存文件是否存在
    if os.path.exists(warehouse_database_cache_file):
        # updateSQLData(warehouse_data)
        # return warehouse_data  
        pass
    else:
        os.makedirs("./Cache", exist_ok=True)
        columns = []
        conn = sqlite3.connect(warehouse_database_cache_file)
        c = conn.cursor()
        createTableName = 'inboundLog' + userCheckId
        c.execute("SELECT name FROM sqlite_master WHERE type='table' AND name= ?", (createTableName,))
        if c.fetchone() is None:
            c.execute(inboundLogTableKey)
            c.execute("PRAGMA table_info(warehouse_data)")
            columns = [row[1] for row in c.fetchall()]
        else:
            c.execute("PRAGMA table_info(warehouse_data)")
            columns = [row[1] for row in c.fetchall()]
            pass
        for jsonkey, warehousevalue in inboundLog.items():
                keys = []
                values = []
                # isKeyExist = False
                for key, value in warehousevalue.items():
                    if key not in columns:
                        c.execute("ALTER TABLE warehouse_data ADD COLUMN (?) TEXT", (key,))
                        # pass
                    # 将内存缓存中的数据写入硬盘缓存文件中
                    keys.append(key) 
                    values.append(value)
                    # values = tuple(tempvalue)
                assert len(keys) == len(values), "Keys and values lists must be of the same length."    
                columns = ', '.join(keys)
                placeholders = ', '.join(['?'] * len(keys))  
                whDbQuery = f"INSERT OR REPLACE INTO warehouse_data ({columns}) VALUES ({placeholders})"
                whDbValue = tuple(values)
                try:      
                    c.execute(whDbQuery, whDbValue)
                    c.execute("SELECT * FROM ? WHERE productCheckID = ? AND id = ?", (createTableName, inboundLog[0]['productCheckID'], inboundLog[0]['id'],))
                    isAddedOrUpdated = True
                except:
                    isAddedOrUpdated = False
                # warehouse_data.append(warehousevalue)
        conn.commit()
        conn.close()
        
        # updateLogFromServer()
        return isAddedOrUpdated  
    
def updateLogFromServer(userCheckId):
    warehouse_data = []  
    all_warehouse_data = whserv.showAll_WarehouseData()
    for jsonkey, warehousevalue in all_warehouse_data.items():
        if warehousevalue['operator'] == userCheckId:
            warehouse_data.append(warehousevalue)
            isUpdated = updateInboundLog(warehouse_data, userCheckId)
            if isUpdated:
                return [True, warehouse_data]
            else:
                return [False, warehouse_data]
                