from datetime import datetime
from WorkFlow import Workflow_type_def
from HTML import UserLogin
import threading
import time
# import schedule
import random
from CommonTools.SQLControl import SQLDataManage

my_workflows = [
    {
        'flow_name': '',
        'flow_link': '',
        'approval_state': True
    }
]


class SingleChoice:
    choice_quantity = 3
    choice_name = ['']
    title = ''
    is_bind_next_flow = True
    next_flow_name = ''

    def set_single_choice(self, choice_quantity, choice_name, title, is_bind_next_flow, next_flow_name):
        self.choice_quantity = choice_quantity
        self.choice_name = choice_name
        self.title = title
        self.is_bind_next_flow = is_bind_next_flow
        self.next_flow_name = next_flow_name


class InputSingle:
    input_title = ''
    input_message = ''


class Associate:
    is_associate = True
    associate_tile = ''
    flow_or_file = 0
    associate_flow_link = ''
    associate_flow_name = ''

    def flow_file_set(self, associate_choice, associate_flow_info):
        if associate_choice is not None:
            if associate_choice == 0:
                self.flow_or_file = 0
                self.associate_flow_name = associate_flow_info[0]
                self.associate_flow_link = associate_flow_info[1]
            else:
                self.flow_or_file = 1
                self.associate_flow_name = ''
                self.associate_flow_link = ''

    def associate_choose(self):
        if self.flow_or_file == 0:
            pass


def workflow_choose_session():
    pass


def create_new_workflow(user_info):
    wflow_permission_number = user_info['Permissions_info'][1][8]
    if wflow_permission_number & 0x0001 != 0:
        # print("You have permission to manage inbound items.")
        nodes = []
        flow_init_settings = {
            'flow_name': '',
            'flow_start_permission_role': '',
            'flow_': ''

        }
        flow_create_features = {
            'single_choice'
        }

        return True
    else:
        print("无权创建工作流")
        return False


def find_department_manager(name):
    user_department_case = {
        'sales': 5,
        'purchasing': 6,
        'warehouse': 7

    }
    user_info = SQLDataManage.find_user_with_name(name)
    users_list = SQLDataManage.find_user_with_name(user_info['department'])
    for user in users_list:
        if user['role'] == 'manager':
            return user

    return None
    # user = SQLDataManage.find_user_with_name(user_info['d'])


def find_user_with_role(user_role):
    user = SQLDataManage.find_user_with_user_role(user_role)
    return user

def find_user_with_name(submitter):
    user = SQLDataManage.find_user_with_name(submitter)
    return user


def find_user_with_username(username):
    user = SQLDataManage.find_user_with_username(username)
    return user


def find_leader_with_name(submitter):
    for list1 in SQLDataManage.users_load():
        for dict1 in list1:
            if dict1['username'] == submitter:
                leader_name = dict1['dir_leader']
                for group in SQLDataManage.users_load():
                    for member in group:
                        if dict1['username'] == leader_name:
                            return member


# def load_sql_flow_data():
#     pass

