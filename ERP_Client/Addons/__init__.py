# # import BaseAddons as BaseAddons
# # from .BaseAddons import *

import os, sys

current_file_path = os.path.abspath(__file__)
addons_path = os.path.dirname(current_file_path)
sys.path.append(addons_path)

# # 获取当前目录下的所有文件和目录名
# items = os.listdir('.')

# # 过滤出以.py结尾的Python模块文件
# py_modules = [item for item in items if item.endswith('.py')]




# __version__ = "1.0"

# # __path__ = __import__('pkgutil').extend_path(__path__, __name__)

# try: 
#     from BaseAddons.MainWindow import MainWindow as mainWindow
# except ImportError:    
#     try:
#         from ...BaseAddons.MainWindow  import MainWindow as mainWindow
#     except ImportError:
#         try:
#             from ..BaseAddons.MainWindow  import MainWindow as mainWindow
#         except ImportError:
#             try:
#                 from .BaseAddons.MainWindow import MainWindow as mainWindow
#             except ImportError:
#                 try:
#                     from BaseAddons.MainWindow import MainWindow as mainWindow
#                 except:
#                     try:
#                         import MainWindow as mainWindow
#                     except:
#                         mainWindow = None




# #####################           out API       ################
# try: 
#     from CommonTools import AppConfig as appConfig
# except ImportError:    
#     try:
#         from ... import AppConfig as appConfig
#     except ImportError:
#         try:
#             from .. import AppConfig as appConfig
#         except ImportError:
#             try:
#                 import AppConfig as appConfig
#             except ImportError:
#                 appConfig = None





# try:
#     from . import BaseAddons as baseAddons
# except ImportError :
#     try:
#         import BaseAddons as baseAddons
#     except ImportError:
#         baseAddons = None
    
# try:
#     from . import HumanSource as humanSource
# except ImportError :
#     try:
#         import HumanSource as humanSource
#     except ImportError:
#         humanSource = None
    
# try:
#     from . import ProduceManade as produceManade
# except ImportError:
#     try:
#         import HumanSource as humanSource
#     except ImportError:
#         produceManade = None
    
# try:
#     from . import PurchManage as purchManage
# except ImportError:
#     try:
#         import PurchManage as purchManage
#     except ImportError:
#         purchManage = None
    
# try:
#     from . import SaleManage as saleManage
# except ImportError:
#     try:
#         import SaleManage as saleManage
#     except ImportError:
#         saleManage = None
    
# try:
#     from . import SystemManage as systemManage
# except ImportError:
#     try:
#         import SystemManage as systemManage
#     except ImportError:
#         systemManage = None
    
# try:
#     from . import TechManage as techManage
# except ImportError:
#     try:
#         import TechManage as techManage
#     except ImportError:
#         techManage = None
    
# try:
#     from . import ToolsCommon as toolsCommon
# except ImportError:
#     try:
#         import ToolsCommon as toolsCommon
#     except ImportError:
#         toolsCommon = None
    
# try:
#     from . import UsersManage as usersManage
# except ImportError:
#     try:
#         import UsersManage as usersManage
#     except ImportError:
#         usersManage = None
    
# try:
#     from . import WareHouse as wareHouse
# except ImportError:
#     try:
#         import WareHouse as wareHouse
#     except ImportError:
#         wareHouse = None
    
# try:
#     from . import WorkFlow as workFlow
# except ImportError:
#     try:
#         import WorkFlow as workFlow
#     except ImportError:
#         workFlow = None
    
# try:
#     from . import addons_manage as addonsManage
# except ImportError:
#     try:
#         import addons_manage as addonsManage
#     except ImportError:
#         addonsManage = None
 
# # try:
# #     import Addons.addons_func_list as addonsFuncList
# # except ImportError:
# #     try:
# #         from . import addons_func_list as addonsFuncList
# #     except ImportError:
# #         try:
# #             import addons_func_list as addonsFuncList
# #         except ImportError:
# #             addonsFuncList = None
    
# # try:
# #     from . import menu_with_button_set as menuWithButtonSet
# # except ImportError:
# #     try:
# #         import menu_with_button_set as menuWithButtonSet
# #     except ImportError:
# #         menuWithButtonSet = None   





# #####################           baseAddons       ################
# try:
#     from .BaseAddons.server_sql import server_data_format as serverDataFormat
# except ImportError:
#     try:
#         from BaseAddons.server_sql import server_data_format as serverDataFormat
#     except ImportError:
#         try:
#             import server_sql as serverDataFormat
#         except ImportError:
#             serverDataFormat = None
            
# try:
#     from .BaseAddons.User import UserProfile as userProfile
# except ImportError:
#     try:
#         from BaseAddons.User import UserProfile as userProfile
#     except ImportError:
#         try:
#             import UserProfile as userProfile
#         except ImportError:
#             userProfile = None
            
# try:
#     from .BaseAddons.UserPermissionManage import WareHousePermission as wareHousePermission
# except ImportError:
#     try:
#         from BaseAddons.UserPermissionManage import WareHousePermission as wareHousePermission
#     except ImportError:
#         try:
#             import UserPermissionManage as wareHousePermission
#         except ImportError:
#             try:
#                 import WareHousePermission as wareHousePermission
#             except ImportError:
#                 wareHousePermission = None
            
# #####################           Tools       ################
            
