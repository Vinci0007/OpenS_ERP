

from db_mysql_manage import mysql_pool as mspool

from concurrent.futures import ThreadPoolExecutor


def showAllWarehouseData():
    with ThreadPoolExecutor(max_workers=5) as executor: 
        allAllData_Warehouse = {}
        params = ['warehouse_product_infos']
        warehouseData = list(executor.map(mspool.query_table, params)) 
        if warehouseData is not None:
            for result in warehouseData[0]:   
                if result:
                    keys = ['id', 'product_id', 'product_type', 'product_name', 
                            'supplier', 'destination', 'isoutbound', 'inbound_time', 'outbound_time', 'receive_time', 
                            'price', 'price_unit', 
                            'quality', 'quality_unit', 'operator', 'productCheckID'] 
                    
                    json_results = dict(zip(keys, result))
                    user_check_id = json_results['operator']
                    
                    name_withcheckid = ['erp_account'], ['user_check_id'], [user_check_id]
                    userinfo = list(executor.map(mspool.query_fields, *name_withcheckid)) 
                    if userinfo is not None:
                        json_results['operator'] = userinfo[0][0][2]
                    allAllData_Warehouse.update({json_results['id']: json_results})
                # json_results.update({'auth_token': Auth_token})
            return allAllData_Warehouse
        else:
            return {}
 
 
