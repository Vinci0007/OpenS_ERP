from CommonTools import AppConfig

import requests, os

from CommonTools.SQLControl import SQLDataManage

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
        
if AppConfig is None:
    def load_config(param):
    # config_data = {}
        with open(config_file_path, 'r') as file:
            for line in file:
                if param in line:
                    param_value = line.split('=')[1].strip().strip("'")
                    config_data = param_value
        return config_data


try:
    runType = AppConfig.load_config('run_Type')
except:
    try:
        runType = load_config('run_Type')
    except:
        runType = None

if runType is not None and runType == 'server':
    def get_data_from_server(Route, Headers, Data):
        # route = 'login_validation'
        url = AppConfig.load_config("server_address") + Route  
        # response = requests.get(url)
        try:
            response_data = requests.post(url, headers=Headers, data=Data)
            if response_data.status_code == 200:
                return response_data.json()
            else:
                return False
            # 处理响应...
        except ConnectionError as e:
            return False
        
        
        # login_state = response_data.json()['login_state']
        

    def find_user_with_username(username, session_token):
        headers = {'Authorization': session_token}
        url = AppConfig.load_config("server_address") + '/find_user_with_username'  
        # response = requests.get(url)
        Data = {
            'Authorization': session_token,
            'username': username,
        } 
        try:
            response_data = requests.post(url, headers=headers, data=Data)
            if response_data.status_code == 200:
                return response_data.json()
            else:
                return False
            # 处理响应...
        except ConnectionError as e:
            return False
elif runType is not None and runType == 'local':
    testuserinfo = {
        'id': '1',
        'username': 'admin',
        'name': 'admin',
        'password': '123',
        'phone': '1231231231231',
        'role': 'admin',
        'department': 'admin',
        'dir_lead': '',
        'permission_group': 'admin',
        'online_status': '1',
        'employeed_status': 'q',
        'permissions_info': '["admin",[0xFFFF, 0xFFFF, 0xFFFF, 0xFFFF, 0xFFFF, 0xFFFF, 0xFFFF, 0xFFFF, 0xFFFF, 0xFFFF]]',
        'user_check_id': 'admin1101051091009720240501000159863',
        'logo': '',
        'email': 'admin@admin.com',
        'note': '',
        'backup0': '',
        'backup1': '',
        'backup2': '',
    }
    
    def find_user_with_username(username, session_token):
        return testuserinfo

        
    def get_data_from_server(Route, Headers, Data):
        return testuserinfo
