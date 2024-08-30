# from Addons.ToolsCommon.FuncQR import ScanProductQR as scanQR
# from Addons.ToolsCommon.FuncQR import CreateProductQR as createQR
# from Addons.BaseAddons.server_sql import server_data_format as sdf
# from Addons.WareHouse.Tools import WarehouseDataCacheManage as whcache
from Addons.WareHouse.Tools import WarehouseServerData as whserv
from Addons.BaseAddons.UserPermissionManage import WareHousePermission as whPer
from Addons.ToolsCommon.FilesOperate import FilesOperator as fileso
from Addons.ToolsCommon.Office_tools import BomExcleDataRead as bomexcledr

from PyQt6.QtWidgets import QMessageBox, QLabel, QWidget, QVBoxLayout, QTabWidget, QHBoxLayout, QPushButton
from PyQt6.QtWidgets import QTableView, QLineEdit, QHeaderView, QComboBox
from PyQt6.QtCore import Qt, QSortFilterProxyModel
from PyQt6.QtGui import QStandardItemModel, QStandardItem

import time, threading

class FilterHeader(QHeaderView):
    def __init__(self, orientation, parent=None):
        super().__init__(orientation, parent)
        self.comboBoxes = []

    def showEvent(self, event):
        model = self.parent().model().sourceModel()  # 获取表格原始模型
        while self.comboBoxes:
            combo = self.comboBoxes.pop()
            combo.deleteLater()

        for i in range(model.columnCount()):
            combo = QComboBox(self)
            unique_values = set()
            for j in range(model.rowCount()):
                unique_values.add(model.item(j, i).text())
            combo.addItem("")  # 默认为空，不进行筛选
            combo.addItems(sorted(unique_values))
            combo.currentIndexChanged.connect(self.parent().filterChanged)  # 筛选发生变化时更新视图
            self.comboBoxes.append(combo)

    def sizeHint(self):
        size = super().sizeHint()
        size.setHeight(max(30, size.height()))
        return size

    def setGeometry(self, rect):
        super().setGeometry(rect)
        x = rect.x()
        for combo in self.comboBoxes:
            combo_width = rect.width() // len(self.comboBoxes)
            combo.setGeometry(x, 0, combo_width, rect.height())  # 更新下拉列表的位置和大小
            x += combo_width

class FilterProxyModel(QSortFilterProxyModel):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.filterConditions = {}

    def setFilter(self, columnIndex, filterText):
        self.filterConditions[columnIndex] = filterText
        self.invalidateFilter()

    def filterAcceptsRow(self, sourceRow, sourceParent):
        for column, text in self.filterConditions.items():
            if text:
                index = self.sourceModel().index(sourceRow, column, sourceParent)
                if text not in self.sourceModel().data(index):
                    return False
        return True

def on_wh_inventory_clicked(mainWin, right_toolbar):         # funcPosition_label,
    funcPosition_label = right_toolbar.findChild(QLabel, 'funcPosition_label')
    funcPosition_label.setText(' 功能 -> 仓库管理 -> 库存信息')
    create_whInventoryUI(mainWin, funcPosition_label)

