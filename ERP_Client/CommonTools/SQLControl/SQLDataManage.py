# import hashlib
# import mysql.connector
# #import Config
# from CommonTools.SQLControl import sql_data_transform as sdt, mysql_Connect as mysqlc


# # def permissions_save():
# #     pass


# # def permissions_load():
# #     # global sql_datatest
# #     preset_permissions_list = sql_datatest[0]
# #     return preset_permissions_list


# def users_save():
#     pass


# def find_user_with_username(username):
#     connect = mysqlc.mysql_connect()
#     cursor_username = connect.cursor()
#     cursor_username.execute("SELECT * FROM `erp_account` WHERE `username` = %s", (username,))
#     row_username = cursor_username.fetchall()
#     if cursor_username.rowcount == 0:
#         user_info = None
#         cursor_username.close()
#         return user_info
#     else:
#         user_info = sdt.user_info_transform2soft(row_username[0])
#         cursor_username.close()
#         return user_info


# # find_user_with_username('123456789')

# def find_user_with_name(name):
#     connect = mysqlc.mysql_connect()
#     cursor = connect.cursor()
#     cursor.execute("SELECT * FROM `erp_account` WHERE `name` = %s", (name,))
#     row = cursor.fetchall()
#     if cursor.rowcount == 0:
#         user_info = None
#         cursor.close()
#         return user_info
#     else:
#         user_info = sdt.user_info_transform2soft(row[0])
#         cursor.close()
#         return user_info


# def find_user_with_user_role(role):
#     connect = mysqlc.mysql_connect()
#     cursor = connect.cursor()
#     cursor.execute("SELECT * FROM `erp_account` WHERE `role` = %s", (role,))
#     row = cursor.fetchall()
#     if cursor.rowcount == 0:
#         user_info = None
#         cursor.close()
#         return user_info
#     else:
#         # user_info = sdt.user_info_transform2soft(row)
#         cursor.close()
#         return user_info


# def find_users_with_user_department(department):
#     users_list = []
#     connect = mysqlc.mysql_connect()
#     cursor = connect.cursor()
#     cursor.execute("SELECT * FROM `erp_account` WHERE `department` = %s", (department,))
#     rows = cursor.fetchall()
#     if cursor.rowcount == 0:
#         user_info = None

#         cursor.close()
#         return users_list
#     else:
#         # 打印数据
#         for row in rows:
#             user_info = sdt.user_info_transform2soft(row)
#             users_list.append(user_info)
#         cursor.close()
#         return users_list


# def username_exist(username):
#     user_find_name = username
#     user_info = find_user_with_username(user_find_name)
#     if user_info is not None:
#         return False
#     return True


# def save_new_users_info(user_info):
#     cursor = mysqlc.mysql_connect()[0]
#     cursor.execute(sdt.save_querys['erp_account_save_query'],
#                    (user_info['username'], user_info['name'], user_info['password'],
#                     user_info['phone'], user_info['role'], user_info['department'],
#                     user_info['dir_lead'], user_info['permission_group'], user_info['online_status'],
#                     user_info['employeed_status'], user_info['permissions_info'],
#                     user_info['user_check_id'], user_info['logo'], user_info['email'], 
#                     user_info['note'], user_info['backup0'],
#                     user_info['backup1'], user_info['backup2']))


# def load_flow_data_from_sql_exist(flow_number):
#     flow_info = {}
#     connect = mysqlc.mysql_connect()
#     cursor = connect.cursor()
#     cursor.execute("SELECT * FROM `work_flow_infos` WHERE `flow_number` = %s", (flow_number,))
#     rows = cursor.fetchall()
#     if cursor.rowcount == 0:
#         flow_info = None
#         cursor.close()
#         return [False, flow_info]
#     else:
#         row = rows[0]
#         flow_info = [row[0], row[1], row[2], row[3], row[4], row[5], row[6], row[7], row[8], row[9], row[10]]
#         cursor.close()
#         return [True, flow_info]


# def save_flow_data_to_sql(flow_info):
#     flow_infos1 = flow_info[1:]
#     # exist_state =
#     if load_flow_data_from_sql_exist(flow_info[1])[0]:
#         connect = mysqlc.mysql_connect()
#         cursor = connect.cursor()
#         #0 ：id ; 1 : flow_number
#         cursor.execute(sdt.update_querys['work_flow_infos_update_query']['update_query_flow_name'],
#                        (flow_info[2], flow_info[1]))
#         cursor.execute(sdt.update_querys['work_flow_infos_update_query']['update_query_flow_type'],
#                        (flow_info[3], flow_info[1]))
#         cursor.execute(sdt.update_querys['work_flow_infos_update_query']['update_query_flow_sub_type'],
#                        (flow_info[4], flow_info[1]))
#         cursor.execute(sdt.update_querys['work_flow_infos_update_query']['update_query_submitter'],
#                        (flow_info[5], flow_info[1]))
#         cursor.execute(sdt.update_querys['work_flow_infos_update_query']['update_query_user_check_id'],
#                        (flow_info[6], flow_info[1]))
#         cursor.execute(sdt.update_querys['work_flow_infos_update_query']['update_query_flow_create_time'],
#                        (flow_info[7], flow_info[1]))
#         cursor.execute(sdt.update_querys['work_flow_infos_update_query']['update_query_flow_submit_time'],
#                        (flow_info[8], flow_info[1]))
#         cursor.execute(sdt.update_querys['work_flow_infos_update_query']['update_query_flow_state'],
#                        (flow_info[9], flow_info[1]))
#         cursor.execute(sdt.update_querys['work_flow_infos_update_query']['update_query_flow_nodes_info'],
#                        (flow_info[10], flow_info[1]))
#         cursor.execute(sdt.update_querys['work_flow_infos_update_query']['update_query_backup0'],
#                        (flow_info[11], flow_info[1]))
#         cursor.execute(sdt.update_querys['work_flow_infos_update_query']['update_query_backup1'],
#                        (flow_info[12], flow_info[1]))
#         cursor.execute(sdt.update_querys['work_flow_infos_update_query']['update_query_backup2'],
#                        (flow_info[13], flow_info[1]))

#         connect.commit()
#         cursor.close()
#     else:
#         connect = mysqlc.mysql_connect()
#         cursor = connect.cursor()
#         a = sdt.save_querys['work_flow_infos_save_query']
#         # print(a)
#         cursor.execute(sdt.save_querys['work_flow_infos_save_query'], (
#             flow_info[1], flow_info[2], flow_info[3], flow_info[4], flow_info[5], flow_info[6], flow_info[7],
#             flow_info[8],
#             flow_info[9], flow_info[10], flow_info[11], flow_info[12], flow_info[13]))
#         connect.commit()
#         cursor.close()


# # info = ['0', 'SO-0001-20241515-2F2SF622WEF6', '123', '001123', '0014124', 'admin', 'admin0132165487', '20240101124', '----1', '1', '0', '0',
# #         '0', '0']
# # save_flow_data_to_sql(info)

# # preset_permissions_list = permissions_load(0)
# # users_list = users_load(0)


# # print(users_load())
