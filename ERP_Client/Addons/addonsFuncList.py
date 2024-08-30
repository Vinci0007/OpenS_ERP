try:
    from Addons import BaseAddons as baseAddons
except ImportError :
    try:
        import BaseAddons as baseAddons
    except ImportError:
        baseAddons = None
    
try:
    from Addons import HumanSource as humanSource
except ImportError :
    try:
        import HumanSource as humanSource
    except ImportError:
        humanSource = None
    
try:
    from Addons import ProduceManade as produceManade
except ImportError:
    try:
        import HumanSource as humanSource
    except ImportError:
        produceManade = None
    
try:
    from Addons import PurchManage as purchManage
except ImportError:
    try:
        import PurchManage as purchManage
    except ImportError:
        purchManage = None
    
try:
    from Addons import SaleManage as saleManage
except ImportError:
    try:
        import SaleManage as saleManage
    except ImportError:
        saleManage = None
    
try:
    from Addons import SystemManage as systemManage
except ImportError:
    try:
        import SystemManage as systemManage
    except ImportError:
        systemManage = None
    
try:
    from Addons import TechManage as techManage
except ImportError:
    try:
        import TechManage as techManage
    except ImportError:
        techManage = None
    
try:
    from Addons import ToolsCommon as toolsCommon
except ImportError:
    try:
        import ToolsCommon as toolsCommon
    except ImportError:
        toolsCommon = None
    
try:
    from Addons import UsersManage as usersManage
except ImportError:
    try:
        import UsersManage as usersManage
    except ImportError:
        usersManage = None
    
try:
    from Addons import WareHouse as wareHouse
except ImportError:
    try:
        import WareHouse as wareHouse
    except ImportError:
        wareHouse = None
    
try:
    from Addons import WorkFlow as workFlow
except ImportError:
    try:
        import WorkFlow as workFlow
    except ImportError:
        workFlow = None

try:
    from Addons.WareHouse import InBoundManage as inBoundManage
except ImportError:
    try:
        from WareHouse import InBoundManage as inBoundManage
    except ImportError:
        try:
            import InBoundManage as inBoundManage
        except ImportError:
            inBoundManage = None
            
try:
    from Addons.WareHouse import OutBoundManage as outBoundManage
except ImportError:
    try:
        from WareHouse import OutBoundManage as outBoundManage
    except ImportError:
        try:
            import OutBoundManage as outBoundManage
        except ImportError:
            outBoundManage = None
            
try:
    from Addons.WareHouse import InventoryManage as inventoryManage
except ImportError:
    try:
        from WareHouse import InventoryManage as inventoryManage
    except ImportError:
        try:
            import InventoryManage as inventoryManage
        except ImportError:
            inventoryManage = None
            
from Addons.BaseAddons.UserPermissionManage import WareHousePermission as whperm

homeButton_submenuList = {
    
    'home_clashboard'   : {'opened': True   , 'icon': 'icon', 'submenuList': None, 'title': '   仪 表 板   '},
    'home_profile'      : {'opened': True   , 'icon': 'icon', 'submenuList': None, 'title': '   资 料 卡   '},
    'home_companyArch'  : {'opened': True   , 'icon': 'icon', 'submenuList': None, 'title': '   组织架构   '},
    'home_backup0'      : {'opened': False  , 'icon': 'icon', 'submenuList': None, 'title': '   开发中..   '},
    'home_backup1'      : {'opened': False  , 'icon': 'icon', 'submenuList': None, 'title': '   开发中..   '},
    'home_backup2'      : {'opened': False  , 'icon': 'icon', 'submenuList': None, 'title': '   开发中..   '},
    'home_backup3'      : {'opened': False  , 'icon': 'icon', 'submenuList': None, 'title': '   开发中..   '},
    'home_sysSetting'   : {'opened': True   , 'icon': 'icon', 'submenuList': None, 'title': '   系统设置   '},
}

menuBar_homeButton = {
    'title'         : '  首页  ',
    'objectName'    : 'buttonMenu_home',
    'icon'          : ':/icon/home.png',
    'submenuList'   : homeButton_submenuList,
    'setStyleSheet' : ("font-size: 13px;border: 1px solid lightgray; border-radius: 5px;"),
    
}




wareButton_submenuList = {
    'wh_inbound'        : {'opened': False, 'icon': 'icon', 'submenuList': None, 'title': '   入库管理   '},
    'wh_outbound'       : {'opened': False, 'icon': 'icon', 'submenuList': None, 'title': '   出库管理   '},
    'wh_inventory'      : {'opened': False, 'icon': 'icon', 'submenuList': None, 'title': '   库存管理   '},
    'wh_backup0'        : {'opened': False, 'icon': 'icon', 'submenuList': None, 'title': '   开发中..   '},
    'wh_backup1'        : {'opened': False, 'icon': 'icon', 'submenuList': None, 'title': '   开发中..   '},
    'wh_backup2'        : {'opened': False, 'icon': 'icon', 'submenuList': None, 'title': '   开发中..   '},
    'wh_backup3'        : {'opened': False, 'icon': 'icon', 'submenuList': None, 'title': '   开发中..   '},
    
    
}

