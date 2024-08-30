

import serial
import time
import os
from cryptography.fernet import Fernet
# from PyQt6.QtWidgets import QMessageBox

from CommonTools import AppConfig as appConfig

dataSecretKey = Fernet.generate_key()
dataSecretCipherSuite = Fernet(dataSecretKey)

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
serial_port = /dev/ttyUSB0      \n\
serial_portNum = 9000              \n\
isSecretInfo = True \n")
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
    
qrClientType = None
try:
    qrClientType = appConfig.load_config('qr_client_type')
except:
    try:
        qrClientType = load_config('qr_client_type')
    except:
        qrClientType = None  
isSecretInfo = None
serialPort = None 
serialPortNum = None
if qrClientType is not None and qrClientType == 'serialType':
    serialPort = None
    try:
        serialPort = appConfig.load_config('serial_port')
    except:
        try:
            serialPort = load_config('serial_port')
        except:
            serialPort = None 
    try:
        serialPortNum = appConfig.load_config('serial_portNum')
    except:
        try:
            serialPortNum = load_config('serial_portNum')
        except:
            serialPortNum = None 
    try:
        isSecretInfo = appConfig.load_config('isSecretInfo')
    except:
        try:
            isSecretInfo = load_config('isSecretInfo')
        except:
            isSecretInfo = None 


# 替换以下串行端口名为你的设备串行端口
# port = serialPort  # Linux示例
# port = "COM3"  # Windows示例
isExist_ser_ClientQR = False
try:
    ser_ClientQR = serial.Serial(serialPort, int(serialPortNum), timeout=1)
    isExist_ser_ClientQR = True
except:
    isExist_ser_ClientQR = False

# while True:
# def scan_barcode():
#     if ser.in_waiting > 0:
#         barcode = ser.readline().decode('utf-8').rstrip()
#         print(f"扫描结果: {barcode}")
#     time.sleep(0.5)  # 延时0.5秒，降低CPU占用