# try:
#     from .ToolsCommon import FuncQR as funcQR
# except ImportError:
#     try:
#         from ToolsCommon import FuncQR as funcQR
#     except ImportError:
#         try:
#             import FuncQR as funcQR
#         except ImportError:
#             funcQR = None
            
# try:
#     from .ToolsCommon.FuncQR import QRClientConfig as qrClientConfig
# except ImportError:
#     try:
#         from ToolsCommon.FuncQR import QRClientConfig as qrClientConfig
#     except ImportError:
#         try:
#             import FuncQR as qrClientConfig
#         except ImportError:
#             qrClientConfig = None

# try:
#     from .ToolsCommon.FuncQR import CreateProductQR as createQR
# except ImportError:
#     try:
#         from ToolsCommon.FuncQR import CreateProductQR as createQR
#     except ImportError:
#         try:
#             import CreateProductQR as createQR
#         except ImportError:
#             createQR = None
            
# try:
#     from .ToolsCommon.FuncQR import ScanProductQR as scanQR
# except ImportError:
#     try:
#         from ToolsCommon.FuncQR import ScanProductQR as scanQR
#     except ImportError:
#         try:
#             import ScanProductQR as scanQR
#         except ImportError:
#             scanQR = None  


# #####################           warehouse       ################

# try:
#     from .WareHouse import WarehouseManage as warehouseManage
# except ImportError:
#     try:
#         from WareHouse import WarehouseManage as warehouseManage
#     except ImportError:
#         try:
#             import WarehouseManage as warehouseManage
#         except ImportError:
#             warehouseManage = None

# try:
#     from .WareHouse import InBoundManage as inBoundManage
# except ImportError:
#     try:
#         from WareHouse import InBoundManage as inBoundManage
#     except ImportError:
#         try:
#             import InBoundManage as inBoundManage
#         except ImportError:
#             inBoundManage = None
            
# try:
#     from .WareHouse import OutBoundManage as outBoundManage
# except ImportError:
#     try:
#         from WareHouse import OutBoundManage as outBoundManage
#     except ImportError:
#         try:
#             import OutBoundManage as outBoundManage
#         except ImportError:
#             outBoundManage = None
            
# try:
#     from .WareHouse import InventoryManage as inventoryManage
# except ImportError:
#     try:
#         from WareHouse import InventoryManage as inventoryManage
#     except ImportError:
#         try:
#             import InventoryManage as inventoryManage
#         except ImportError:
#             inventoryManage = None
            

            

            
            
            
#  ###########插件外部接口
#  ###########程序内导入
            
# # try:
# #     from .WareHouse import InventoryManage as inventoryManage
# # except ImportError:
# #     try:
# #         from WareHouse import InventoryManage as inventoryManage
# #     except ImportError:
# #         try:
# #             import InventoryManage as inventoryManage
# #         except ImportError:
# #             inventoryManage = None

# # module_list_info = {
# #     'baseAddons'        : baseAddons,
# #     'humanSource'       : humanSource,
# #     'produceManade'     : produceManade,
# #     'purchManage'       : purchManage,
# #     'saleManage'        : saleManage,
# #     'systemManage'      : systemManage,
# #     'techManage'        : techManage,
# #     'toolsCommon'       : toolsCommon,
# #     'usersManage'       : usersManage,
# #     'wareHouse'         : wareHouse,
# #     'workFlow'          : workFlow,
# #     'addonsManage'      : addonsManage,
# #     # 'addonsFuncList'    : addonsFuncList,
# #     # 'menuWithButtonSet' : menuWithButtonSet,
    
    
# #  }  
# # class module_list_init:
# #     baseAddons_module       = baseAddons
# #     humanSource_module      = humanSource      
# #     produceManade_module    = produceManade     
# #     purchManage_module      = purchManage    
# #     saleManage_module       = saleManage     
# #     systemManage_module     = systemManage       
# #     techManage_module       = techManage     
# #     toolsCommon_module      = toolsCommon   
# #     usersManage_module      = usersManage    
# #     wareHouse_module        = wareHouse      
# #     workFlow_module         = workFlow
    
# #     inBoundManage_module    = inBoundManage
# #     outBoundManage_module   = outBoundManage
# #     inventoryManage_module  = inventoryManage
           
# #     addonsManage_module     = addonsManage  
# #     # addonsFuncList_module   = addonsFuncList
# #     # menuWithButtonSet_module = menuWithButtonSet   


    
    
    
# def init():
#     if py_modules is not None:
#         return ('module exists !')
#     else:
#         return ('module fault !')
    
# # def find_qt():
# #     import os, sys

# #     qtcore_dll = '\\Qt5Core.dll'

# #     dll_dir = os.path.dirname(sys.executable)
# #     if not os.path.isfile(dll_dir + qtcore_dll):
# #         path = os.environ['PATH']

# #         dll_dir = os.path.dirname(__file__) + '\\Qt5\\bin'
# #         if os.path.isfile(dll_dir + qtcore_dll):
# #             path = dll_dir + ';' + path
# #             os.environ['PATH'] = path
# #         else:
# #             for dll_dir in path.split(';'):
# #                 if os.path.isfile(dll_dir + qtcore_dll):
# #                     break
# #             else:
# #                 return

# #     try:
# #         os.add_dll_directory(dll_dir)
# #     except AttributeError:
# #         pass


# # find_qt()
# # del find_qt