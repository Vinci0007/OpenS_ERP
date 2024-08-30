# # from CommonTools.SQLControl import SQLDataManage
# from Addons.BaseAddons.server_sql import server_data_format as sdf


# from PyQt6.QtWidgets import QMessageBox

# from datetime import datetime


# def warehouse_permission(userInfo):
#     # user_permissions_info = sdt.sql_data_permissions_info_eval(userInfo['Permissions_info'])
#     user_permissions_info = sdf.sql_data_permissions_info_eval(userInfo['permissions_info'])
#     # print(user_permissions_info)
#     user_permissions_num = user_permissions_info[1][3]
#     # print(user_permissions_info)
    
#     if user_permissions_num & 0xFFFF != 0:
#         # print("You have permission to manage inbound items.")

#         return True
#     else:
#         msg = QMessageBox()
#         msg.setIcon(QMessageBox.Information)
#         msg.setText("无权限")
#         msg.setWindowTitle("无权限")
#         msg.exec_()  
#         return False
    
# def warehouse_subfunc_permission(userInfo, str):
#     ware_permission_number = userInfo['Permissions_info'][1][3]
#     if ware_permission_number & 0xFFFF != 0:
#         # print("You have permission to manage inbound items.")

#         return True
#     else:
#         msg = QMessageBox()
#         msg.setIcon(QMessageBox.Information)
#         msg.setText("无权限")
#         msg.setWindowTitle("无权限")
#         msg.exec_()  
#         return False


# def warehpuse_inbound(login_userinfo, wareHouseMenu):
#     wareHouseMenu.close()
#     warehouse_permission(login_userinfo)
    
    


# def warehpuse_outbound():
#     msg = QMessageBox()
#     msg.setIcon(QMessageBox.Information)
#     msg.setText("出库页面")
#     msg.setWindowTitle("出库页面")
#     msg.exec_()

# def isPermissionPrice_show(permissions_info):
#     user_permissions_info = sdf.sql_data_permissions_info_eval(permissions_info)
#     user_permission = user_permissions_info[1][3]
#     if user_permission & 0x4FFF != 0:
#     # if user_permission & 0 != 0:
#         # print("You have permission to manage inbound items.")
#         return True
#     else:
#         # msg = QMessageBox()
#         # msg.setIcon(QMessageBox.Information)
#         # msg.setText("无权限")
#         # msg.setWindowTitle("无权限")
#         # msg.exec_()
#         return False
    
# # warehouse_manage(SQLDataManage.users_load()[0])
