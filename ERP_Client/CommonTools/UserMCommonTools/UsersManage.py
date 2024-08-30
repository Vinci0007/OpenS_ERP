from UserMCommonTools import UsersLogin, Permissions
from CommonTools.SQLControl import SQLDataManage
import hashlib
from datetime import datetime
import random



# 定义权限预设枚举
class PresetPermission:
    permissions_number = []
    per_group = 0x000000
    group_name = ''
    permissions_info = ['', '', 0x000000]

    def __init__(self):
        self.permissions_number = []
        self.per_group = 0x000000
        self.group_name = ''
        self.permissions_info = ['', '', 0x000000]

    def set_custom_permissions(self, username, permissions_info, is_inheritance):
        self.permissions_info = permissions_info
        permission_name = permissions_info[1]
        permissions_number = permissions_info[2]
        permissions_username = permissions_info[0]
        if permission_name in SQLDataManage.permissions_load():
            self.permissions_number = SQLDataManage.permissions_load()[permission_name]
            self.group_name = permission_name
            self.permissions_info = [username, permission_name, permissions_number]
        else:
            if is_inheritance & 0xFFFF != 0x0:
                if is_inheritance & 0x8000 != 0x0:
                    self.group_name = 'admin'
                    self.permissions_number = SQLDataManage.permissions_load()['admin'](2)
                    self.permissions_info = [username, permission_name + '/admin', self.permissions_number]
                    if is_inheritance & 0x4000 != 0x0:
                        self.group_name = 'sales_manager'
                        self.permissions_number = SQLDataManage.permissions_load()['sales_manager'](2)
                        self.permissions_info = [username, permission_name + '/sales_manager', self.permissions_number]
                    if is_inheritance & 0x2000 != 0x0:
                        self.group_name = 'warehouse_manager'
                        self.permissions_number[3] = 0xFFFF
                        self.permissions_info = [username, permission_name + '/warehouse_manager',
                                                 self.permissions_number]
                    if is_inheritance & 0x1000 != 0x0:
                        self.group_name = 'purchasing_manager'
                        self.permissions_number[4] = 0xFFFF
                        self.permissions_info = [username, permission_name + '/purchasing_manager',
                                                 self.permissions_number]
                    if is_inheritance & 0x0800 != 0x0:
                        self.group_name = 'tech_manager'
                        self.permissions_number[5] = 0xFFFF
                        self.permissions_info = [username, permission_name + '/tech_manager', self.permissions_number]
                    if is_inheritance & 0x0400 != 0x0:
                        self.group_name = 'hr_manager'
                        self.permissions_number[6] = 0xFFFF
                        self.permissions_info = [username, permission_name + '/hr_manager', self.permissions_number]
                    if is_inheritance & 0x0200 != 0x0:
                        self.group_name = 'common'
                        self.permissions_number[7] = 0xFFFF
                        self.permissions_info = [username, permission_name + '/common', self.permissions_number]
                else:
                    self.group_name = 'custom'
                    self.permissions_number = permissions_number
                    self.permissions_info = [username, permission_name + '/custom', self.permissions_number]
            else:
                self.group_name = 'custom'
                self.permissions_number = permissions_number
                self.permissions_info = [username, permission_name + '/custom', self.permissions_number]

    def preset_group_manage(self):
        pass

    def set_pre_admin_group(self, permission):
        if permission == 0x100000:
            permissionlist = {
                'change_permission': True,
                'create_user': True,
                'delete_user': True,
                'update_user': True,
                'create_group': True,
                'delete_group': True,
                'update_group': True,
                'create_role': True,
                'delete_role': True,
                'update_role': True,
            }


