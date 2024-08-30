from Addons.ToolsCommon.FuncQR import ScanProductQR as scanQR
from Addons.ToolsCommon.FuncQR import CreateProductQR as createQR
from Addons.ToolsCommon.Threadings import ThreadsControl as threadc
from Addons.BaseAddons.server_sql import server_data_format as sdfs
from Addons.WareHouse.Tools import WarehouseServerData as whserv

from PyQt6.QtWidgets import QMessageBox, QLabel, QWidget, QVBoxLayout, QTabWidget, QHBoxLayout, QPushButton
from PyQt6.QtWidgets import QTableView, QLineEdit, QStyledItemDelegate, QComboBox, QCheckBox, QHeaderView
from PyQt6.QtCore import Qt
from PyQt6.QtGui import QStandardItemModel, QStandardItem, QColor, QImage, QPixmap, QIcon

import threading, time

class outboundBtnDelegate(QStyledItemDelegate):
    def __init__(self, parent, model):
        super(outboundBtnDelegate, self).__init__(parent)
        self.model = model
    
    def paint(self, painter, option, index):
        super(outboundBtnDelegate, self).paint(painter, option, index)
        # 绘制一个按钮
        if not self.parent().indexWidget(index):  # 假设按钮在第3列
            painter.fillRect(option.rect, Qt.GlobalColor.gray)  # 自定义按钮颜色
            painter.drawText(option.rect, Qt.AlignmentFlag.AlignCenter, "确认出库")
            # image_path = "Resource/Icon/delete001.png"
            # image = QImage(image_path)
            # image = image.scaled(14, 14)  
            # painter.drawImage(option.rect.x() + 43, option.rect.y() + 7, image)

    def editorEvent(self, event, model, option, index):
        # 处理点击事件，仅当点击第14列时响应
        if event.type() == event.Type.MouseButtonPress and index.column() == 13:
            if event.button() == Qt.MouseButton.LeftButton:
                # print(f"Row {index.row()} 的删除按钮被点击")
                model.removeRow(index.row())
                return True
        return super(outboundBtnDelegate, self).editorEvent(event, model, option, index)
# 注意: 你需要将你的项视图（如 QTableView）传给委托的构造函数。



# inbound_manage(SQLDataManage.users_load()[0], [SQLDataManage.users_load()[1]])
def on_wh_outbound_clicked(widget, right_toolbar):         # funcPosition_label,
    funcPosition_label = right_toolbar.findChild(QLabel, 'funcPosition_label')
    funcPosition_label.setText(' 功能 -> 仓库管理 -> 出库管理')
    
    createFeatureWidget(widget, funcPosition_label)
    
    
    pass

def createFeatureWidget(widget, right_toolbar):   
    centralwidget = QWidget()
    feature_layout = QHBoxLayout()
    centralwidget.setLayout(feature_layout)
    widget.setCentralWidget(centralwidget)  
    
    outboundTabWidget = QTabWidget()
    outboundTabWidget.setObjectName("wh_inboundTabWidget")
    
    pdcinfos_tab = QWidget()
    pdcinfos_tab.setObjectName("pdcinfos")
    outboundTabWidget.addTab(pdcinfos_tab, 'pdcinfos_tab')
    outboundTabWidget.setTabText(0, "操作记录")
    feature_layout.addWidget(outboundTabWidget)
    
    multiOutbound_tab = QWidget()
    multiOutbound_tab.setObjectName("product_inbound")
    outboundTabWidget.addTab(multiOutbound_tab, 'pdcInbound_tab')
    outboundTabWidget.setTabText(1, "批量出库")
    feature_layout.addWidget(outboundTabWidget)
    
    
    ############################################################
    #########           批量出库    #########################
    ############################################################
    # whData = threadc.outboundGetDataThreads()
    whData = threadc.threadsControl(updateWhDataFromServer_Cycle, 'warehouse_data')
    print(whData)

    
    
    multiOutbound_layout = QVBoxLayout()
    multiOutbound_tab.setLayout(multiOutbound_layout)
    
    toolsLayout = QHBoxLayout()
    addBtn = QPushButton()
    
    chooseProductCombox = QComboBox()
    
    toolsLayout.addWidget(addBtn)
    toolsLayout.addStretch()
    multiOutbound_layout.addLayout(toolsLayout)
    
    
    
    
    #############  tableviews 
    dataHeadersName = ['product_id','product_name','product_type','supplier', 'isoutbound',
                        'inbound_time','outbound_time','receive_time','price','price_unit','quality',
                        'quality_unit','operator']# 'productCheckID'  生成的checkid不显示# 'id'  数据库id不显示
    dataHeadersName_ZH = ['?', '物料号','物料名称','物料类型','供应商/来源', '是否出库', '入库时间', 
                        '出库时间','接收时间','单价','价格单位','数量','数量单位','操作者','((数据操作))']
    
    multiOutboundTableView = QTableView()
    multiOutboundTableView.setObjectName('multiOutboundTableView')
    multiOutboundTableView.horizontalHeader().setSectionResizeMode(QHeaderView.ResizeMode.ResizeToContents)
    mannu_multiOutboundTableModel = QStandardItemModel(0, 15) 
    mannu_multiOutboundTableModel.setHorizontalHeaderLabels(dataHeadersName_ZH)
    multiOutbound_layout.addWidget(multiOutboundTableView)
    multiOutboundTableView.setModel(mannu_multiOutboundTableModel)
    
    addBtn.clicked.connect(lambda: on_addBtn_clicked(multiOutbound_layout, mannu_multiOutboundTableModel))
    multiOutbound_layout.addStretch()


