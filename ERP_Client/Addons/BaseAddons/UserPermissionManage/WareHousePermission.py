from PyQt6.QtWidgets import QMessageBox


from Addons.BaseAddons.server_sql import server_data_format as sdf


def warehouse_permission(userInfo):
    # user_permissions_info = sdt.sql_data_permissions_info_eval(userInfo['Permissions_info'])
    user_permissions_info = sdf.sql_data_permissions_info_eval(userInfo['permissions_info'])
    # print(user_permissions_info)
    user_permissions_num = user_permissions_info[1][3]
    # print(user_permissions_info)
    
    if user_permissions_num & 0xFFFF != 0:
        # print("You have permission to manage inbound items.")

        return True
    else:
        msg = QMessageBox()
        msg.setIcon(QMessageBox.Information)
        msg.setText("无权限")
        msg.setWindowTitle("无权限")
        msg.exec_()  
        return False
 
def inbound_permission(permissions_info):
    user_permissions_info = sdf.sql_data_permissions_info_eval(permissions_info)
    user_permission = user_permissions_info[1][3]
    if user_permission & 0x4FFF != 0:
    # if user_permission & 0 != 0:
        # print("You have permission to manage inbound items.")
        return True
    else:
        msg = QMessageBox()
        msg.setIcon(QMessageBox.Information)
        msg.setText("无权限")
        msg.setWindowTitle("无权限")
        msg.exec_()
        return False
    
def outbound_permission(permissions_info):
    user_permissions_info = sdf.sql_data_permissions_info_eval(permissions_info)
    user_permission = user_permissions_info[1][3]
    if user_permission & 0x4FFF != 0:
    # if user_permission & 0 != 0:
        # print("You have permission to manage inbound items.")
        return True
    else:
        msg = QMessageBox()
        msg.setIcon(QMessageBox.Information)
        msg.setText("无权限")
        msg.setWindowTitle("无权限")
        msg.exec_()
        return False
    
def inventory_permission(permissions_info):
    user_permissions_info = sdf.sql_data_permissions_info_eval(permissions_info)
    user_permission = user_permissions_info[1][3]
    if user_permission & 0x4FFF != 0:
    # if user_permission & 0 != 0:
        # print("You have permission to manage inbound items.")
        return True
    else:
        msg = QMessageBox()
        msg.setIcon(QMessageBox.Information)
        msg.setText("无权限")
        msg.setWindowTitle("无权限")
        msg.exec_()
        return False
    
def isPermissionPrice_show(permissions_info):
    user_permissions_info = sdf.sql_data_permissions_info_eval(permissions_info)
    user_permission = user_permissions_info[1][3]
    if user_permission & 0x4FFF != 0:
    # if user_permission & 0 != 0:
        # print("You have permission to manage inbound items.")
        return True
    else:
        # msg = QMessageBox()
        # msg.setIcon(QMessageBox.Information)
        # msg.setText("无权限")
        # msg.setWindowTitle("无权限")
        # msg.exec_()
        return False