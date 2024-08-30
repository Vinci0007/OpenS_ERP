from PyQt6.QtWidgets import  QPushButton,  QToolButton, QMenuBar, QLabel, QLineEdit, QMessageBox
from PyQt6.QtWidgets import QWidgetAction, QHBoxLayout, QWidget, QToolBar, QMenu, QSizePolicy, QMenuBar
from PyQt6.QtGui import QIcon, QPixmap
from PyQt6.QtCore import QSize, Qt

from datetime import datetime
import sys, os

from Addons import addonsFuncList as addfl
from Addons.WareHouse import InBoundManage as inboundM, OutBoundManage as outboundM, InventoryManage as inventM
from Addons.WorkFlow import WorkFlowLaunch as wfla

# exitIcon = 'Resource/Icon/exit.png'
# is_exiticon_ = os.path.isfile(exitIcon)
# image = Image.open(exitIcon)
# image.show()


def b_menus(mainWindow):
    # InstantPopup = QToolButton.ToolButtonPopupMode.InstantPopup   
    toolBar = mainWindow.toolbar
    menuBar = mainWindow.customMenuBar
    menuBarSize = menuBar.size()
    menuBarWidth = menuBarSize.width()
    menuBarHeight = menuBarSize.height()
    function_list_info = addfl.addons_func_list_init(mainWindow.userinfo['permissions_info'])
    # function_active_info = addfl.addons_func_list_init(widget.uerinfo)
    
    menuBarAction_dict = {}
    
    right_toolbar = QToolBar("右侧工具栏")
    mainWindow.addToolBar(Qt.ToolBarArea.RightToolBarArea, right_toolbar)
    search_box = QLineEdit()
    search_box.resize(120, 60)
    search_box.setPlaceholderText("Search...")
    search_box.setObjectName('search_box')
    funcPosition_label = QLabel("..")
    funcPosition_label.setObjectName('funcPosition_label')
    right_toolbar.addWidget(funcPosition_label)
    right_toolbar.addWidget(search_box)
    search_box.setMaximumWidth(200)
    # menuBar.setCornerWidget(search_funcPosition_toolbar, Qt.AnchorPoint.AnchorHorizontalCenter)
    
    exit_button = QPushButton()
    scale_button = QPushButton()
    mini_button = QPushButton()
    exit_buttonIcon = 'Resource/Icon/exit_pink.png'
    if os.path.exists(exit_buttonIcon):
        exit_button.setIcon(QIcon(exit_buttonIcon))
    exit_button.setIconSize(QSize(19, 19))
    scale_buttonIcon = 'Resource/Icon/maximize__blue.png'
    if os.path.exists(scale_buttonIcon):
        scale_button.setIcon(QIcon(scale_buttonIcon))
    scale_button.setIconSize(QSize(19, 19))
    mini_buttonIcon = 'Resource/Icon/minimize_dian.png'
    if os.path.exists(mini_buttonIcon):
        mini_button.setIcon(QIcon(mini_buttonIcon))
    mini_button.setIconSize(QSize(19, 19))
    exit_button.setObjectName('exit_button')
    scale_button.setObjectName('scale_button')
    mini_button.setObjectName('mini_button')
    sftOperateToolArea = QWidget()
    sftOperateToolArea.setStyleSheet("background-color: none")
    right_tool_barlayout = QHBoxLayout()
    right_tool_barlayout.addWidget(mini_button)
    right_tool_barlayout.addWidget(scale_button)
    right_tool_barlayout.addWidget(exit_button)
    sftOperateToolArea.setLayout(right_tool_barlayout)
    exit_button.setStyleSheet("border: none;")
    scale_button.setStyleSheet("border: none;")
    mini_button.setStyleSheet("border: none;")
    menuBar.setCornerWidget(sftOperateToolArea, Qt.Corner.TopRightCorner)
    exit_button.clicked.connect(mainWindow.close)
    scale_button.clicked.connect(mainWindow.maximizeWindow)
    mini_button.clicked.connect(mainWindow.minimizeWindow)

    #######################
    ## home
    #######################
    home_menu_info = function_list_info['menuBar_homeButton']
    home_menu = menuBar.addMenu(home_menu_info['title'])
    home_menu.setObjectName(home_menu_info['objectName'])
    home_menu.setStyleSheet(home_menu_info['setStyleSheet'])
    # home_menu.setStyleSheet("QMenu::item[isSpecial_menuActionButton='true'] {color: grey;}")
    # home_menu.setStyleSheet("border: 1px solid lightgray; border-radius: 5px;")
    ##########   菜单项   ###########
    if home_menu_info['submenuList'] is not None:
        for key, value in home_menu_info['submenuList'].items():
            key_subMenuList = value['submenuList']
            menuActionButton = home_menu.addAction(value['title'])
            menuActionButton.setObjectName(key)
            menuBarAction_dict.update({key: menuActionButton})
            if value['opened'] == False:
                menuActionButton.setEnabled(False)  
                menuBarAction_dict.update({key: {'actionName': menuActionButton, 'opened': True}})   
            else:
                menuBarAction_dict.update({key: {'actionName': menuActionButton, 'opened': False}})       
                
            home_menu.addSeparator()
            if  key_subMenuList is not None:
                sub_menu = QMenu(key, mainWindow)      ####必须设置父对象，否则无法显示
                menuActionButton.setMenu(sub_menu)
                sub_menu.setStyleSheet(departFunc_menu_info['setStyleSheet'])
                sub_menu.setObjectName('sub_departFunc_menu')
                for sub_key, sub_value in key_subMenuList.items():
                    key_sub_menuButtonList = sub_value['submenuList']
                    sub_menuActionButton = sub_menu.addAction(sub_value['title'])
                    sub_menuActionButton.setObjectName(sub_key)
                    menuBarAction_dict.update({sub_key: sub_menuActionButton})
                    if sub_value['opened'] == False:
                        sub_menuActionButton.setEnabled(False) 
                        menuBarAction_dict.update({sub_key: {'actionName': sub_menuActionButton, 'opened': True}})   
                    else:
                        menuBarAction_dict.update({sub_key: {'actionName': sub_menuActionButton, 'opened': False}})   
                    sub_menu.addSeparator()
                    menuActionButton.setParent(sub_menu)
    #######################
    ## main funcion
    #######################
    departFunc_menu_info = function_list_info['menuBar_departFuncButton']
    departFunc_menu = menuBar.addMenu(departFunc_menu_info['title'])
    departFunc_menu.setObjectName(departFunc_menu_info['objectName'])
    departFunc_menu.setStyleSheet(departFunc_menu_info['setStyleSheet'])
    ############   菜单项   ###########
    if departFunc_menu_info['submenuList'] is not None:
        for key, value in departFunc_menu_info['submenuList'].items():
            key_subMenuList = value['submenuList']
            menuActionButton = departFunc_menu.addAction(value['title'])
            menuActionButton.setObjectName(key)
            
            if value['opened'] == False:
                menuActionButton.setEnabled(False)  
                menuBarAction_dict.update({key: {'actionName': menuActionButton, 'opened': False}})   
            else:
                menuBarAction_dict.update({key: {'actionName': menuActionButton, 'opened': True}})
            departFunc_menu.addSeparator()
            
            if  key_subMenuList is not None:
                sub_menu = QMenu(key, mainWindow)      ####必须设置父对象，否则无法显示
                menuActionButton.setMenu(sub_menu)
                sub_menu.setStyleSheet(departFunc_menu_info['setStyleSheet'])
                sub_menu.setObjectName('sub_departFunc_menu')
                for sub_key, sub_value in key_subMenuList.items():
                    sub_sub_menuButtonList = sub_value['submenuList']
                    sub_menuActionButton = sub_menu.addAction(sub_value['title'])
                    sub_menuActionButton.setObjectName(sub_key)
                    menuBarAction_dict.update({sub_key: sub_menuActionButton})
                    if sub_value['opened'] == False:
                        sub_menuActionButton.setEnabled(False) 
                        menuBarAction_dict.update({sub_key: {'actionName': sub_menuActionButton, 'opened': False}})   
                    else:
                        menuBarAction_dict.update({sub_key: {'actionName': sub_menuActionButton, 'opened': True}}) 
                    sub_menu.addSeparator()
                    sub_menuActionButton.setParent(sub_menu)
                
                
                
    #########################################################################################################
    #########################################################################################################
    ##################              action bind                                             #################
    #########################################################################################################
    #########################################################################################################
                
    inbound_action_info = menuBarAction_dict['wh_inbound'] 
    if inbound_action_info['opened'] == True:
        inbound_action_info['actionName'].triggered.connect(lambda: inboundM.on_wh_inbound_clicked(mainWindow, right_toolbar))
    
    outbound_action_info = menuBarAction_dict['wh_outbound'] 
    if outbound_action_info['opened'] == True:
        outbound_action_info['actionName'].triggered.connect(lambda: outboundM.on_wh_outbound_clicked(mainWindow, right_toolbar))
        
    inventory_action_info = menuBarAction_dict['wh_inventory'] 
    if inventory_action_info['opened'] == True:
        inventory_action_info['actionName'].triggered.connect(lambda: inventM.on_wh_inventory_clicked(mainWindow, right_toolbar))
        
    apvl_launch_action_info = menuBarAction_dict['apvl_launch'] 
    if apvl_launch_action_info['opened'] == True:
        apvl_launch_action_info['actionName'].triggered.connect(lambda: wfla.on_apvl_launch_Clicked(mainWindow, right_toolbar))
                
  
    
    
    
    

    
    
    