def create_whInventoryUI(mainWin, right_toolbar):   
    # all_warehouse_data = whcache.swStart_DbCacheInit()
    # all_warehouse_data = whserv.showAll_WarehouseData()
    
    inventoryTabWidget = QTabWidget()
    inventoryTabWidget.setObjectName("wh_inboundTabWidget")
    mainWin.setCentralWidget(inventoryTabWidget)
    
    showAllinfos_tab = QWidget()
    showAllinfos_tab.setObjectName("showAllinfos_tab")
    inventoryTabWidget.addTab(showAllinfos_tab, 'showAllinfos_tab')
    inventoryTabWidget.setTabText(0, "库存总览")  
    
    exsitBound_tab = QWidget()
    exsitBound_tab.setObjectName('exsitBound_tab')
    inventoryTabWidget.addTab(exsitBound_tab, 'exsitBound_tab')
    inventoryTabWidget.setTabText(1, "未出库库存")
    
    # ###   tools
    # tools_addBtn = QPushButton("新增")
    # tools_addBtn.setObjectName("mann_auto_add")
    # tools_submitBtn = QPushButton("提交")
    # tools_submitBtn.setObjectName("submit_addBtn")
    # tools_ClearBtn = QPushButton("清空")
    # tools_ClearBtn.setObjectName("submit_addBtn")
    
    
    ############################################################
    #########           库存总览    #########################
    ############################################################
    # whInventoryTableRowNum = len(all_warehouse_data)
    dataHeadersName = [
        # 'id'  数据库id不显示
        'product_id',
        'product_name',
        'product_type',
        'supplier',
        'destination',
        'isoutbound',
        'inbound_time',
        'outbound_time',
        'receive_time',
        'price',
        'price_unit',
        'quality',
        'quality_unit',
        'operator',
        # 'productCheckID'  生成的checkid不显示
        ]
    dataHeadersName_ZH = ['物料号','物料名称','物料类型','供应商/来源', '去处','是否出库', '入库时间',
                          '出库时间','接收时间','价格','价格单位','数量','数量单位','操作者']
    
    showAllinfos_tab_Layout = QVBoxLayout()
    #### tools
    showAllinfos_tab_ToolsLayout = QHBoxLayout()
    showAllinfos_tab_Layout.addLayout(showAllinfos_tab_ToolsLayout)
    
    inventoryReflash_btn = QPushButton()
    inventoryReflash_btn.setText('刷新库存')
    inventoryReflash_btn.setStyleSheet("font-size: 15px;")
    showAllinfos_tab_ToolsLayout.addWidget(inventoryReflash_btn)
      
    turnToExistBoundTab_btn = QPushButton()
    turnToExistBoundTab_btn.setText('未出库库存')
    turnToExistBoundTab_btn.setStyleSheet("font-size: 15px;")
    showAllinfos_tab_ToolsLayout.addWidget(turnToExistBoundTab_btn)
    showAllinfos_tab_ToolsLayout.addStretch()
    
    #### tools
    showAllinfos_tabView = QTableView()
    showAllinfos_tab_Layout.addWidget(showAllinfos_tabView)
    showAllinfos_tab.setLayout(showAllinfos_tab_Layout) 
    whInventoryTableModel = QStandardItemModel(0, 14) 
    # showAllinfos_tabView.setModel(whInventoryTableModel)
    whInventoryTableModel.setHorizontalHeaderLabels(dataHeadersName_ZH)
    ########    table setting --- 筛选
    proxy_model = FilterProxyModel()
    proxy_model.setSourceModel(whInventoryTableModel)
    showAllinfos_tabView.setModel(proxy_model)
    filterHeader = FilterHeader(Qt.Orientation.Horizontal, showAllinfos_tabView)  # 自定义列头
    showAllinfos_tabView.setHorizontalHeader(filterHeader)
    def filterChanged():
        for i, combo in enumerate(filterHeader.comboBoxes):
            proxy_model.setFilter(i, combo.currentText())
    showAllinfos_tabView.filterChanged = filterChanged
    
    turnToExistBoundTab_btn.clicked.connect(lambda: inventoryDataShow(whInventoryTableModel, dataHeadersName, mainWin))
    turnToExistBoundTab_btn.clicked.connect(lambda: inventoryTabWidget.setCurrentIndex(1))
        

    ############################################################
    #########           未出库库存    #########################
    ############################################################
    # whInventoryTableRowNum = len(all_warehouse_data)
    exsitBound_tab_dataHeadersName = [
        'product_id',
        'product_name',
        'product_type',
        'supplier',
        'isoutbound',
        'inbound_time',
        'outbound_time',
        'receive_time',
        'quality',
        'quality_unit',
        'operator',
        ]
    exsitBound_tab_dataHeadersName_ZH = ['物料号','物料名称','物料类型','供应商/来源', '是否出库', '入库时间',
                          '出库时间','接收时间','数量','数量单位','操作者']
    
    exsitBound_tab_Layout = QVBoxLayout()
    #### tools
    exsitBound_tab_ToolsLayout = QHBoxLayout()
    exsitBound_tab_Layout.addLayout(exsitBound_tab_ToolsLayout)
    
    exsitBoundReflash_btn = QPushButton()
    exsitBoundReflash_btn.setText('刷新库存')
    exsitBoundReflash_btn.setStyleSheet("font-size: 15px;")
    exsitBound_tab_ToolsLayout.addWidget(exsitBoundReflash_btn)
    
    bomCheckBtn = QPushButton()
    exsitBound_tab_ToolsLayout.addWidget(bomCheckBtn)
    bomCheckBtn.setText('BOM 库存检查')
    bomCheckBtn.setStyleSheet("font-size: 15px;")
    exsitBound_tab_ToolsLayout.addStretch()
      
    #### tools
    exsitBound_tabView = QTableView()
    exsitBound_tab_Layout.addWidget(exsitBound_tabView)
    exsitBound_tab.setLayout(exsitBound_tab_Layout) 
    whExsitBoundTableModel = QStandardItemModel(0, 11) 
    exsitBound_tabView.setModel(whExsitBoundTableModel)
    
    whExsitBoundTableModel.setHorizontalHeaderLabels(exsitBound_tab_dataHeadersName_ZH)
    
    bomCheckBtn.clicked.connect(lambda: on_bomCheckBtn_clicked(exsitBound_tab_ToolsLayout, bomCheckBtn))
    exsitBoundReflash_btn.clicked.connect(lambda: existBoundDataShow(whExsitBoundTableModel, exsitBound_tab_dataHeadersName))
    
    
    ############################################################
    #########           库存数据展示    #########################
    ############################################################
    # inventoryDataShow(whInventoryTableModel, dataHeadersName, mainWin)
    # existBoundDataShow(whExsitBoundTableModel, exsitBound_tab_dataHeadersName) 
    threads = []
    thread = threading.Thread(target=dataShowControl, args=(inventoryTabWidget,whInventoryTableModel, dataHeadersName,
                                                            whExsitBoundTableModel, exsitBound_tab_dataHeadersName, 
                                                            mainWin))
    thread.start()
    threads.append(thread)
    for thread in threads:
        if not thread.is_alive():
            threads.remove(thread)
            break
  