def tableDataShow_All():
    pass

def on_addBtn_clicked(multiOutbound_layout, mannu_multiOutboundTableModel):    
    row = []
    # for num in range(14):
    #     standItem = QStandardItem('')
    #     if num == 0:
    #         pass
    #         # standItem.setEditable(False)
    #     row.append(standItem)
    for j in range(5):
        item = QStandardItem('')
        if j == 0:
            checkbox = QCheckBox()
            item.setCheckable(True)
        item.setTextAlignment    
        # item.setCheckBox(checkbox)
        row.append(item)
        # mannu_multiOutboundTableModel.setItem(i, j, item)
    mannu_multiOutboundTableModel.appendRow(row)
    # mannu_multiOutboundTableModel.submit() 
    
def updateWhDataFromServer_Cycle(toClearTableModelName):
    while True:
        clearAllTableRows(toClearTableModelName)
        warehouse_data = getWhDataFromServer()
        tableDataShow_All(warehouse_data)
        time.sleep(3600)
        

def clearAllTableRows(toClearTableModelName):
    while toClearTableModelName.rowCount() > 0:
                    toClearTableModelName.removeRow(0)            
    
def getWhDataFromServer():
    all_warehouse_data = whserv.showAll_WarehouseData()
    warehouse_data = []
    if (all_warehouse_data is not None) and (all_warehouse_data != False):
        for jsonkey, warehousevalue in all_warehouse_data.items():
            warehouse_data.append(warehousevalue)       # list [{id: 'sdads'}, {id: 'sdads'}, {id: 'sdads'}]
            return warehouse_data
    else:
        return None
    
    
    
# def on_addBtn_cliecked(multiOutbound_layout):
#     mannu_multiOutboundLayout = QHBoxLayout()
#     multiOutbound_layout.addLayout(mannu_multiOutboundLayout)
#     selectBtn = QPushButton()
#     mannu_multiOutboundLayout.addWidget(selectBtn)
#     mannu_multiOutboundTableView = QTableView()
#     mannu_multiOutboundTableView.horizontalHeader().setVisible(False)
#     mannu_multiOutboundLayout.addWidget(mannu_multiOutboundTableView)
#     mannu_multiOutboundTableModel = QStandardItemModel(0, 15) 
#     # mannu_multiOutboundTableModel.setHorizontalHeaderLabels(dataHeadersName_ZH)
#     # auto_multiOutboundTableModel = QStandardItemModel(0, 15) 
#     # # auto_multiOutboundTableModel.setHorizontalHeaderLabels(dataHeadersName_ZH)
    
#     mannu_multiOutboundTableView.setModel(mannu_multiOutboundTableModel)
    
#     row = []
#     for num in range(14):
#         standItem = QStandardItem('')
#         if num == 0:
#             pass
#             # standItem.setEditable(False)
#         row.append(standItem)
#     mannu_multiOutboundTableModel.appendRow(row)
#     mannu_multiOutboundTableModel.submit() 
    
    
    