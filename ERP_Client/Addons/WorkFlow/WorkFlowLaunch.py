
from Addons.WorkFlow.PresetWorkflows import SalesToProduce as salesTP

from PyQt6.QtWidgets import QLayout, QHBoxLayout, QVBoxLayout, QLabel, QWidget


def on_apvl_launch_Clicked(mainWindow, right_toolbar):
    funcPosition_label = right_toolbar.findChild(QLabel, 'funcPosition_label')
    funcPosition_label.setText(' 功能 -> 审批 -> 发起申请')
    create_launch_workflowUI(mainWindow)


def create_launch_workflowUI(mainWindow):
    centerWidget = QWidget()
    mainWindow.setCentralWidget(centerWidget)
    launchLayout = QVBoxLayout()
    centerWidget.setLayout(launchLayout)
    toolsLayout = QHBoxLayout()
    launchLayout.addLayout(toolsLayout)
    appvlLayout = QHBoxLayout()
    launchLayout.addLayout(appvlLayout)
    appvlLayout_left = QVBoxLayout()
    appvlLayout_right = QVBoxLayout()
    appvlLayout.addLayout(appvlLayout_left)
    appvlLayout.addLayout(appvlLayout_right)
    appvlLayout.addStretch()
    launchLayout.addStretch()
    
    SalesToProduce = salesTP.SalesToProduce()   
    SalesToProduce.apvl_launch(appvlLayout_left)
    
    pass