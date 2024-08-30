
from Addons.WorkFlow import WorkFlowClass as WFclass

from PyQt6.QtWidgets import QLabel, QLineEdit, QCheckBox, QComboBox, QPushButton
from PyQt6.QtWidgets import QSpinBox, QDoubleSpinBox, QTextEdit, QMessageBox, QFileDialog
from PyQt6.QtWidgets import QTableWidget, QTableWidgetItem, QHeaderView, QAbstractItemView
from PyQt6.QtWidgets import QFormLayout, QVBoxLayout, QHBoxLayout, QGroupBox, QStackedWidget
from PyQt6.QtWidgets import QStackedLayout, QFrame, QGridLayout, QDialog, QDialogButtonBox
from PyQt6.QtWidgets import QMenu, QInputDialog, QProgressDialog, QStyle, QStyleOption
from PyQt6.QtWidgets import QStylePainter, QStyleHintReturn, QStyleOptionButton, QStyleOptionComboBox 
from PyQt6.QtWidgets import QStyleOptionComplex, QStyleOptionDockWidget, QStyleOptionFocusRect
from PyQt6.QtWidgets import QStyleOptionFrame, QStyleOptionGraphicsItem, QStyleOptionGroupBox
from PyQt6.QtWidgets import QStyleOptionHeader, QStyleOptionMenuItem, QStyleOptionProgressBar
from PyQt6.QtWidgets import QStyleOptionRubberBand, QStyleOptionSizeGrip, QStyleOptionSlider
from PyQt6.QtWidgets import QStyleOptionSpinBox, QStyleOptionTabBarBase, QWidget


# class ApprovalProcess:
#     def __init__(self):
#         self.states = ['submit', 'save2draft', 'reject', 'reSubmit', 'cancle']
#         self.current_state = 'A'
#         self.transitions = []

#     def add_transition(self, start, end, trigger, action, attributes=None):
#         self.transitions.append((start, end, trigger, action, attributes))

#     def execute_transition(self, trigger):
#         for transition in self.transitions:
#             if transition[2] == trigger:
#                 self.current_state = transition[1]
#                 transition[3]()
#                 break



class SalesToProduce(WFclass.ApprovalProcess):
    def __init__(self):
        super().__init__()
        self.name = "Sales to Produce"
        self.description = "This workflow is used to track sales orders and produce products."
        self.icon = ":/icons/sales_to_produce.png"
        
        self.color = "#0099ff"
        
        # self.add_node("Start", "Start", "Start node", ":/icons/start.png")
        # self.add_node("Receive Sales Order", "Receive Sales Order", "Receive sales order from customer", ":/icons/receive_sales_order.png")
        # self.add_node("Create Purchase Order", "Create Purchase Order", "Create purchase order for products", ":/icons/create_purchase_order.png")
        # self.add_node("Receive Purchase Order", "Receive Purchase Order", "Receive purchase order from supplier", ":/icons/receive_purchase_order.png")
        # self.add_node("Produce Product", "Produce Product", "Produce product from purchase order", ":/icons/produce_product.png")
        # self.add_node("Ship Product", "Ship Product", "Ship product to customer", ":/icons/ship_product.png")
        # self.add_node("End", "End", "End node", ":/icons/end.png")
        
        self.add_transition("Start", "Receive Sales Order", "Receive sales order from customer", self.run)
        self.add_transition("Receive Sales Order", "Create Purchase Order", "Create purchase order for products", self.run)
        self.add_transition("Create Purchase Order", "Receive Purchase Order", "Receive purchase order from supplier", self.run)
        self.add_transition("Receive Purchase Order", "Produce Product", "Produce product from purchase order", self.run)
        self.add_transition("Produce Product", "Ship Product", "Ship product to customer", self.run)
        self.add_transition("Ship Product", "End", "End node", self.run)
        
    def run(self):
        pass
    
    def stop(self):
        pass
    
    def reject():
        pass

    def add_node(a,b,c,d):
        pass
    
    def apvl_launch(self, appvlLayout):
        # appvlWidget = QWidget()
        # appvlWidget.setGeometry(300, 150, 500, 900)
        # appvlWidget.setWindowIconText('销售订单生产审批')
        # appvlLayout = QVBoxLayout()
        # appvlWidget.setLayout(appvlLayout)
        # appvlLayout.addWidget(QLabel('销售订单生产审批'))
        
        appvl_form = QFormLayout()
        appvlLayout.addLayout(appvl_form)
        
        appvl_form.addRow(QLabel('销售订单编号：'), QLineEdit())
        appvl_form.addRow(QLabel('销售订单日期：'), QLineEdit())
        appvl_form.addRow(QLabel('客户名称：'), QLineEdit())
        appvl_form.addRow(QLabel('联系电话：'), QLineEdit())
        appvl_form.addRow(QLabel('收货地址：'), QLineEdit())
        appvl_form.addRow(QLabel('销售人员：'), QLineEdit())
        # appvl_form.addRow(QLabel('销售总额：'), QLineEdit())
        appvl_form.addRow(QLabel('备注：'), QTextEdit())
        
        appvl_form.addRow(QLabel('采购订单编号：'), QLineEdit())
        appvl_form.addRow(QLabel('采购订单日期：'), QLineEdit())
        appvl_form.addRow(QLabel('供应商名称：'), QLineEdit())
        appvl_form.addRow(QLabel('联系电话：'), QLineEdit())
        appvl_form.addRow(QLabel('收货地址：'), QLineEdit())
        appvl_form.addRow(QLabel('采购人员：'), QLineEdit())
        appvl_form.addRow(QLabel('采购总额：'), QLineEdit())
        appvl_form.addRow(QLabel('备注：'), QTextEdit())
        
        appvl_form.addRow(QLabel('生产订单编号：'), QLineEdit())
        appvl_form.addRow(QLabel('生产订单日期：'), QLineEdit())
        appvl_form.addRow(QLabel('生产人员：'), QLineEdit())
        appvl_form.addRow(QLabel('生产数量：'), QLineEdit())
        appvl_form.addRow(QLabel('生产备注：'), QTextEdit())
        