class SalesOrderWorkFlow:
    flow_name = ''
    # flow_type：[]
    # 流程类型编号：001-销售订单，002-采购订单，003-产品BOM，004-自定义；
    # 流程子类编号；
    # 流程子类名称：销售订单，采购订单，产品BOM，自定义；
    flow_type = ''
    user_check_id = ''
    flow_sub_type = ''
    flow_typename = ''
    submitter = ''
    contract_filepath = ''
    contract_filename = ''
    flow_submit_type = 0  # 0:立即提交，1:定时提交，2:延迟提交
    flow_create_time = ''
    flow_submit_time = ''
    flow_number = ''  # sales:SO-0001、purchase:PO-0001 + time + random number + 校验位（0-99）
    flow_state = 0  # 0:未提交，1:已提交，2:已拒绝，3:已撤销, 4:已完成, 5. 存草稿
    flow_submit_state = 0x0  # 0:start, 1:已跳转至当前节点, 2:审批完成自动跳转至下一节点, 3:等待审批, 4:已驳回请修改, 5:审批完成,
    flow_handler = ''
    flow_nodes_number = 5
    flow_nodes_info = []
    flow_nodes_state = []
    sales_flow_title_number = ''
    current_approval_user = ''
    flow_infos = []

    def __init__(self) -> None:
        pass

    def set_flow_infos(self, flow_infos):
        self.flow_type = flow_infos[0]
        self.flow_sub_type = flow_infos[1]
        self.flow_name = flow_infos[2]
        self.submitter = flow_infos[3]
        self.user_check_id = UserLogin.login_state[1]['user_check_id']
        self.flow_create_time = flow_infos[4]
        self.flow_submit_time = ''
        sql_flow_number = 'SO-0001-20230101-00010001'
        self.flow_number = self.flow_number_create()
        self.flow_state = flow_infos[4]
        # if self.flow_state == 1:
        #     self.start_approve(self.submitter)
        if self.flow_state != '4':
            self.under_approve_sql_data_save()

    def flow_number_create(self):
        if self.flow_type == '001':
            self.sales_flow_title_number = 'SO-' + self.flow_type
            self.flow_typename = Workflow_type_def.SalesFlowSubType[self.flow_type]
        # elif self.flow_type == '销售订单下发生产审批':
        #     sales_flow_title_number = 'S2PO-0001'
        # elif self.flow_type == '采购审批':
        #     sales_flow_title_number = 'PO-0001'
        # elif self.flow_type == '产品Bom审批':
        #     sales_flow_title_number = 'PBO-0001'
        # elif self.flow_type == '自定义':
        #     sales_flow_title_number = 'CUS-0001'
        flow_create_time = self.flow_create_time
        flow_submit_time = self.flow_submit_time
        random_number = str(random.randint(1, 99999)).zfill(5)
        check_number = 1
        flow_number_temp = self.sales_flow_title_number + '-' + flow_create_time + '-' + random_number
        self.flow_number = flow_number_temp + str(check_number).zfill(4)
        flow_exist_info = SQLDataManage.load_flow_data_from_sql_exist(self.flow_number)[1]
        if flow_exist_info is not None:
            if self.flow_number == flow_exist_info[1]:
                check_number += 1
                self.flow_number = flow_number_temp + str(check_number).zfill(4)
        return self.flow_number

    def under_approve_sql_data_save(self):
        flow_id = '01'
        sql_data = [
            flow_id,
            self.user_check_id,
            self.flow_number,
            self.flow_name,
            self.flow_type,
            self.flow_sub_type,
            self.submitter,
            self.flow_create_time,
            self.flow_submit_time,
            self.flow_state,
            self.flow_nodes_info,
            'backup0',
            'backup1',
            'backup2'
        ]
        self.flow_infos = sql_data
        SQLDataManage.save_flow_data_to_sql(sql_data)
        pass

    def get_flow_infos(self):
        pass

    def send_approval_to(self, approval_user):
        self.current_approval_user = 'approval_user'
        test_input = input('请输入')
        if test_input == '1':
            return [True, '审批通过']
        return [False, '']

    def start_approve(self, flow_info):
        submitter = flow_info[2]
        user_info = find_user_with_name(submitter)
        flow_nodes_info = flow_info[6]
        if flow_info[5] != 1:
            return
        if not flow_nodes_info:
            self.flow_nodes_info.append({'node0': [0x1, '', '流程开始', '']})  # 节点：状态、审批人、注释、审批人注释
            # flow_nodes_info = self.flow_nodes_info
        # else:
        #     return self.flow_nodes_info
        if self.flow_nodes_info[0]['node0'][0] & 0x1:
            self.flow_nodes_info[0]['node0'][0] = 0x2
            if user_info is not None:
                if user_info['role'] == 'manager':  # and user_info['role'] != 'leader'
                    self.flow_nodes_info.append({'node1': [0x2, '', '下级节点同一人，自动跳转', '']})
                    self.flow_nodes_info.append({'node2': [0x2, '', '下级节点同一人，自动跳转', '']})
                    pass
                elif user_info['role'] == 'leader':
                    self.flow_nodes_info.append({'node1': [0x2, '', '下级节点同一人，自动跳转', '']})
                    self.flow_nodes_info.append({'node2': [0x3, user_info['dir_lead'], '等待部门领导审批', '']})
                    approval_state = self.send_approval_to(find_user_with_username(user_info['dir_lead']))
                    if approval_state[0]:
                        self.flow_nodes_info[2]['node2'][0] = 0x2
                        self.flow_nodes_info[2]['node2'][2] = '当前节点审批完成'
                        self.flow_nodes_info[2]['node2'][3] = approval_state[1]
                    pass
                else:
                    self.flow_nodes_info.append({'node1': [0x3, user_info['dir_lead'], '等待直属上级审批', '']})
                    self.flow_nodes_info.append({'node2': []})
                    approval_state = self.send_approval_to(find_user_with_username(user_info['dir_lead']))
                    if approval_state[0]:
                        self.flow_nodes_info[1]['node1'][0] = 0x2
                        self.flow_nodes_info[1]['node1'][2] = '当前节点审批完成'
                        self.flow_nodes_info[1]['node1'][3] = approval_state[1]
                    manager = find_department_manager(user_info['name'])
                    approval_state = self.send_approval_to(manager)
                    if approval_state[0]:
                        self.flow_nodes_info[2]['node2'][0] = 0x2
                        self.flow_nodes_info[2]['node2'][2] = '当前节点审批完成'
                        self.flow_nodes_info[2]['node2'][3] = approval_state[1]
                    pass
                if self.flow_nodes_info[2]['node2'][0] == 0x2:
                    self.flow_nodes_info.append({'node3': [0x3, user_info['dir_lead'], '等待总经理审批', '']})
                    general_manager_name = find_user_with_role('general_manager')
                    approval_state = self.send_approval_to(general_manager_name)
                    if approval_state[0]:
                        self.flow_nodes_info[3]['node3'][0] = 0x2
                        self.flow_nodes_info[3]['node3'][2] = '当前节点审批完成'
                        self.flow_nodes_info[3]['node3'][3] = approval_state[1]
                        self.flow_state = 4

        self.under_approve_sql_data_save()
        pass

        threads = []
        for thread in threads:
            thread.start()

        for thread in threads:
            thread.join()


t = 'SO-455-GJGKK-GJG-55W55W-0001'
# t1 = int(t + 1)
print(str(random.randint(1, 99999)).zfill(5))
# print(datetime.now().strftime("%Y%m%d"))


test = SalesOrderWorkFlow()
test_p = ['001', '001', 'order-test', 'admin', datetime.now().strftime("%Y%m%d"), '1']
test.set_flow_infos(test_p)
flow_datas = []

current_flow = []
flow_exist = SQLDataManage.load_flow_data_from_sql_exist(test.flow_number)
if flow_exist[1] is not None:
    current_flow = flow_exist[1]
else:
    current_flow = test.flow_infos
while test.flow_state == 1:
    if test.flow_state == 4:
        # flow_info = test.under_approve_sql_data_save()
        # SQLDataManage.save_flow_data_to_sql(test.flow_info)
        break
    else:
        test.start_approve(current_flow)
