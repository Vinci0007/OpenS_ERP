from PyQt6.QtWidgets import QMessageBox, QLabel, QVBoxLayout, QHBoxLayout, QLineEdit, QPushButton, QWidget
from PyQt6 import QtCore

from CommonTools.Custom_qt5 import ClickToEditLineEdit as cteLineEdit


def on_home_profiled_clicked(action, mainWindow):
    features_page_dock = mainWindow.features_page_dock
    features_page_dock.setTitle('个人资料卡')
    features_page_dock.setStyleSheet("font-size: 19px;")
    
    ############       主布局       ############
    main_layout = QVBoxLayout()
    main_layout.setContentsMargins(150, 30, 250, 30)
    main_layout.setSpacing(10)
    # main_layout.setTitle('用户信息')
    # main_layout.setStyleSheet("font-size: 19px;")
    
        
    # ############       用户名       ############
    # username_layout = QHBoxLayout()
    # # username_label_layout = QHBoxLayout()
    # username_title = QLabel('username_title')
    # username_label = QLabel('username_label')
    
    # # 设置布局的边距为左: 10, 上: 20, 右: 10, 下: 20
    # # username_layout.setContentsMargins(200, 50, 930, 830)
    # # username_label_layout.setContentsMargins(220, 50, 900, 830)

    # # 设置布局内部各控件之间的间距为10
    # username_layout.setSpacing(10)
    # # username_label_layout.setSpacing(10)
    # username_title.setText('用 户 名：')
    # username_title.setStyleSheet("font-size: 19px;")
    # username_title.resize(80, 30)
    # username_layout.addWidget(username_title)
    # username_label.setText(mainWindow.userinfo['username'])
    # username_label.setStyleSheet("font-size: 19px;")
    # username_label.resize(80, 30)
    # username_layout.addWidget(username_label)
    # username_layout.addStretch()
    # # 设置QGroupBox的布局
    # main_layout.addLayout(username_layout)
    
    ############       名       ############
    name_layout = QHBoxLayout()
    name_layout.setSpacing(10)  
    
    name_title = QLabel('name_title')  
    name_title.setText('姓    名：')
    name_title.setStyleSheet("font-size: 19px;")
    name_title.resize(80, 30)
    name_layout.addWidget(name_title)
    
    name_label = QLabel('name_label')
    name_label.setText(mainWindow.userinfo['name'])   
    name_label.setStyleSheet("font-size: 19px;")
    name_label.resize(80, 30)
    name_layout.addWidget(name_label)

    name_layout.addStretch()
    
    main_layout.addLayout(name_layout)
    
    ############       手机       ############
    phone_layout = QHBoxLayout()
    phone_layout.setSpacing(10)    
    phone_title = QLabel('phone_title')  
    phone_title.setText('电    话：')
    phone_title.setStyleSheet("font-size: 19px;")
    phone_title.resize(80, 30)  
    phone_label = QLabel()
    phone_label.setObjectName('phone_label')
    # phone_label = cteLineEdit.ClickToEditLineEdit()
    phone_label.setText(mainWindow.userinfo['phone'])   
    phone_label.setStyleSheet("font-size: 19px;")
    phone_label.resize(80, 30)
    phone_layout.addWidget(phone_title) 
    phone_layout.addWidget(phone_label)
    phone_layout.addStretch()  
    main_layout.addLayout(phone_layout)
    
    ############       邮箱       ############
    email_layout = QHBoxLayout()
    email_layout.setSpacing(10)    
    email_title = QLabel('email_title')  
    email_title.setText('邮    箱：')
    email_title.setStyleSheet("font-size: 19px;")
    email_title.resize(80, 30)  
    email_label = QLabel('email_label')
    email_label.setText(mainWindow.userinfo['email'])   
    email_label.setStyleSheet("font-size: 19px;")
    email_label.resize(80, 30)
    email_layout.addWidget(email_title) 
    email_layout.addWidget(email_label)
    email_layout.addStretch()  
    main_layout.addLayout(email_layout)
    
    ############       所属部门       ############
    department_layout = QHBoxLayout()
    department_layout.setSpacing(10)    
    department_title = QLabel('department_title')  
    department_title.setText('所属部门')
    department_title.setStyleSheet("font-size: 19px;")
    department_title.resize(80, 30)  
    department_label = QLabel('department_label')
    department_label.setText(mainWindow.userinfo['department'])   
    department_label.setStyleSheet("font-size: 19px;")
    department_label.resize(80, 30)
    department_layout.addWidget(department_title) 
    department_layout.addWidget(department_label)
    department_layout.addStretch()  
    main_layout.addLayout(department_layout)
    
    ############       直属领导       ############
    dir_lead_layout = QHBoxLayout()
    dir_lead_layout.setSpacing(10)    
    dir_lead_title = QLabel('dir_lead_title')  
    dir_lead_title.setText('直属领导：')
    dir_lead_title.setStyleSheet("font-size: 19px;")
    dir_lead_title.resize(80, 30)  
    dir_lead_label = QLabel('dir_lead_label')
    dir_lead_label.setText(mainWindow.userinfo['dir_lead'])   
    dir_lead_label.setStyleSheet("font-size: 19px;")
    dir_lead_label.resize(80, 30)
    dir_lead_layout.addWidget(dir_lead_title) 
    dir_lead_layout.addWidget(dir_lead_label)
    dir_lead_layout.addStretch()  
    main_layout.addLayout(dir_lead_layout)
    
    ############       部门领导       ############
    # email_layout = QHBoxLayout()
    # email_layout.setSpacing(10)    
    # email_title = QLabel('email_title')  
    # email_title.setText('直属领导：')
    # email_title.setStyleSheet("font-size: 19px;")
    # email_title.resize(80, 30)  
    # email_label = QLabel('email_label')
    # email_label.setText(mainWindow.userinfo['email'])   
    # email_label.setStyleSheet("font-size: 19px;")
    # email_label.resize(80, 30)
    # email_layout.addWidget(email_title) 
    # email_layout.addWidget(email_label)
    # email_layout.addStretch()  
    # main_layout.addLayout(email_layout)
    
    ############       用户权限       ############
    permissions_layout = QHBoxLayout()
    permissions_layout.setSpacing(10)    
    permissions_title = QLabel('permissions_title')  
    permissions_title.setText('用户权限：')
    permissions_title.setStyleSheet("font-size: 19px;")
    permissions_title.resize(80, 30)  
    permissions_label = QLabel('permissions_label')
    permissions_label.setText(mainWindow.userinfo['permissions_info'])   
    permissions_label.setStyleSheet("font-size: 19px;")
    permissions_label.resize(80, 30)
    permissions_layout.addWidget(permissions_title) 
    permissions_layout.addWidget(permissions_label)
    permissions_layout.addStretch()  
    main_layout.addLayout(permissions_layout)
    
    layout_list = {
        'main_layout': main_layout,
        'name_layout': name_layout,
        'phone_layout': phone_layout,
        'email_layout': email_layout,
        'department_layout': department_layout,
        'dir_lead_layout': dir_lead_layout,
        'permissions_layout': permissions_layout,
        
        
    }
    
    
    
    
    ##########  主布局设置   ##########
    main_layout.addStretch()
    features_page_dock.setLayout(main_layout)
    ##########  修改   ##########
    change_label_list = {
        'phone_label': features_page_dock.findChild(QLabel, 'phone_label'),
    }
    ########   右侧 工具区    ##########
    current_layout = mainWindow.layout()
    right_tool_widget = QWidget(mainWindow)
    right_tools_area = QVBoxLayout(right_tool_widget)
    # right_tools_area.setGeometry(1728, 270, 180, 700)
    right_tools_area.setContentsMargins(1728, 270, 500, 20)
    right_tools_area.setSpacing(20) 
     
    profile_change_button =  QPushButton()
    # profile_change_button.setGeometry(1728, 200, 180, 40)
    profile_change_button.setStyleSheet("font-size: 21px;")
    profile_change_button.resize(80, 30)
    
    right_tools_area.addWidget(profile_change_button)
    profile_change_button.clicked.connect(lambda: on_profile_change_clicked(layout_list, right_tools_area, change_label_list, mainWindow.userinfo))
    
    right_tools_area.addStretch()
    right_tool_widget.setLayout(right_tools_area)
    if current_layout is not None:
        current_layout.addWidget(right_tool_widget)
    else:
        print("主窗口没有现有布局")
    
    
    # mainWindow.addWidget(profile_change_button)
    
    
    