############################################################
#########           库存数据获取与刷新    ###################
############################################################
 
def dataShowControl(inventoryTabWidget, whInventoryTableModel, dataHeadersName, 
                    whExsitBoundTableModel, exsitBound_tab_dataHeadersName, 
                    mainWin):
    while True:
        inventoryDataShow(whInventoryTableModel, dataHeadersName, mainWin)
        existBoundDataShow(whExsitBoundTableModel, exsitBound_tab_dataHeadersName)
        time.sleep(3600) 
 
def inventoryDataShow(whInventoryTableModel, dataHeadersName, mainWin):
    all_warehouse_data = whserv.showAll_WarehouseData()
    warehouse_data = []
    if (all_warehouse_data is not None) and (all_warehouse_data != False):
        clearInventoryAllTableRows(whInventoryTableModel)   #  or all_warehouse_data:
        for jsonkey, warehousevalue in all_warehouse_data.items():
            warehouse_data.append(warehousevalue)       # list [{id: 'sdads'}, {id: 'sdads'}, {id: 'sdads'}]
    else:
        return        
    for item in warehouse_data:
        index = whInventoryTableModel.rowCount()
        row = []
        for num in range(len(dataHeadersName)):
            if dataHeadersName[num] == 'price':               
                if not whPer.isPermissionPrice_show(mainWin.userinfo['permissions_info']):
                # if True:
                    item[dataHeadersName[num]] = '无权限' 
                if dataHeadersName[num] == 'operator':               
                        item[dataHeadersName[num]] = '无权限' 
            standItem = QStandardItem(str(item[dataHeadersName[num]]))
            standItem.setEditable(False)
            standItem.setTextAlignment(Qt.AlignmentFlag.AlignCenter)
            row.append(standItem)
        whInventoryTableModel.appendRow(row) 
    return warehouse_data