class UserInfo:
    def __init__(self):
        self.username = ''
        self.per_name = ''
        self.password = ''
        self.phone = ''
        self.role = ''
        self.department = ''
        self.my_workflow = ''
        self.dir_lead = ''
        self.permission_group = ''
        self.my_workflows_data_number = ''  
        self.online_status = ''
        self.employeed_status = ''
        self.permissions_info = ''
        self.Permissions = []
        self.user_check_id = ''
        self.logo = ''
        
    def upload_userlogo(self):
        ###### 增加图片上传功能
        self.logo = ''
        # upload_pic()

    def create_user(self, userinfo, is_inheritance):
        self.username = userinfo['username']
        self.per_name = userinfo['per_name']
        self.password = userinfo['password']
        self.phone = userinfo['phone']
        self.role = userinfo['role']
        self.department = userinfo['department']
        self.my_workflow = userinfo['my_workflow']
        permissions_info = userinfo['permissions_info']
        self.set_permission(self.username, permissions_info, is_inheritance)
        username_exist = SQLDataManage.username_exist(self.username)
        if not username_exist:
            print('username already exist')
        self.user_check_id = self.create_user_check_id
        user_infos = {
            'id':                  '0',
            'username':            self.username,
            'name':                self.per_name,
            'password':            self.password,
            'phone':               self.phone,
            'role':                self.role,
            'department':          self.department,
            'dir_lead':            self.dir_lead,
            'permission_group':    self.permission_group,
            'online_status':       self.online_status,
            'employeed_status':    self.employeed_status,
            'permissions_info':    self.permissions_info,
            'user_check_id':       self.user_check_id,
            'logo':                self.logo,  
            'note':                datetime.now(),
            'backup0':             'backup0',
            'backup1':             'backup1',
            'backup2':             'backup2',
        }
        
        SQLDataManage.save_new_users_info(user_infos)

    def set_permission(self, username, permissions_info, is_inheritance):
        # self.name = username
        # self.permissions = permissions
        PresetPermission.set_custom_permissions(username, permissions_info, is_inheritance)
        self.Permissions = PresetPermission.permissions_info
        
    # user_name + name(ascii) + create date + department number + random_number = str(random.randint(1, 99999)).zfill(5)
    def create_user_check_id(self):
        ascii_value = ''
        for char in self.per_name:
            ascii_value = str(ord(char)) + ascii_value
        create_date = datetime.now().strftime("%Y%m%d%H%M%S")
        department = {
            'admin': 0,
            'ceo': 1,
            'boss': 2,
            'sale': 3,
            'purchasing': 4,
            'warehouse': 5,
            'hr': 6,
            'backup': 7
        }
        random_number = str(random.randint(1, 99999)).zfill(5)
        department_number = str(department[self.department]).zfill(4)
        check_id = self.username + ascii_value + create_date + department_number + random_number
        return check_id
     
    def update_user_info(self):
        pass
        

def register_user():
    username = input("Enter new username: ")
    password = input("Enter new password: ")

    # 计算密码的 hash 值
    password_hash = hashlib.sha256(password.encode()).hexdigest()

    # 将新用户信息添加到用户数据库
    UsersLogin.user_database[username] = password_hash
    print("User registered successfully!")


def update_user():
    username = input("Enter username to update: ")

    # 检查用户是否存在
    if username in UsersLogin.user_database:
        new_password = input("Enter new password: ")
        password_hash = hashlib.sha256(new_password.encode()).hexdigest()
        UsersLogin.user_database[username] = password_hash
        print("User information updated.")
    else:
        print("User not found.")


def delete_user():
    username = input("Enter username to delete: ")

    # 检查用户是否存在
    if username in UsersLogin.user_database:
        del UsersLogin.user_database[username]
        print("User deleted successfully.")
    else:
        print("User not found.")


# 用户权限字典
user_permissions = {
    "admin": ["create", "read", "update", "delete"],
    "manager": ["read", "update"],
    "employee": ["read"]
}


def check_permission(username, action):
    if username in user_permissions:
        if action in user_permissions[username]:
            return True
        else:
            print("You don't have permission to perform this action.")
            return False
    else:
        print("User not found.")
        return False


def perform_action(username, action):
    if check_permission(username, action):
        # 执行相应的操作
        print(f"Performing {action} action.")


# 示例用法
perform_action("admin", "create")
perform_action("manager", "delete")
perform_action("employee", "update")
