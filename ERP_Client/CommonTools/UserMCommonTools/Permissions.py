
class PermissionsManager:
    common_permissions_group = {
        'change_usermane': False,
        'change_password': False,
        'view_user_details': False,
        'view_user_permissions': False,
        'workflow_notification': False,
        'workflow_modify': False,
        'workflow_delete': False,
        'workflow_view': False,
        'workflow_approval': False,
        'work_handover': True,

    }

    sales_permissions_group = {
        'sales_workflow': False,
        'sales_order_application': False,
        'sales_order_approval': False,
        'sales_order_delete': False,
        'sales_order_view': False,
        'sales_order2work_application': False,
        'sales_order2work_modify': False,
        'sales_order2work_delete': False,
        'sales_order2work_view': False,
    }

    warehouse_permissions_group = {
        'warehouse_workflow': False,
        'warehouse_outbound': False,
        'warehouse_inbound': False,
        'warehouse_view': False,
        'warehouse_add_product': False,
        'warehouse_delete_product': False,
        'warehouse_modify_product': False,
        'warehouse_view_product': False,
        'warehouse_view_product_detail': True,
        
    }
    
    system_control_permission = {
        'change_workflow': False,
        'create_workflow': False,
        'delete_workflow': False
    }

    def set_common_permissions_group(self, number):
        if number == 0x1:
            self.common_permissions_group = {
                'change_usermane': True,
                'change_password': False,
                'view_user_details': False,
                'view_user_permissions': False,
                'workflow_notification': False,
                'workflow_modify': False,
                'workflow_delete': False,
                'workflow_view': False,
                'workflow_approval': False,
                'work_handover': False,
            }
        elif number == 0x2:
            self.common_permissions_group = {
                'change_usermane': False,
                'change_password': True,
                'view_user_details': False,
                'view_user_permissions': False,
                'workflow_notification': False,
                'workflow_modify': False,
                'workflow_delete': False,
                'workflow_view': False,
                'workflow_approval': False,
                'work_handover': False,
            }
        elif number == 0x3:
            self.common_permissions_group = {
                'change_usermane': True,
                'change_password': True,
                'view_user_details': False,
                'view_user_permissions': False,
                'workflow_notification': False,
                'workflow_modify': False,
                'workflow_delete': False,
                'workflow_view': False,
                'workflow_approval': False,
                'work_handover': False,
            }


    def permission_number_cal(common_permissions_group, sales_permissions_group, warehouse_permissions_group):
        permission_number_common = 0b0
        permission_number_sales = 0b0
        permission_number_warehouse = 0b0
        permission_number = []
        if common_permissions_group.get('change_usermane') == True:
            permission_number_common += 0b1
            if common_permissions_group.get('change_password') == True:
                permission_number_common += 0b01
                if common_permissions_group.get('view_user_details') == True:
                    permission_number_common += 0b001
                    if common_permissions_group.get('view_user_permissions') == True:
                        permission_number_common += 0b0001
                        if common_permissions_group.get('workflow_notification') == True:
                            permission_number_common += 0b00001
                            if common_permissions_group.get('workflow_modify') == True:
                                permission_number_common += 0b000001
                                if common_permissions_group.get('workflow_delete') == True:
                                    permission_number_common += 0b0000001
                                    if common_permissions_group.get('workflow_view') == True:
                                        permission_number_common += 0b00000001
                                        if common_permissions_group.get('workflow_approval') == True:
                                            permission_number_common += 0b000000001
                                            if common_permissions_group.get('work_handover') == True:
                                                permission_number_common += 0b0000000001
                        
        else:
            permission_number = 0b0
        
        if sales_permissions_group.get('sales_workflow') == True:
            permission_number_sales += 0b10
            if sales_permissions_group.get('sales_order_application') == True:
                permission_number_sales += 0b010
                if sales_permissions_group.get('sales_order_approval') == True:
                    permission_number_sales += 0b0010
                    if sales_permissions_group.get('sales_order_delete') == True:
                        permission_number_sales += 0b00010
                        if sales_permissions_group.get('sales_order_view') == True:
                            permission_number_sales += 0b000010
                            if sales_permissions_group.get('sales_order2work_application') == True:
                                permission_number_sales += 0b0000010
                                if sales_permissions_group.get('sales_order2work_modify') == True:
                                    permission_number_sales += 0b00000010
                                    if sales_permissions_group.get('sales_order2work_delete') == True:
                                        permission_number_sales += 0b000000010
                                        if sales_permissions_group.get('sales_order2work_view') == True:
                                            permission_number_sales += 0b0000000010
        else:
            permission_number_sales += 0b0

        if warehouse_permissions_group.get('warehouse_workflow') == True:
            permission_number_warehouse += 0b10
            if warehouse_permissions_group.get('warehouse_outbound') == True:
                permission_number_warehouse += 0b010
                if warehouse_permissions_group.get('warehouse_inbound') == True:
                    permission_number_warehouse += 0b0010
                    if warehouse_permissions_group.get('warehouse_view') == True:
                        permission_number_warehouse += 0b00010
                        if warehouse_permissions_group.get('warehouse_add_product') == True:
                            permission_number_warehouse += 0b000010
                            if warehouse_permissions_group.get('warehouse_delete_product') == True:
                                permission_number_warehouse += 0b0000010
                                if warehouse_permissions_group.get('warehouse_modify_product') == True:
                                    permission_number_warehouse += 0b00000010
                                    if warehouse_permissions_group.get('warehouse_view_product') == True:
                                        permission_number_warehouse += 0b000000010
                                        if warehouse_permissions_group.get('warehouse_view_product_detail') == True:
                                            permission_number_warehouse += 0b0000000010
                            else:
                                permission_number_warehouse += 0b0
                        else:
                            permission_number_warehouse += 0b0
                    else:
                        permission_number_warehouse += 0b0
                else:
                    permission_number_warehouse += 0b0
            else:
                permission_number_warehouse += 0b0
        else:
            permission_number_warehouse += 0b0

        permission_number = [permission_number_common, permission_number_sales, permission_number_warehouse]



        return permission_number