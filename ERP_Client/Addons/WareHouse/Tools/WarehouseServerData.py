
import os, json
import requests

from PyQt6.QtWidgets import QMessageBox


from CommonTools import AppConfig as appConfig

config_file_path = ''
def find_file(path, filename):
    for root, dirs, files in os.walk(path):
        if filename in files:
            return os.path.join(root, filename)
    return None

isAppConfigFileExist = find_file(".", "config.erpconfig")

if isAppConfigFileExist:
    config_file_path = isAppConfigFileExist
else:
    if not os.path.exists("Config"):
        os.mkdir("Config")
    with open("Config/config.erpconfig", "w") as f:
        f.write("                               \n\
### run Type            \n\
run_Type = local       \n\
      \n\
# mysql host                                \n\
erp_sql_host =                   \n\
erp_sql_port =                        \n\
erp_sql_account =                     \n\
erp_sql_password =                     \n\
erp_sql_database_name =           \n\
server_address =       \n\
server_port =                           \n\
\n\
#  QR CLIENT        \n\
qr_client_type =        \n\
serial_port = /dev/ttyUSB0               \n")
        # msg = QMessageBox()
        # msg.setIcon(QMessageBox.Icon.Warning)
        # msg.setText("请联系管理员或先行配置代理 !\n\
        #             自行配置请至'Config/config.erpconfig' ... ")
        # msg.setWindowTitle("数据库错误 !")
        # msg.exec_()


if appConfig is None:
    def load_config(param):
    # config_data = {}
        with open(config_file_path, 'r') as file:
            for line in file:
                if param in line:
                    param_value = line.split('=')[1].strip().strip("'")
                    config_data = param_value
        return config_data

sqlURL = None
try:
    sqlURL = appConfig.load_config('server_address')
except:
    try:
        sqlURL = load_config('server_address')
    except:
        sqlURL = None
try:
    runType = appConfig.load_config('run_Type')
except:
    try:
        runType = load_config('run_Type')
    except:
        runType = None

if runType is not None and runType == 'server':
    def showAll_WarehouseData():
        
        if sqlURL is None:
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Icon.Warning)
            msg.setText("请联系管理员或先行配置代理 !\n\
                        自行配置请至'Config/config.erpconfig' ... ")
            msg.setWindowTitle("数据库错误 !")
            msg.exec_()
        
        url = sqlURL + '/showAllWarehouseData'  
        try:
            response_data = requests.post(url)
            if response_data.status_code == 200:
                warehouseData = response_data.json()
                return warehouseData
            else:
                return False
            # 处理响应...
        except:
            return False
        
        
    def saveWarehouseData(productData, session_token):
        
        if sqlURL is None:
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Icon.Warning)
            msg.setText("请联系管理员或先行配置代理 !\n\
                        自行配置请至'Config/config.erpconfig' ... ")
            msg.setWindowTitle("数据库错误 !")
            msg.exec_()
        
        url = sqlURL + '/saveWarehouseData'
        headers = {
            'Content-Type': 'application/json',
            'Authorization': 'Bearer ' + session_token  # 替换 your_token_here 为你的实际 token
        }  
        try:
            data = json.dumps(productData)
            response_data = requests.post(url, headers=headers, data=data)
            if response_data.status_code == 200:
                warehouseData = response_data.json()
                return warehouseData
            else:
                return False
            # 处理响应...
        except:
            return False
        pass
elif runType is not None and runType == 'local':
    def showAll_WarehouseData():
       allData =  {1: {
            'id': '1',
            'product_id': 'test0001',
            'product_type': '测试产品类型1',
            'product_name': '测试产品1',
            'supplier': '测试供应商1',
            'destination': '测试',
            'isoutbound': '0',
            'inbound_time': '20240101 15:00:00',
            'outbound_time': '20240101 15:00:00',
            'receive_time': '20240101 15:00:00',
            'price': 'test',
            'price_unit': '$',
            'quality': '1',
            'quality_unit': '个',
            'operator': 'admin',
            'productCheckID': '1ewg51g6ew56g16we4gg1sde6',
            } ,}
       return allData
        
        
    def saveWarehouseData(productData, session_token):
        
        return True
