
import os

from PyQt6.QtWidgets import QMessageBox

config_file_path = 'Config/config.erpconfig'

if os.path.exists(config_file_path):
    appConfigPath = config_file_path
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
        appConfigPath = 'Config/config.erpconfig'


# config_data = {}

def load_config(param):
    # config_data = {}
    with open(appConfigPath, 'r') as file:
        for line in file:
            if param in line:
                param_value = line.split('=')[1].strip().strip("'")
                config_data = param_value
    return config_data

# load_config('server_address')