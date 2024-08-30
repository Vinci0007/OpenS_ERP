import importlib.util

def get_inBoundManage():
    if importlib.util.find_spec('Addons.WareHouse.InBoundManage') is not None:
        return importlib.import_module('Addons.WareHouse.InBoundManage')
    return None

def get_warehouseManage():
    if importlib.util.find_spec('Addons.WareHouse.WarehouseManage') is not None:
        return importlib.import_module('Addons.WareHouse.WarehouseManage')
    return None


#########   main Functions  ##########

# baseAddons_module = 'Addons.AaseAddons'
# if importlib.util.find_spec(baseAddons_module) is not None:
#     baseAddons = importlib.import_module(baseAddons_module)
#     # InBoundManage = getattr(module, 'InBoundManage', None)
#     # from Addons.WareHouse import InBoundManage
# else:
#     baseAddons = None  # 返回一个状态值

# from . import baseAddons

# userManage_module = '.UserManage'
# if importlib.util.find_spec(userManage_module) is not None:
#     userManage = importlib.import_module(userManage_module)
#     # InBoundManage = getattr(module, 'InBoundManage', None)
#     # from Addons.WareHouse import InBoundManage
# else:
#     userManage = None  # 返回一个状态值
    
# wareHouse_module = '.WareHouse'
# if importlib.util.find_spec(wareHouse_module) is not None:
#     wareHouse = importlib.import_module(wareHouse_module)
#     # InBoundManage = getattr(module, 'InBoundManage', None)
#     # from Addons.WareHouse import InBoundManage
# else:
#     wareHouse = None  
    
# techManage_module = '.TechManage'
# if importlib.util.find_spec(techManage_module) is not None:
#     techManage = importlib.import_module(techManage_module)
#     # InBoundManage = getattr(module, 'InBoundManage', None)
#     # from Addons.WareHouse import InBoundManage
# else:
#     techManage = None  
    
# systemManage_module = '.SystemManage'
# if importlib.util.find_spec(systemManage_module) is not None:
#     systemManage = importlib.import_module(systemManage_module)
#     # InBoundManage = getattr(module, 'InBoundManage', None)
#     # from Addons.WareHouse import InBoundManage
# else:
#     systemManage = None  
    
# saleManage_module = '.SaleManage'
# if importlib.util.find_spec(saleManage_module) is not None:
#     saleManage = importlib.import_module(saleManage_module)
#     # InBoundManage = getattr(module, 'InBoundManage', None)
#     # from Addons.WareHouse import InBoundManage
# else:
#     saleManage = None  
    
# purchManage_module = '.PurchManage'
# if importlib.util.find_spec(purchManage_module) is not None:
#     purchManage = importlib.import_module(purchManage_module)
#     # InBoundManage = getattr(module, 'InBoundManage', None)
#     # from Addons.WareHouse import InBoundManage
# else:
#     purchManage = None  
    
# produceManade_module = '.ProduceManade'
# if importlib.util.find_spec(produceManade_module) is not None:
#     produceManade = importlib.import_module(produceManade_module)
#     # InBoundManage = getattr(module, 'InBoundManage', None)
#     # from Addons.WareHouse import InBoundManage
# else:
#     produceManade = None  
    
# humanSource_module = '.HumanSource'
# if importlib.util.find_spec(humanSource_module) is not None:
#     humanSource = importlib.import_module(humanSource_module)
#     # InBoundManage = getattr(module, 'InBoundManage', None)
#     # from Addons.WareHouse import InBoundManage
# else:
#     humanSource = None  
    
# workFlow_module = '.WorkFlow'
# if importlib.util.find_spec(workFlow_module) is not None:
#     workFlow = importlib.import_module(workFlow_module)
#     # InBoundManage = getattr(module, 'InBoundManage', None)
#     # from Addons.WareHouse import InBoundManage
# else:
#     workFlow = None  



##############################################
##############################################
# homepage #######
##############################################
##############################################


##############################################
##############################################
# warehouse #######
##############################################
##############################################


# from Addons.WareHouse import InBoundManage as ibma
# warehouse_inbound_module = '.WareHouse.InBoundManage'
# if importlib.util.find_spec(warehouse_inbound_module) is not None:
#     inBoundManage = importlib.import_module(warehouse_inbound_module)
#     # InBoundManage = getattr(module, 'InBoundManage', None)
#     # from Addons.WareHouse import InBoundManage
# else:
#     inBoundManage = None  # 返回一个状态值
    
# warehouse_module = '.WareHouse'
# if importlib.util.find_spec(warehouse_module) is not None:
#     warehouse_manage_module = 'WareHouse.WarehouseManage'
#     wareHouse = importlib.import_module(warehouse_module)
#     warehouseManage = importlib.import_module(warehouse_manage_module)
#     # WarehouseManage = getattr(module, 'warehouse_module', None)
# else:
#     wareHouse = None
#     warehouseManage = None  # 返回一个状态值