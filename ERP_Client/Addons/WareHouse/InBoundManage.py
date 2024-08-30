
from Addons.ToolsCommon.FuncQR import ScanProductQR as scanQR
from Addons.ToolsCommon.FuncQR import CreateProductQR as createQR
from Addons.BaseAddons.server_sql import server_data_format as sdf
from Addons.ToolsCommon.FuncQR import QRClientConfig as qrcc
from Addons.WareHouse.Tools import WarehouseServerData as whserv
from Addons.WareHouse.Tools import WarehouseDataCacheManage as whcache

from PyQt6.QtWidgets import QMessageBox, QLabel, QWidget, QVBoxLayout, QTabWidget, QHBoxLayout, QPushButton
from PyQt6.QtWidgets import QTableView, QLineEdit, QComboBox, QStyledItemDelegate
from PyQt6.QtCore import Qt, QSize
from PyQt6.QtGui import QStandardItemModel, QStandardItem, QColor, QImage, QPixmap, QIcon

import random, datetime, hashlib, threading, json, base64
# from cryptography.fernet import Fernet
# sercretKey_cipherSuite = createQR.cipher_suite


class ButtonDelegate(QStyledItemDelegate):
    def __init__(self, parent, model):
        super(ButtonDelegate, self).__init__(parent)
        self.model = model
    
    def paint(self, painter, option, index):
        super(ButtonDelegate, self).paint(painter, option, index)
        # 绘制一个按钮
        if not self.parent().indexWidget(index):  # 假设按钮在第3列
            painter.fillRect(option.rect, Qt.GlobalColor.gray)  # 自定义按钮颜色
            # painter.drawText(option.rect, Qt.AlignmentFlag.AlignCenter, "删除此行")
            image_path = "Resource/Icon/delete001.png"
            image = QImage(image_path)
            image = image.scaled(14, 14)  
            painter.drawImage(option.rect.x() + 43, option.rect.y() + 7, image)

    def editorEvent(self, event, model, option, index):
        # 处理点击事件，仅当点击第14列时响应
        if event.type() == event.Type.MouseButtonPress and index.column() == 13:
            if event.button() == Qt.MouseButton.LeftButton:
                # print(f"Row {index.row()} 的删除按钮被点击")
                model.removeRow(index.row())
                return True
        return super(ButtonDelegate, self).editorEvent(event, model, option, index)
# 注意: 你需要将你的项视图（如 QTableView）传给委托的构造函数。


# inbound_manage(SQLDataManage.users_load()[0], [SQLDataManage.users_load()[1]])
def on_wh_inbound_clicked(widget, right_toolbar):         # funcPosition_label,
    funcPosition_label = right_toolbar.findChild(QLabel, 'funcPosition_label')
    funcPosition_label.setText(' 功能 -> 仓库管理 -> 入库管理')
    createFeatureWidget(widget, funcPosition_label)
    
    
    pass

