import ast

def sql_data_permissions_info_eval(permissions_info):
    fixed_permissions_info = ast.literal_eval(permissions_info)
    return fixed_permissions_info