from PyQt6 import QtWidgets, uic
from PyQt6.QtWidgets import QMessageBox, QPushButton, QLineEdit, QToolButton, QWidget, QMenuBar, QToolBar
from PyQt6.QtWidgets import QStyleFactory, QLabel, QTabWidget, QApplication, QGroupBox
from PyQt6.QtCore import Qt, QPoint
from PyQt6.QtGui import QKeySequence, QAction, QPalette, QColor

import sys, os
from datetime import datetime

# current_file_path = os.path.abspath(__file__)
# addons_path = os.path.join(os.path.dirname(current_file_path), 'PathToSys')

from CommonTools.Server_Client import client_functions as clientf
from Addons import menuWithButtonSet as mwbs
from Addons.BaseAddons.MainWindow import mainWindow_ui as mwui



class CustomMenuBar(QMenuBar):
    def __init__(self, parent=None):
        super().__init__(parent)
        self._parent = parent
        self.drag_position = None

    def mousePressEvent(self, event):
    # 鼠标按下事件，记录鼠标位置
        if event.button() == Qt.MouseButton.LeftButton and not self.activeAction():
            self.drag_position = event.globalPosition().toPoint()  # 修改这里
        else:
            super().mousePressEvent(event)

    def mouseDoubleClickEvent(self, event):
        # 双击最大化或还原窗口
        if event.button() == Qt.MouseButton.LeftButton and not self.activeAction():
            if self.parent().isMaximized():
                self.parent().showNormal()
            else:
                self.parent().showMaximized()
        else:
            super().mouseDoubleClickEvent(event)

    def mouseMoveEvent(self, event):
        # 鼠标移动时拖动窗口
        if event.buttons() == Qt.MouseButton.LeftButton and self.drag_position is not None:
            move_pos = event.globalPosition().toPoint() - self.drag_position
            self.parent().move(self.parent().pos() + move_pos)
            self.drag_position = event.globalPosition().toPoint()  # 修改这里
            event.accept()
        else:
            super().mouseMoveEvent(event)


class MainWindow(QtWidgets.QMainWindow, mwui.Ui_mainWindow):
# class MainWindow(QtWidgets.QMainWindow):
    def __init__(self, login_username, login_session_token):
        super().__init__()
        self.current_window = self
        self.login_username = login_username
        self.login_session_token = login_session_token
        # self.palette = QPalette()
        # uic.loadUi('Resource/ui/mainWindow.ui', self)
        self.setupUi(self)
        # self.setWindowTitle('ERP系统')
        self.setWindowFlag(Qt.WindowType.FramelessWindowHint)
        self.resize(1920, 1080)
        self.userinfo = clientf.find_user_with_username(self.login_username, self.login_session_token) #查询登录人员的信息数据
        self.create_elements_in_widget()
        # 设置应用程序风格为操作系统一致的风格
        # style_name = QStyleFactory.create('Fusion') if sys.platform == 'win32' else QStyleFactory.create('GTK+')
        # QApplication.setStyle(style_name)
                                  
    
    def create_elements_in_widget(self):
        # palette = self.palette()  
        self.customMenuBar = CustomMenuBar()
        # self.customMenuBar.setStyleSheet("font-size: 15px; border: none; QMenuBar::item {padding: 10px;}")
        self.customMenuBar.setStyleSheet("font-size: 15px; border: none;")
        self.toolbar = QToolBar()
        # self.menuBar.setPalette(palette)
        self.setMenuWidget(self.customMenuBar)
        
        mwbs.b_menus(self)
        
    def minimizeWindow(self):
        self.showMinimized()

    def maximizeWindow(self):
        if self.isMaximized():
            self.showNormal()
        else:
            self.showMaximized()
            
    def closeEvent(self, event):
        reply = QMessageBox.question(self, '警告',
            "确定退出吗?", QMessageBox.StandardButton.Yes | 
            QMessageBox.StandardButton.No | QMessageBox.StandardButton.Ignore)
        if reply == QMessageBox.StandardButton.Yes:
            event.accept()
        else:
            event.ignore()    
            
    def keyReleaseEvent(self, event):
        if event.key() == Qt.Key.Key_F1:
            self.showMaximized()
        elif event.key() == Qt.Key.Key_F2:
            self.showNormal()
        elif event.key() == Qt.Key.Key_F3:
            self.showMinimized()
        # elif event.key() == Qt.Key.Key_F4:
        #     self.close()
            
    # def palette_control(self):
    #     palette = QPalette()
    #     palette.setColor(QPalette.ColorRole.Window, QColor(53, 53, 53))  # 主背景颜色
    #     palette.setColor(QPalette.ColorRole.Window, Qt.GlobalColor.darkGray)  # 主背景颜色
    #     palette.setColor(QPalette.ColorRole.WindowText, QColor(255, 255, 255))  # 文字颜色
    #     palette.setColor(QPalette.ColorRole.Base, Qt.GlobalColor.lightGray)  # 主要元素背景
    #     palette.setColor(QPalette.ColorRole.AlternateBase, QColor(53, 53, 53))  # 备用元素背景
    #     palette.setColor(QPalette.ColorRole.ToolTipBase, QColor(255, 255, 255))
    #     palette.setColor(QPalette.ColorRole.ToolTipText, QColor(255, 255, 255))
    #     palette.setColor(QPalette.ColorRole.Text, QColor(255, 255, 255))  # 用于LineEdit, TextView等的文字颜色
    #     palette.setColor(QPalette.ColorRole.Button, Qt.GlobalColor.darkGray)
    #     palette.setColor(QPalette.ColorRole.ButtonText, QColor(255, 255, 255))
    #     palette.setColor(QPalette.ColorRole.BrightText, Qt.GlobalColor.red)
    #     palette.setColor(QPalette.ColorRole.Link, QColor(42, 130, 218))
    #     palette.setColor(QPalette.ColorRole.Highlight, QColor(42, 130, 218))
    #     palette.setColor(QPalette.ColorRole.HighlightedText, QColor(0, 0, 0))
    #     self.palette = palette
    #     return palette    