def createFeatureWidget(widget, right_toolbar):
    isExistFuncScanQR = False
       
    inboundTabWidget = QTabWidget()
    inboundTabWidget.setObjectName("wh_inboundTabWidget")
    widget.setCentralWidget(inboundTabWidget)  
    inboundTabWidget.setStyleSheet("background-color: lightgray;")
    
    inboundLogs_tab = QWidget()
    inboundLogs_tab.setObjectName("inboundLogs_tab")
    inboundTabWidget.addTab(inboundLogs_tab, 'inboundLogs_tab')
    inboundTabWidget.setTabText(0, "操作记录")
    
    multiInbound_tab = QWidget()
    multiInbound_tab.setObjectName("multiInbound_tab")
    inboundTabWidget.addTab(multiInbound_tab, 'multiInbound_tab')
    inboundTabWidget.setTabText(1, "批量入库")

    singleInbound_tab = QWidget()
    singleInbound_tab.setObjectName("singleInbound_tab")
    inboundTabWidget.addTab(singleInbound_tab, 'singleInbound_tab')
    inboundTabWidget.setTabText(2, "单品入库")


    ############################################################
    #########           批量入库    #########################
    ############################################################
    multiInbound_layout = QVBoxLayout()
    multiInbound_tab.setLayout(multiInbound_layout)
    
    toolsLayout = QHBoxLayout()
    toolswidget = QWidget()
    toolswidget.setStyleSheet("background-color: rgb(185, 185, 185);")
    toolsLayout.addWidget(toolswidget)
    toolswidgetLayout = QHBoxLayout()
    toolswidget.setLayout(toolswidgetLayout)
    multiInbound_layout.addLayout(toolsLayout)
    
    ###   tools
    tools_addBtn = QPushButton("新增")
    tools_addBtn.setObjectName("mann_auto_add")
    tools_submitBtn = QPushButton("全部提交")
    tools_submitBtn.setObjectName("submit_addBtn")
    tools_ClearBtn = QPushButton("清空")
    tools_ClearBtn.setObjectName("submit_addBtn")
    
    mann_auto_SelectCombox = QComboBox()
    mann_auto_SelectCombox.setObjectName("mannualInbound_SelectCombox")
    mann_auto_SelectCombox.setStyleSheet("font-size: 16px;")
    mann_auto_SelectCombox.addItem("手动入库")  # index 0
    mann_auto_SelectCombox.addItem("扫码入库")  # index 1
    mann_auto_SelectCombox.model().item(1).setEnabled(False)
    mann_auto_SelectCombox.setCurrentIndex(0)

    toolswidgetLayout.addWidget(mann_auto_SelectCombox)
    toolswidgetLayout.addWidget(tools_addBtn)
    toolswidgetLayout.addWidget(tools_submitBtn)
    toolswidgetLayout.addWidget(tools_ClearBtn)
    toolswidgetLayout.addStretch()
    
    #############  tableviews 
    dataHeadersName = ['product_id','product_name','product_type','supplier', 'isoutbound',
                        'inbound_time','outbound_time','receive_time','price','price_unit','quality',
                        'quality_unit','operator']# 'productCheckID'  生成的checkid不显示# 'id'  数据库id不显示
    dataHeadersName_ZH = ['物料号','物料名称','物料类型','供应商/来源', '是否出库', '入库时间', 
                        '出库时间','接收时间','单价','价格单位','数量','数量单位','操作者','((数据操作))']
    
    multiInboundTableView = QTableView()
    multiInboundTableView.setObjectName('multiInbound_tableView')
    mann_multiInboundTableModel = QStandardItemModel(0, 14) 
    mann_multiInboundTableModel.setHorizontalHeaderLabels(dataHeadersName_ZH)
    auto_multiInboundTableModel = QStandardItemModel(0, 14) 
    auto_multiInboundTableModel.setHorizontalHeaderLabels(dataHeadersName_ZH)
    
    multiInboundTableView.horizontalHeader().setStyleSheet("background-color: gray;")
    deleteButtonDelegate = ButtonDelegate(multiInboundTableView, mann_multiInboundTableModel)
    multiInboundTableView.setItemDelegateForColumn(13, deleteButtonDelegate)
    multiInboundTableView.setModel(mann_multiInboundTableModel)
    multiInbound_layout.addWidget(multiInboundTableView)
    multiInbound_layout.addStretch()
    ###### 初始化绑定
    if mann_auto_SelectCombox.currentIndex() == 0:
        tools_addBtn.clicked.connect(lambda: on_mann_add_clicked(widget, mann_multiInboundTableModel))
        tools_ClearBtn.clicked.connect(lambda: clearAllTableRows(mann_multiInboundTableModel))
        tools_submitBtn.clicked.connect(lambda: on_submit_addBtn_clicked(widget, mann_multiInboundTableModel, dataHeadersName, dataHeadersName_ZH))
    elif mann_auto_SelectCombox.currentIndex() == 1:
        tools_addBtn.clicked.connect(lambda: on_auto_add_clicked(widget, auto_multiInboundTableModel))
        tools_ClearBtn.clicked.connect(lambda: clearAllTableRows(auto_multiInboundTableModel))
        tools_submitBtn.clicked.connect(lambda: on_submit_addBtn_clicked(widget, auto_multiInboundTableModel, dataHeadersName, dataHeadersName_ZH))
     
    widgetsInMultiInbound = {
        'multiInboundTableView':    multiInboundTableView,
        'mannuTableView':           'mannuTableView',
        'autoTableView':            'autoTableView',
        'mann_TableModel':          mann_multiInboundTableModel,
        'auto_TableModel':          auto_multiInboundTableModel,
        'multiInbound_layout':      multiInbound_layout,
        'mann_auto_SelectCombox':   mann_auto_SelectCombox,
        'toolswidgetLayout':        toolswidgetLayout,
        'tools_addBtn':             tools_addBtn,
        'tools_submitBtn':          tools_submitBtn,
        'tools_ClearBtn':           tools_ClearBtn,
        'dataHeadersName':          dataHeadersName,
        'dataHeadersName_ZH':       dataHeadersName_ZH   
    }
    
    if scanQR is not None:
        isExistFuncScanQR = True
        mann_auto_SelectCombox.model().item(1).setForeground(QColor(128, 128, 128))
        mann_auto_SelectCombox.model().item(1).setEnabled(True) 
    mann_auto_SelectCombox.currentIndexChanged.connect(lambda: on_mannAutoSelectCombox_Changed(widget, widgetsInMultiInbound))   

