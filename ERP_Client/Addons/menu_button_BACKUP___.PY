from PyQt6.QtWidgets import  QMenu, QToolButton, QAction, QMenuBar
from PyQt6.QtCore import QSize

from Addons.addons_manage import profile as pfl
from Addons.addons_manage import inBoundManage as ibma
from Addons.addons_manage import warehouseManage as wbm
# from Addons.addons_manage import get_inBoundManage, get_warehouseManage
# ibma = get_inBoundManage()
# wbm = get_warehouseManage()

    
    # menuBar = QMenuBar()
    # menuBar.setStyleSheet("font-size: 15px;")
    # # toolbar = widget.addToolBar("菜 单 栏")
    # widget.setMenuBar(menuBar)
    ######
    #两种方式：
    ## 1. home_menu = menuBar.addMenu('   首    页   ')
    ##    home_menu.setObjectName('buttonMenu_home')
    ####  home_menu 作为QMenur 对象，预先添加进bar, 然后再设置菜单项
    ## 2. wh_menu = QMenu(widget)  先创建一个QMenu对象，然后添加到bar，父类直接指定主窗口
    ####  menuBar.addMenu(wh_menu)  指定了父类主窗口，add添加进bar才有用



def b_menus(widget):
    InstantPopup = QToolButton.ToolButtonPopupMode.InstantPopup
    
    toolBar = widget.toolbar
    menuBar = widget.menuBar
    
    # menuBar = QMenuBar()
    # menuBar.setStyleSheet("font-size: 15px;")
    # # toolbar = widget.addToolBar("菜 单 栏")
    # widget.setMenuBar(menuBar)
    ######
    #两种方式：
    ## 1. home_menu = menuBar.addMenu('   首    页   ')
    ##    home_menu.setObjectName('buttonMenu_home')
    ####  home_menu 作为QMenur 对象，预先添加进bar, 然后再设置菜单项
    ## 2. wh_menu = QMenu(widget)  先创建一个QMenu对象，然后添加到bar，父类直接指定主窗口
    ####  menuBar.addMenu(wh_menu)  指定了父类主窗口，add添加进bar才有用
    #######################
    ## home
    #######################

    home_menu = menuBar.addMenu('   首    页   ')
    home_menu.setObjectName('buttonMenu_home')
    ##########   菜单项   ###########
    home_clashboard_l1 = home_menu.addAction('   仪表板   ')
    home_profile_l1 = home_menu.addAction('   个人资料卡   ')
    home_menu.addSeparator()  # 添加一个分隔符
    home_backup1_l1 = home_menu.addAction('   开发中.   ')
    home_backup2_l1 = home_menu.addAction('   开发中..   ')
    home_backup3_l1 = home_menu.addAction('   开发中...   ')
    home_menu.addSeparator()  # 添加一个分隔符
    home_menu.addSeparator()  # 添加一个分隔符
    home_sysSetting_l1 = home_menu.addAction('   系统设置   ')
    #########   菜单项   ###########
    #########   。。。   ###########
    home_menu.setStyleSheet("font-size: 13px;")
    
    
    ############        action bind         ###########
    home_profile_l1.triggered.connect(lambda: pfl.on_home_profiled_clicked(home_profile_l1, widget))
    
    
    #######################
    ## warehouse
    #######################
    wh_menu = QMenu(widget)
    wh_menu.setTitle('   仓库管理   ')
    # wh_menu = menuBar.addMenu('   仓库管理   ')
    wh_menu.setObjectName('buttonMenu_warehouse')
    ##########   菜单项   ###########
    isPermit = wbm.warehouse_permission(widget.userinfo)      
    #判断用户权限
    if not isPermit or wbm is None:
        wh_menu.setEnabled(False)  # 禁用按钮
        wh_menu.setStyleSheet("background-color: #C0C0C0; color: #808080;")
    inbound_permission = ibma.inbound_permission(widget.userinfo)
    wh_inbound_l1 = wh_menu.addAction('   入库管理   ')
    if not inbound_permission or ibma is None:
        wh_inbound_l1.setEnabled(False)  # 禁用按钮
        wh_inbound_l1.setDisabled(True)  # 设置按钮为灰色  
        # menu_bar.setActiveAction(wh_inbound_l1)     
    wh_outbound_l1 = wh_menu.addAction('   出库管理   ')
    wh_inventory_l1 = wh_menu.addAction('   库存管理   ')
    wh_menu.addSeparator()  # 添加一个分隔符
    wh_backup1_l1 = wh_menu.addAction('   开发中.   ')
    wh_backup2_l1 = wh_menu.addAction('   开发中..   ')
    wh_backup3_l1 = wh_menu.addAction('   开发中...   ')
    wh_menu.addSeparator()  # 添加一个分隔符
    wh_backup4_l1 = wh_menu.addAction('   ...   ')

    wh_menu.setStyleSheet("font-size: 13px;")
    menu = menuBar.addMenu(wh_menu)
    menu.setObjectName('buttonMenu_warehouse')
    
    ############        action bind         ###########
    wh_inbound_l1.triggered.connect(lambda: ibma.on_wh_inbound_clicked(wh_inbound_l1, warehouse_button, widget))
    
    
    
    
    
    
    ###################################################################################################
    ## APPROVAL
    ###################################################################################################
    apvl_menu = menuBar.addMenu('   审    批   ')
    apvl_menu.setObjectName('buttonMenu_home')
    ##########   菜单项   ###########
    apvl_request_l1 = apvl_menu.addAction('   发起申请   ')
    apvl_done_l1 = apvl_menu.addAction('   已办   ')
    apvl_menu.addSeparator()  # 添加一个分隔符
    apvl_pending_l1 = apvl_menu.addAction('   待办   ')
    apvl_CC_me_l1 = apvl_menu.addAction('   抄送我   ')
    apvl_submited_l1 = apvl_menu.addAction('   已发起   ')
    apvl_processing_l1 = apvl_menu.addAction('   流程中   ')
    apvl_completed_l1 = apvl_menu.addAction('   已完成   ')
    apvl_menu.addSeparator()  # 添加一个分隔符
    apvl_menu.addSeparator()  # 添加一个分隔符
    apvl_backup1_l1 = apvl_menu.addAction('   开发中.   ')
    apvl_backup2_l1 = apvl_menu.addAction('   开发中..   ')
    apvl_backup3_l1 = apvl_menu.addAction('   开发中...   ')
    apvl_menu.addSeparator()  # 添加一个分隔符
    wh_backup4_l1 = apvl_menu.addAction('   ...   ')
    apvl_menu.setStyleSheet("font-size: 13px;")
    
    
    #######################
    ## SALES
    #######################
    warehouse_button = widget.buttonMenu['buttonMenu_sale']