def existBoundDataShow(whExsitBoundTableModel, exsitBound_tab_dataHeadersName):
    all_warehouse_data = whserv.showAll_WarehouseData()
    warehouse_data = []
    if (all_warehouse_data is not None) and (all_warehouse_data != False):
        clearInventoryAllTableRows(whExsitBoundTableModel)#  or all_warehouse_data:
        for jsonkey, warehousevalue in all_warehouse_data.items():
            warehouse_data.append(warehousevalue)       # list [{id: 'sdads'}, {id: 'sdads'}, {id: 'sdads'}]
    else:
        return 
    for item in warehouse_data:
        index = whExsitBoundTableModel.rowCount()
        row = []
        if item['isoutbound'] == '已出库' or item['isoutbound'] == '1':
            pass
        else:
            for num in range(len(exsitBound_tab_dataHeadersName)):
                standItem = QStandardItem(str(item[exsitBound_tab_dataHeadersName[num]]))
                standItem.setEditable(False)
                standItem.setTextAlignment(Qt.AlignmentFlag.AlignCenter)
                row.append(standItem)
            whExsitBoundTableModel.appendRow(row)
    return warehouse_data
def clearInventoryAllTableRows(toClearTableModelName):
    while toClearTableModelName.rowCount() > 0:
                    toClearTableModelName.removeRow(0)    
    
    
    
    
   
   
############################################################
#########           bom 按钮控制    ###################
############################################################   
def on_bomCheckBtn_clicked(exsitBound_tab_ToolsLayout, bomCheckBtn):
    upLoadBomFile_Btn = QPushButton()
    upLoadBomFile_Btn.setText('上传BOM文件(excle)')
    upLoadBomFile_Btn.setObjectName('upLoadBomFile_Btn')
    upLoadBomFile_Btn.setStyleSheet("font-size: 15px;")
    if not exsitBound_tab_ToolsLayout.findChild(QPushButton, 'upLoadBomFile_Btn'):      ##判断按钮是否存在有问题
        exsitBound_tab_ToolsLayout.addWidget(upLoadBomFile_Btn)
        
    startCheckBomFile_Btn = QPushButton()
    startCheckBomFile_Btn.setText('开始BOM检查')
    startCheckBomFile_Btn.setObjectName('startCheckBomFile_Btn')
    startCheckBomFile_Btn.setStyleSheet("font-size: 15px;")
    if not exsitBound_tab_ToolsLayout.findChild(QPushButton, 'startCheckBomFile_Btn'):
        exsitBound_tab_ToolsLayout.addWidget(startCheckBomFile_Btn)
        
    upLoadBomFile_Btn.clicked.connect(lambda: fileso.UpLoadFile())
    # bomFilePath = upLoadBomFile_Btn.clicked.connect(lambda: fileso.UpLoadFile() : fileso.sendFilePathTo())
    startCheckBomFile_Btn.clicked.connect(lambda: bomexcledr.bomDataRead_FromExcle(fileso.sendFilePathTo()))
    try:
        bomCheckBtn.clicked.disconnect()
    except:
        pass
    bomCheckBtn.clicked.connect(lambda: on_bomCheckBtn_DeleteBtn_clicked(exsitBound_tab_ToolsLayout, upLoadBomFile_Btn, startCheckBomFile_Btn, bomCheckBtn))
    
def on_bomCheckBtn_DeleteBtn_clicked(exsitBound_tab_ToolsLayout, upLoadBomFile_Btn, startCheckBomFile_Btn, bomCheckBtn):
    exsitBound_tab_ToolsLayout.removeWidget(upLoadBomFile_Btn)
    exsitBound_tab_ToolsLayout.removeWidget(startCheckBomFile_Btn)
    upLoadBomFile_Btn.deleteLater()
    startCheckBomFile_Btn.deleteLater()
    try:
        bomCheckBtn.clicked.disconnect()
    except:
        pass
    bomCheckBtn.clicked.connect(lambda: on_bomCheckBtn_clicked(exsitBound_tab_ToolsLayout, bomCheckBtn))