def on_mannAutoSelectCombox_Changed(widget, widgetsInMultiInbound):             
        if widgetsInMultiInbound['mann_auto_SelectCombox'].currentIndex() == 0:  
            if widgetsInMultiInbound['mann_TableModel'] is None or widgetsInMultiInbound['auto_TableModel'] is not None:       
                widgetsInMultiInbound['multiInboundTableView'].setModel(widgetsInMultiInbound['mann_TableModel'])
            ###  取消绑定
            try:
                widgetsInMultiInbound['tools_addBtn'].clicked.disconnect()
                widgetsInMultiInbound['tools_ClearBtn'].clicked.disconnect()
                widgetsInMultiInbound['tools_submitBtn'].clicked.disconnect()
            except:
                pass
            ####更新绑定
            widgetsInMultiInbound['tools_addBtn'].clicked.connect(lambda: on_mann_add_clicked(widget, widgetsInMultiInbound['mann_TableModel']))
            widgetsInMultiInbound['tools_ClearBtn'].clicked.connect(lambda: clearAllTableRows(widgetsInMultiInbound['mann_TableModel']))
            widgetsInMultiInbound['tools_submitBtn'].clicked.connect(lambda: on_submit_addBtn_clicked(widget, widgetsInMultiInbound['mann_TableModel'],
                                                                                                        widgetsInMultiInbound['dataHeadersName'],
                                                                                                        widgetsInMultiInbound['dataHeadersName_ZH']))   
        elif widgetsInMultiInbound['mann_auto_SelectCombox'].currentIndex() == 1: 
            if widgetsInMultiInbound['auto_TableModel'] is None or widgetsInMultiInbound['mann_TableModel'] is not None:       
                widgetsInMultiInbound['multiInboundTableView'].setModel(widgetsInMultiInbound['auto_TableModel'])
            try:
                widgetsInMultiInbound['tools_addBtn'].clicked.disconnect()
                widgetsInMultiInbound['tools_ClearBtn'].clicked.disconnect()
                widgetsInMultiInbound['tools_submitBtn'].clicked.disconnect()
            except:
                pass
            if qrcc.isExist_ser_ClientQR:
            # if True:
                widgetsInMultiInbound['tools_addBtn'].clicked.connect(lambda: on_auto_add_clicked(widgetsInMultiInbound['toolswidgetLayout'],
                                                                                                  widgetsInMultiInbound['auto_TableModel']))
                widgetsInMultiInbound['tools_ClearBtn'].clicked.connect(lambda: clearAllTableRows(widgetsInMultiInbound['auto_TableModel']))
                widgetsInMultiInbound['tools_submitBtn'].clicked.connect(lambda: on_submit_addBtn_clicked(widget, widgetsInMultiInbound['auto_TableModel'],
                                                                                                        widgetsInMultiInbound['dataHeadersName'],
                                                                                                        widgetsInMultiInbound['dataHeadersName_ZH'])) 
            else:
                QMessageBox.warning(None, "警告", "扫码功能错误或未安装 ！") 