def on_profile_change_clicked(layout_list, right_tools_area, change_label_list, userinfo):
    profile_confirm_button =  QPushButton()
    profile_confirm_button.setObjectName('profile_confirm_button')
    profile_confirm_button.setGeometry(1728, 270, 180, 40)
    profile_confirm_button.setStyleSheet("font-size: 21px;")     
    right_tools_area.addWidget(profile_confirm_button)
    
    phone_layout = layout_list['phone_layout']
    phone_label = change_label_list['phone_label']
    phone_label.hide()
    phone_value_label = QLineEdit()
    phone_value_label.setObjectName('phone_label_temp')
    phone_value_label.resize(80, 30)   
    if phone_layout.findChild('phone_label_temp') is None:
        phone_layout.addWidget(phone_value_label)
    phone_value = phone_value_label.text()
    if phone_value == userinfo['phone']:
        data_state = [False, '']
    else:
        data_state = [True, phone_value]
    
    profile_confirm_button.clicked.connect(lambda: on_profile_confirm_clicked(data_state, layout_list, right_tools_area, change_label_list))
    return data_state
    
    
    
    
def on_profile_confirm_clicked(data_state, layout_list, right_tools_area, change_label_list):
    phone_layout = layout_list['phone_layout']
    phone_label = change_label_list['phone_label']
    phone_layout.removeWidget('phone_label_temp')

    if data_state[0]:
            phone_label.show()
    else:
        phone_label.setText(data_state[1])
        ### 更新用户数据
        # update_user_data(data_state[1], 'phone', mainWindow)
    right_tools_area.removeWidget('profile_confirm_button')
    pass
    
# def mousePressEvent(self, event):
#     # 当鼠标单击输入框时
#     if self.isReadOnly():
#         self.setReadOnly(False)
#         # 输入框处于编辑状态时的样式
#         self.setStyleSheet("border: 1px solid black;")  # 根据需要调整边框样式
#     super(ClickToEditLineEdit, self).mousePressEvent(event)

# def focusOutEvent(self, event):
#     # 当焦点离开输入框时
#     self.setReadOnly(True)
#     self.setDefaultStyle()
#     super(ClickToEditLineEdit, self).focusOutEvent(event)

# def keyPressEvent(self, event):
#     # 当按下回车键时
#     if event.key() == Qt.Key_Return or event.key() == Qt.Key_Enter:
#         self.setReadOnly(True)
#         self.setDefaultStyle()
#     else:
#         super(ClickToEditLineEdit, self).keyPressEvent(event)