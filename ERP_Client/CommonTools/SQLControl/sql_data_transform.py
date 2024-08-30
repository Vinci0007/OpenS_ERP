import ast

erp_account_save_query = """
            INSERT INTO `erp_account` (
                `username`
                `name`
                `password`
                `phone`
                `role`
                `department`
                `dir_lead`
                `permission_group`
                `online_status`
                `employeed_status`
                `permissions_info`
                `user_check_id`
                `logo`
                `email`
                `note`
                `backup0`
                `backup1`
                `backup2`

            )
            VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
            """
work_flow_infos_save_query = """
                INSERT INTO `work_flow_infos` (   
                `flow_number`,
                `flow_name`,
                `flow_type`,
                `flow_sub_type`,
                `submitter`,
                `user_check_id`,
                `flow_create_time`,
                `flow_submit_time`,
                `flow_state`,
                `flow_nodes_info`,
                `backup0`,
                `backup1`,
                `backup2`
            )
            VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
            """
            
save_querys = {
    'erp_account_save_query': erp_account_save_query, 
    'work_flow_infos_save_query': work_flow_infos_save_query
    }

update_querys = {
    'erp_account_update_query': {
        'update_query_username': "UPDATE `erp_account` SET `username` = %s WHERE `username` = %s && `user_check_id` = %s", 
        'update_query_name': "UPDATE `erp_account` SET `name` = %s WHERE `username` = %s && `user_check_id` = %s", 
        'update_query_password': "UPDATE `erp_account` SET `password` = %s WHERE `username` = %s && `user_check_id` = %s", 
        'update_query_phone': "UPDATE `erp_account` SET `phone` = %s WHERE `username` = %s && `user_check_id` = %s", 
        'update_query_role': "UPDATE `erp_account` SET `role` = %s WHERE `username` = %s && `user_check_id` = %s", 
        'update_query_department': "UPDATE `erp_account` SET `department` = %s WHERE `username` = %s && `user_check_id` = %s", 
        'update_query_dir_lead': "UPDATE `erp_account` SET `dir_lead` = %s WHERE `username` = %s && `user_check_id` = %s", 
        'update_query_permission_group': "UPDATE `erp_account` SET `permission_group` = %s WHERE `username` = %s && `user_check_id` = %s", 
        
        'update_query_role': "UPDATE `erp_account` SET `online_status` = %s WHERE `username` = %s && `user_check_id` = %s", 
        'update_query_role': "UPDATE `erp_account` SET `employeed_status` = %s WHERE `username` = %s && `user_check_id` = %s", 
        'update_query_role': "UPDATE `erp_account` SET `permissions_info` = %s WHERE `username` = %s && `user_check_id` = %s", 
        
        # 'update_query_user_check_id': "UPDATE `erp_account` SET `user_check_id` = %s WHERE `username` = %s && `user_check_id` = %s", 
        'update_query_note': "UPDATE `erp_account` SET `logo` = %s WHERE `username` = %s && `user_check_id` = %s",
        'update_query_note': "UPDATE `erp_account` SET `email` = %s WHERE `username` = %s && `user_check_id` = %s", 
        'update_query_note': "UPDATE `erp_account` SET `note` = %s WHERE `username` = %s && `user_check_id` = %s",
        'update_query_backup0': "UPDATE `erp_account` SET `backup0` = %s WHERE `username` = %s && `user_check_id` = %s", 
        'update_query_backup1': "UPDATE `erp_account` SET `backup1` = %s WHERE `username` = %s && `user_check_id` = %s",
        'update_query_backup2': "UPDATE `erp_account` SET `backup2` = %s WHERE `username` = %s && `user_check_id` = %s", 
        
        },
    'work_flow_infos_update_query': {
        'update_query_flow_name': "UPDATE `work_flow_infos` SET `flow_name` = %s WHERE `flow_number` = %s", 
        'update_query_flow_type': "UPDATE `work_flow_infos` SET `flow_type` = %s WHERE `flow_number` = %s", 
        'update_query_flow_sub_type': "UPDATE `work_flow_infos` SET `flow_sub_type` = %s WHERE `flow_number` = %s", 
        'update_query_submitter': "UPDATE `work_flow_infos` SET `submitter` = %s WHERE `flow_number` = %s", 
        'update_query_user_check_id': "UPDATE `work_flow_infos` SET `user_check_id` = %s WHERE `flow_number` = %s", 
        'update_query_flow_create_time': "UPDATE `work_flow_infos` SET `flow_create_time` = %s WHERE `flow_number` = %s", 
        'update_query_flow_submit_time': "UPDATE `work_flow_infos` SET `flow_submit_time` = %s WHERE `flow_number` = %s", 
        'update_query_flow_state': "UPDATE `work_flow_infos` SET `flow_state` = %s WHERE `flow_number` = %s", 
        'update_query_flow_nodes_info': "UPDATE `work_flow_infos` SET `flow_nodes_info` = %s WHERE `flow_number` = %s", 
        'update_query_backup0': "UPDATE `work_flow_infos` SET `backup0` = %s WHERE `flow_number` = %s", 
        'update_query_backup1': "UPDATE `work_flow_infos` SET `backup1` = %s WHERE `flow_number` = %s",
        'update_query_backup2': "UPDATE `work_flow_infos` SET `backup2` = %s WHERE `flow_number` = %s", 
        
    }
}

def user_info_transform2soft(user_data_row):
    user_info_transform_dict = {
                    'user_id': user_data_row[0],
                    'username': user_data_row[1],
                    'name': user_data_row[2],
                    'password': user_data_row[3],
                    'phone': user_data_row[4],
                    'role': user_data_row[5],
                    'department': user_data_row[6],
                    'dir_lead': user_data_row[7],
                    'my_workflow': '',
                    'Permissions_group': user_data_row[8],
                    'online_status': user_data_row[9],
                    'employee_status': user_data_row[10],
                    'Permissions_info': user_data_row[11],
                    'user_check_id': user_data_row[12],
                    'logo': user_data_row[13],

                }
    return user_info_transform_dict

def user_info_transform2sql(user_data):
    username = user_data['username'], 
    name = user_data['name'], 
    password = user_data['password'],                           
    phone = user_data['phone'], 
    role = user_data['role'], 
    department = user_data['department'], 
    dir_lead = user_data['dir_lead'],
    permission_group = user_data['permission_group'], 
    online_status = user_data['online_status'], 
    employeed_status = user_data['employeed_status'], 
    permissions_info = user_data['permissions_info'], 
    user_check_id = user_data['user_check_id'], 
    note = user_data['note'], 
    backup0 = user_data['backup0'], 
    backup1 = user_data['backup1'], 
    backup2 = user_data['backup2']
    return username, name, password, phone, role, department, \
            dir_lead, permission_group, online_status, employeed_status, \
                permissions_info, user_check_id, note, backup0, backup1, backup2


# def 
# flow_infos = {
        
#             'flow_name': flow_info[2],
#             'flow_type': flow_info[3],
#             'flow_sub_type': flow_info[4],
#             'submitter': flow_info[5],
#             'flow_create_time': flow_info[6],
#             'flow_submit_time': flow_info[7],
#             'flow_state': flow_info[8],
#             'flow_nodes_info': flow_info[9],
#             'backup0': flow_info[10],
#             'backup1': flow_info[11],
#             'backup2': flow_info[12],
#         }