#####手动部分                              
def on_mann_add_clicked(widget, tableModelName):
                # index = widgetsInMultiInbound['mann_TableModel'].rowCount()
                items = []
                for num in range(14):
                    standItem = QStandardItem('')
                    if num == 4:
                        standItem = QStandardItem('未出库')
                        standItem.setEditable(False)
                    if num == 5:
                        standItem.setEditable(False)
                    if num == 6:
                        standItem.setEditable(False)
                    if num == 8:
                        standItem = QStandardItem('无权限')
                        standItem.setEditable(False)
                    if num == 10:
                        standItem = QStandardItem('1')
                        standItem.setEditable(False)
                    if num == 12:
                        standItem = QStandardItem(widget.userinfo['name'])
                        standItem.setEditable(False)
                    if num == 13:
                        # standItem = QStandardItem('删除此行')
                        standItem.setEditable(False)
                    standItem.setTextAlignment(Qt.AlignmentFlag.AlignCenter)
                    # multiInboundTableModel.setItem(0, num, standItem)
                    items.append(standItem)
                tableModelName.appendRow(items)
                tableModelName.submit() 
#####  自动扫码部分                            
controlState = False
def on_scanQR_Control(tableModelName):
    global controlState
    controlState = True
    thread = threading.Thread(target=scanLoop, args=tableModelName)
    thread.start()
def on_cancel_scan():
    global controlState
    controlState = False
def scanLoop(widget, tableModelName):
    index = tableModelName.rowCount()
    items = []
    global controlState
    while controlState:
        scanData = scanQR.scan_barcode(controlState)
        if qrcc.isSecretInfo == 'True' and scanData is not None:     ## is sercret data ?
            decrypted_text = qrcc.dataSecretCipherSuite.decrypt(scanData)
            scanData = json.loads(decrypted_text.decode('utf-8'))
            # print("解密后的数据:", scanData) 
            if scanData is not None: 
                for num in range(14):
                    standItem = QStandardItem('')
                    data = {0:'product_id', 1:'product_name', 2:'product_type', 3:'supplier', 
                            6:'receive_time', 8:'price_unit', 10:'quality_unit'}
                    if num == 4:
                        standItem = QStandardItem('未出库')
                        standItem.setEditable(False)
                        pass
                    if num == 5:
                        standItem.setEditable(False)
                        pass
                    if num == 6:
                        standItem.setEditable(False)
                        pass
                    if num == 8:
                        standItem = QStandardItem('无权限')
                        standItem.setEditable(False)
                        pass
                    if num == 10:
                        standItem = QStandardItem('1')
                        standItem.setEditable(False)
                        pass
                    if num == 12:
                        standItem = QStandardItem(widget.userinfo['name'])
                        standItem.setEditable(False)
                        pass
                    if num == 13:
                        standItem = QStandardItem('删除此行')
                        standItem.setEditable(False)
                    standItem = QStandardItem(scanData[data[num]])
                    standItem.setTextAlignment(Qt.AlignmentFlag.AlignCenter)
                    # multiInboundTableModel.setItem(0, num, standItem)
                    items.append(standItem)
                tableModelName.appendRow(items)
                tableModelName.submit()
                
