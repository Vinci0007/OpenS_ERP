import sys
import os

# 获取当前Python解释器的路径
# exe_path = sys.executable
exe_path = sys.executable

def createPath_module(path):

    # 构造自建模块的路径
    addons_path = []
    addons_path.append(os.path.join(os.path.dirname(path), 'Addons'))
    addons_path.append(os.path.join(os.path.dirname(path), 'CommonTools'))
    addons_path.append(os.path.join(os.path.dirname(path), 'Addons/BaseAddons'))
    addons_path.append(os.path.join(os.path.dirname(path), 'Addons/BaseAddons/MainWindow'))
    addons_path.append(os.path.join(os.path.dirname(path), 'Addons/BaseAddons/MainWindow/MainWindow.py'))
    addons_path.append(os.path.join(os.path.dirname(path), 'Addons/BaseAddons/server_sql'))
    addons_path.append(os.path.join(os.path.dirname(path), 'Addons/BaseAddons/server_sql/server_data_format.py'))
    addons_path.append(os.path.join(os.path.dirname(path), 'Addons/BaseAddons/User'))
    addons_path.append(os.path.join(os.path.dirname(path), 'Addons/BaseAddons/User/UserProfile.py'))
    addons_path.append(os.path.join(os.path.dirname(path), 'Addons/BaseAddons/UserPermissionManage'))
    addons_path.append(os.path.join(os.path.dirname(path), 'Addons/BaseAddons/UserPermissionManage/WareHousePermission.py'))
    addons_path.append(os.path.join(os.path.dirname(path), 'Addons/HumanSource'))
    addons_path.append(os.path.join(os.path.dirname(path), 'Addons/WareHouse'))
    addons_path.append(os.path.join(os.path.dirname(path), 'Addons/WareHouse/InBoundManage.py'))
    addons_path.append(os.path.join(os.path.dirname(path), 'Addons/WareHouse/InventoryManage.py'))
    addons_path.append(os.path.join(os.path.dirname(path), 'Addons/WareHouse/OutBoundManage.py'))
    addons_path.append(os.path.join(os.path.dirname(path), 'Addons/WareHouse/WarehouseManage.py'))
    addons_path.append(os.path.join(os.path.dirname(path), 'Addons/WareHouse/Tools'))
    addons_path.append(os.path.join(os.path.dirname(path), 'Addons/WareHouse/Tools/WarehouseDataCacheManage.py'))
    addons_path.append(os.path.join(os.path.dirname(path), 'Addons/WareHouse/Tools/WarehouseServerData.py'))
    addons_path.append(os.path.join(os.path.dirname(path), 'Addons/WorkFlow'))
    addons_path.append(os.path.join(os.path.dirname(path), 'Addons/WorkFlow/WorkFlowClass.py'))
    addons_path.append(os.path.join(os.path.dirname(path), 'Addons/ToolsCommon'))
    addons_path.append(os.path.join(os.path.dirname(path), 'Addons/ToolsCommon/FuncQR'))
    addons_path.append(os.path.join(os.path.dirname(path), 'Addons/ToolsCommon/FuncQR/CreateProductQR.py'))
    addons_path.append(os.path.join(os.path.dirname(path), 'Addons/ToolsCommon/FuncQR/QRClientConfig.py'))
    addons_path.append(os.path.join(os.path.dirname(path), 'Addons/ToolsCommon/FuncQR/ScanProductQR.py'))
    addons_path.append(os.path.join(os.path.dirname(path), 'CommonTools/Custom_qt5'))
    addons_path.append(os.path.join(os.path.dirname(path), 'CommonTools/Custom_qt5/ClickToEditLineEdit.py'))
    addons_path.append(os.path.join(os.path.dirname(path), 'CommonTools/Data'))
    addons_path.append(os.path.join(os.path.dirname(path), 'CommonTools/Data/Bom_data_manage'))
    addons_path.append(os.path.join(os.path.dirname(path), 'CommonTools/Data/Bom_data_manage/BomData.py'))
    addons_path.append(os.path.join(os.path.dirname(path), 'CommonTools/Data/QR_Data'))
    addons_path.append(os.path.join(os.path.dirname(path), 'CommonTools/Office_tools'))
    addons_path.append(os.path.join(os.path.dirname(path), 'CommonTools/Office_tools/ExcleDataRead.py'))
    addons_path.append(os.path.join(os.path.dirname(path), 'CommonTools/Server_Client'))
    addons_path.append(os.path.join(os.path.dirname(path), 'CommonTools/Server_Client/client_functions'))
    addons_path.append(os.path.join(os.path.dirname(path), 'CommonTools/SQLControl'))
    addons_path.append(os.path.join(os.path.dirname(path), 'CommonTools/SQLControl/sql_data_transform.py'))
    addons_path.append(os.path.join(os.path.dirname(path), 'CommonTools/UserMCommonTools'))
    addons_path.append(os.path.join(os.path.dirname(path), 'CommonTools/UserMCommonTools/Permissions.py'))
    addons_path.append(os.path.join(os.path.dirname(path), 'CommonTools/UserMCommonTools/UsersLogin.py'))
    addons_path.append(os.path.join(os.path.dirname(path), 'CommonTools/UserMCommonTools/UsersManage.py'))
    addons_path.append(os.path.join(os.path.dirname(path), 'CommonTools/UserMCommonTools/UsersSessionManage.py'))
    # addons_path = os.path.join(os.path.dirname(path), 'CommonTools/UserMCommonTools/UsersManage.py')
    # addons_path = os.path.join(os.path.dirname(path), 'CommonTools/UserMCommonTools/UsersManage.py')
    # addons_path = os.path.join(os.path.dirname(path), 'CommonTools/UserMCommonTools/UsersManage.py')

    # 将自建模块所在的目录添加到系统路径中
    for item in addons_path:
        sys.path.append(item)
        
# try:
#     import Server_Client.client_functions as clientf
# except:
#     clientf = None
