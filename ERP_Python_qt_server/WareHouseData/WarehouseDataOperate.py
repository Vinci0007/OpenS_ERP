
import json

from db_mysql_manage import mysql_pool as mspool

from concurrent.futures import ThreadPoolExecutor


def saveWarehouseData(auth_token, toSaveData):
    with ThreadPoolExecutor(max_workers=5) as executor: 
        warehouseSaveData_query = """
            INSERT INTO `warehouse_product_infos` (
                        `product_id`,
                        `product_name`,
                        `product_type`,
                        `supplier`,
                        `destination`,
                        `isoutbound`,
                        `inbound_time`,
                        `outbound_time`,
                        `receive_time`,
                        `price`,
                        `price_unit`,
                        `quality`,
                        `quality_unit`,
                        `operator`,
                        `productCheckID`
                        )
                        VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
        """
        # print(warehouseSaveData_query)
        # whData = json.loads(toSaveData)
        datalist = []
        queryslist = []
        for key, value in toSaveData.items():
            id = ''
            product_id = value['product_id']
            product_type = value['product_type']
            product_name = value['product_name']
            supplier = value['supplier']
            destination = ''
            isoutbound = value['isoutbound']
            inbound_time = value['inbound_time']
            outbound_time = value['outbound_time']
            receive_time = value['receive_time']
            price = value['price']
            price_unit = value['price_unit']
            quality = value['quality']
            quality_unit = value['quality_unit']
            operator = value['operator']
            productCheckID = value['productCheckID']

            data = (product_id, product_name, product_type, 
                                               supplier, destination, isoutbound, inbound_time, 
                                               outbound_time,receive_time, price, price_unit, 
                                               quality, quality_unit, operator, productCheckID,)
            # query = warehouseSaveData_query % (product_id, product_name, product_type, 
            #                                    supplier, destination, isoutbound, inbound_time, 
            #                                    outbound_time,receive_time, price, price_unit, 
            #                                    quality, quality_unit, operator, productCheckID,)
            datalist.append(data)
            # queryslist.append(query)
        params = [warehouseSaveData_query], [datalist]
        isSubmitSave = list(executor.map(mspool.saveAllDataToTable_withTable, *params)) 
        if isSubmitSave:
            return json.dumps(True)
        else:
            return json.dumps(False)





