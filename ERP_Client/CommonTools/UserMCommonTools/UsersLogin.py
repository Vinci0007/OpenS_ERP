import hashlib
import jwt
import datetime
# from tkinter import messagebox
from CommonTools import AppConfig
from CommonTools.SQLControl import SQLDataManage
from CommonTools.Server_Client import client_functions as clientf

def login(username, password):
    # username = input("Enter username: ")
    # password = input("Enter password: ")
    # 计算输入密码的 hash 值
    password_hash = hashlib.sha256(password.encode()).hexdigest()
    user_login_data = {
        'username': username,
        'password': password_hash,
    }
    secret_key = 'zghksys'
    payload = {
    'user_id': username,
    'exp': datetime.datetime.now() + datetime.timedelta(days=1)  # 设置过期时间
    }
    token = jwt.encode(payload, secret_key, algorithm='HS256')
    headers = {'Authorization': token}
    try:
        response_data = clientf.get_data_from_server('/login_validation', headers, user_login_data)
    except:
        return {
            'login_state': False,
            'user_check_id': '',
            'auth_token': '',
            } 
    if response_data == 200:
        login_state = response_data
        # print(login_state)
        return login_state
    else:
        return {
            'login_state': False,
            'user_check_id': '',
            'auth_token': '',
            }
        
    
    
    # 验证用户名和密码是否匹配,本地
    # user_info = SQLDataManage.find_user_with_username(username)
    # if user_info is not None:
    #     sql_password_hash = hashlib.sha256(user_info['password'].encode()).hexdigest()
    #     if sql_password_hash == password_hash:
    #         return [True, user_info]
    # return [False, {}]
    


