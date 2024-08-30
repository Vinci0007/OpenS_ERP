import threading
import hashlib
import time
import json
from flask import Flask, request, jsonify
from concurrent.futures import ThreadPoolExecutor

from db_mysql_manage import mysql_pool as mspool

app = Flask(__name__)

# 模拟的用户验证逻辑
def validate_user(Auth_token, Login_user):
    # 在这里可以添加具体的用户验证逻辑，比如从数据库中查询用户信息并验证密码
    username = Login_user['username']
    password_hash = Login_user['password']
    result = find_user_with_username(Auth_token, username)
    if result:
        sql_pass = result['password']
        sql_username = result['username']
        sql_password_hash = hashlib.sha256(sql_pass.encode()).hexdigest()
        if username == sql_username and password_hash == sql_password_hash:
            return {'login_state': True,
                            'user_check_id': result['username'],
                            'auth_token': result['auth_token'],
                            }
        else:
            # return jsonify({'login_state': False,
            #                 'user_check_id': '',
            #                 'auth_token': '',
            #                 })
            return {'login_state': False,
                        'user_check_id': '',
                        'auth_token': '',
                        }
    else:
        return {'login_state': False,
                        'user_check_id': '',
                        'auth_token': '',
                        }
        
    


def find_user_with_username(Auth_token, username):
    params = ['erp_account'], ['username'], [username]
    with ThreadPoolExecutor(max_workers=5) as executor:    
        user_account = list(executor.map(mspool.query_fields, *params)) 
        new_user_info =  user_account[0] 
        # print(user_account)
        if new_user_info is not None:
        ####是否需要多次查询 
            # new_user_info =  user_account[0]    
            keys = ['id', 'username', 'name', 'password', 
                    'phone', 'role', 'department', 'dir_lead', 
                    'permission_group', 'online_status', 
                    'employeed_status', 'permissions_info', 
                    'user_check_id', 'logo', 'email', 'note', 'backup0', 'backup1']  # 假设这里列出了所有字段名
            
            json_results = dict(zip(keys, new_user_info[0]))
            json_results.update({'auth_token': Auth_token})
            # print(json_results)
            return json_results
        else:
            return {}
    # return jsonify(json_results)
    

def thread_task(name):
    time.sleep(2)