############  按钮功能区
def on_auto_add_clicked(toolsLayout, tableModelName):
    startScanQRbBtn = QPushButton()
    endScanQRbBtn = QPushButton()
    toolsLayout.addWidget(startScanQRbBtn)
    toolsLayout.addWidget(endScanQRbBtn)
    startScanQRbBtn.setText("开始扫码")
    endScanQRbBtn.setText("结束扫码")
    startScanQRbBtn.setObjectName("startScanQRbBtn")
    endScanQRbBtn.setObjectName("endScanQRbBtn")
    startBtnState = startScanQRbBtn.isDown()
    endBtnState = endScanQRbBtn.isDown()
    startScanQRbBtn.clicked.connect(lambda: on_scanQR_Control(tableModelName))
    endScanQRbBtn.clicked.connect(lambda: on_cancel_scan())
    # widgetsInMultiInbound['autoTableView'].horizontalHeader().setSectionsMovable(False)            
def on_mann_auto_add_clicked(mann_auto_Switch_btn):
    # mann_auto_Switch_btn.setText('扫码入库')
    # mann_auto_Switch_btn.setObjectName("autoInbound_btn")
    return mann_auto_Switch_btn

dataShowLogAll = []
dataShowLogAdd = []
saveLogState = False
def clearAllTableRows(toClearTableModelName):
    while toClearTableModelName.rowCount() > 0:
                    toClearTableModelName.removeRow(0)
def on_submit_addBtn_clicked(widget, tableModelName, tableHeader, tableHeader_zh):
        DataState, DataFromTable = getDataFromTable(tableModelName, tableHeader, tableHeader_zh)
        if not DataState or len(DataFromTable) <= 0:
            QMessageBox.warning(None, "警告", "数据不完整或无可供提交的数据")
            pass
        else:
            isNeedApprove = False
            saveToServerState = False
            inBoundTime = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            for row in range(tableModelName.rowCount()):
                for column in range(tableModelName.columnCount()):
                    if column == 5:
                        index = tableModelName.index(row, column)
                        standItem = QStandardItem(inBoundTime)
                        tableModelName.setItem(row, column, standItem)
            for row in range(len(DataFromTable)):
                DataFromTable[row]['inbound_time'] = inBoundTime 
            fillAllData = tableDataTransToSQLDataFormat(widget, DataFromTable)   
            if not isNeedApprove:
                if fillAllData is not None or fillAllData != []:
                    saveToServerState = whserv.saveWarehouseData(fillAllData, widget.login_session_token)
            else:
                #### 审批流程函数
                QMessageBox.warning(None, "警告", "请等待管理员审核")
                
            ####### show log needed data and save to local cache    
            if saveToServerState:
                QMessageBox.warning(None, "提示", "已提交至数据库")
                clearAllTableRows(tableModelName)
            saveLogState = whcache.updateInboundLog(fillAllData, widget.userinfo['user_check_id'])
            if not saveLogState:
                QMessageBox.warning(None, "警告", "Log保存错误, 尝试从服务器获取重新保存")
                serverData = whcache.updateLogFromServer(widget.userinfo['user_check_id'])
                QMessageBox.warning(None, "警告", "Log二次保存错误, 请检查本地配置文件")
                if serverData is None:
                    dataShowLogAll = getDataFromTable
                dataShowLogAll = serverData
            dataShowLogAdd = getDataFromTable  

def getDataFromTable(model, dataHeadersName, dataHeadersName_ZH):
    has_noEmpty_column = True
    header_name = []
    allTableData = []
    tableData = {}
    # 获取物料数据    
    edited_rows = set()
    for row in range(model.rowCount()):
        for column in range(model.columnCount()):
            header_name.append(model.headerData(column, Qt.Orientation.Horizontal))
            if column == 4 or column == 6 or column == 7 or column == 8 or column == 9 or column == 10:  # 跳过删除按钮
                pass
            index = model.index(row, column)
            if ((index.data(Qt.ItemDataRole.EditRole) != '' or index.data(Qt.ItemDataRole.EditRole) != None) and 
                (index.data(Qt.ItemDataRole.DisplayRole) != '' or index.data(Qt.ItemDataRole.DisplayRole) != None)): # and 
                # index.data(Qt.ItemDataRole.EditRole) != index.data(Qt.ItemDataRole.DisplayRole)
                pass
                # edited_rows.add(row)
            else:
                has_noEmpty_column = False
                break
        if has_noEmpty_column:
            edited_rows.add(row)
            row_data = []
            for col in range(model.columnCount()):
                coldata = model.index(row, col).data()
                row_data.append(coldata)     
            header_name_trans = {}
            header_name_trans.update({dataHeadersName_ZH[num]: dataHeadersName[num] for num in range(len(dataHeadersName_ZH)-1)})
            for num in range(len(row_data)):  # 去掉最后删除操作那列值
                header_name[num]
                if header_name[num] == '((数据操作))':
                    pass
                else:
                    tableData.update({header_name_trans[header_name[num]]: row_data[num]})
        allTableData.append(tableData)

    return [has_noEmpty_column, allTableData]