apvlButton_submenuList = {
    'apvl_launch'       : {'opened': True, 'icon': 'icon', 'submenuList': None, 'title': '   发起申请   '},
    'apvl_waitme'       : {'opened': True, 'icon': 'icon', 'submenuList': None, 'title': '   待    办   '},
    'apvl_waitme'       : {'opened': True, 'icon': 'icon', 'submenuList': None, 'title': '   已    办   '},
    'apvl_loading'      : {'opened': True, 'icon': 'icon', 'submenuList': None, 'title': '   流 程 中   '},
    'apvl_done'         : {'opened': True, 'icon': 'icon', 'submenuList': None, 'title': '   已 完 成   '},
    'apvl_submit'       : {'opened': True, 'icon': 'icon', 'submenuList': None, 'title': '   已 提 交   '},
    'apvl_CCme'         : {'opened': True, 'icon': 'icon', 'submenuList': None, 'title': '   抄 送 我   '},
    'wh_backup0'        : {'opened': False, 'icon': 'icon', 'submenuList': None, 'title': '   开发中..   '},
    'wh_backup1'        : {'opened': False, 'icon': 'icon', 'submenuList': None, 'title': '   开发中..   '},
    'wh_backup2'        : {'opened': False, 'icon': 'icon', 'submenuList': None, 'title': '   开发中..   '},
    'wh_backup3'        : {'opened': False, 'icon': 'icon', 'submenuList': None, 'title': '   开发中..   '},
    
}


departFuncButton_submenuList = {
    'apvl_menu_button'  : {'opened': True   , 'icon': 'icon', 'submenuList': apvlButton_submenuList, 'title': '   审    批   '},
    'tech_menu_button'  : {'opened': True   , 'icon': 'icon', 'submenuList': None, 'title': '   技    术   '},
    'sale_menu_button'  : {'opened': True   , 'icon': 'icon', 'submenuList': None, 'title': '   销    售   '},
    'prod_menu_button'  : {'opened': True   , 'icon': 'icon', 'submenuList': None, 'title': '   生    产   '},
    'purc_menu_button'  : {'opened': True   , 'icon': 'icon', 'submenuList': None, 'title': '   采    购   '},
    'ware_menu_button'  : {'opened': True   , 'icon': 'icon', 'submenuList': wareButton_submenuList, 'title': '   仓    储   '},
    'husr_menu_button'  : {'opened': True   , 'icon': 'icon', 'submenuList': None, 'title': '   人事行政   '},
    'sysm_menu_button'  : {'opened': True   , 'icon': 'icon', 'submenuList': None, 'title': '   成员管理   '},
    'cms0_menu_button'  : {'opened': False   , 'icon': 'icon', 'submenuList': None, 'title': '   ComSoon.   '},
    'cms1_menu_button'  : {'opened': False  , 'icon': 'icon', 'submenuList': None, 'title': '   ComSoon.   '},
    'cms2_menu_button'  : {'opened': False  , 'icon': 'icon', 'submenuList': None, 'title': '   ComSoon.   '},
}

menuBar_departFuncButton = {
    'title'         : '  功能  ',
    'objectName'    : 'buttonMenu_home',
    'icon'          : ':/icon/departFunc.png',
    'submenuList'   : departFuncButton_submenuList,   
    'setStyleSheet' : ("font-size: 13px;border: 1px solid lightgray; border-radius: 5px;"),
}



def addons_func_list_init(userPermissionInfo):
#init data

    if wareHouse is not None:
        if inBoundManage is not None:
            isAllow = whperm.inbound_permission(userPermissionInfo)
            if isAllow == True:
                wareButton_submenuList['wh_inbound']['opened'] = True
        if outBoundManage is not None:
            isAllow = whperm.outbound_permission(userPermissionInfo)
            if isAllow == True:
                wareButton_submenuList['wh_inventory']['opened'] = True
            wareButton_submenuList['wh_outbound']['opened'] = True
        if inventoryManage is not None:
            isAllow = whperm.inventory_permission(userPermissionInfo)
            if isAllow == True:
                wareButton_submenuList['wh_inventory']['opened'] = True
            
    return {'menuBar_homeButton':       menuBar_homeButton,
            'menuBar_departFuncButton': menuBar_departFuncButton}
    