def tableDataTransToSQLDataFormat(widget, tableData):
    allFilledData = {}
    fillDataToSave = {
        'product_id': '',
        'product_name': '',
        'product_type': '',
        'supplier': '',
        'isoutbound': '',
        'inbound_time': '',
        'outbound_time': '',
        'receive_time': '',
        'price': '',
        'price_unit': '',
        'quality': '',
        'quality_unit': '',
        'operator': '',
        'productCheckID': ''
    }
    def createProductCheckId(product_id, product_name, supplier, inbound_time, operator, isoutbound):
        randomNum  = str(random.randint(1, 99999)).zfill(5)
        inbound_time_str = str(''.join(e for e in inbound_time if e.isalnum()))
        product_name_str = ''
        supplier_str = ''
        # outbound_time_str = str(outbound_time)
        for char in product_name:
            product_name_str = str(ord(char)) + product_name_str
        for char in supplier:
            supplier_str = str(ord(char)) + supplier_str
        if isoutbound == '未出库':
            isoutbound_str = '000'.zfill(3)
        else:
            isoutbound_str = '001'.zfill(3)
        initId = product_id + product_name_str + supplier_str + inbound_time_str + operator + randomNum + isoutbound_str
        initId_HASH = hashlib.sha256(initId.encode()).digest()
        productCheckId = base64.b32encode(initId_HASH).decode('utf-8')
        return productCheckId
    for row in range(len(tableData)):
        fillDataToSave['product_id'] = tableData[row]['product_id']
        fillDataToSave['product_name'] = tableData[row]['product_name']
        fillDataToSave['product_type'] = tableData[row]['product_type']
        fillDataToSave['supplier'] = tableData[row]['supplier']
        fillDataToSave['inbound_time'] = tableData[row]['inbound_time']
        fillDataToSave['outbound_time'] = tableData[row]['outbound_time']
        fillDataToSave['outbound_time'] = tableData[row]['outbound_time']
        fillDataToSave['receive_time'] = tableData[row]['receive_time']
        fillDataToSave['price'] = tableData[row]['price']
        fillDataToSave['price_unit'] = tableData[row]['price_unit']
        fillDataToSave['quality'] = tableData[row]['quality']
        fillDataToSave['quality_unit'] = tableData[row]['quality_unit']
        fillDataToSave['operator'] = widget.userinfo['user_check_id']
        fillDataToSave['productCheckID'] = createProductCheckId(tableData[row]['product_id'], tableData[row]['product_name'],
                                                                tableData[row]['supplier'], tableData[row]['inbound_time'],
                                                                widget.userinfo['user_check_id'], tableData[row]['isoutbound'])
        allFilledData.update({row: fillDataToSave})
    return allFilledData
    
        
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    ### 切换自动手动时，没有清空已有的  tableview
    
    # header_name_trans = {
                #     '物料号': 'product_id',
                #     '物料名称': 'product_name',
                #     '物料类型': 'product_type',
                #     '供应商/来源': 'supplier',
                #     '入库时间': 'inbound_time',
                #     '出库时间': 'outbound_time',
                #     '接收时间': 'receive_time',
                #     '单价': 'price',
                #     '价格单位': 'price_unit',
                #     '数量': 'quality',
                #     '数量单位': 'quality_unit',
                #     '操作者': 'operator',                 
                # }