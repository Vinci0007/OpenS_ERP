# This Python file uses the following encoding: utf-8
import os
from pathlib import Path
import sys
import requests

# from PySide6.QtWidgets import QApplication, QWidget, QPushButton, QLineEdit, QMainWindow
# # from PySide6.QtUiTools import loadUi
# from PySide6.QtCore import QFile
# from PySide6.QtUiTools import QUiLoader
from PyQt6 import QtWidgets, uic
from PyQt6.QtWidgets import QMessageBox, QPushButton, QPlainTextEdit, QLineEdit
from PyQt6.QtCore import Qt
from PyQt6.QtGui import QKeySequence, QAction, QPalette, QColor, QShortcut

try:
    current_file_path = os.path.abspath(__file__)
    addons_path = os.path.join(os.path.dirname(current_file_path), 'Addons')
    sys.path.append(addons_path)
    addons_path = os.path.join(os.path.dirname(current_file_path), 'CommonTools')
    sys.path.append(addons_path)
    addons_path = os.path.join(os.path.dirname(current_file_path), 'Pages')
    sys.path.append(addons_path)
except:
    pass

from CommonTools.UserMCommonTools import UsersLogin
from Addons.BaseAddons.MainWindow import MainWindow as mainw
from Addons.BaseAddons.MainWindow import Login_ui


# class ErpWidget(QtWidgets.QWidget):
class ErpWidget(QtWidgets.QWidget, Login_ui.Ui_ErpWidget):
    def __init__(self):
        super().__init__()
        self.username = ''
        self.password = ''
        self.current_window = self
        self.session_token = ''
        # self.palette = QPalette()
        self.setupUi(self)
        self.load_ui()
        self.resize(500,300)
        
        

    def load_ui(self):
        # uic.loadUi("Resource/ui/login.ui", self)
        login_button = self.findChild(QPushButton, "loginButton")
        login_button.setDefault(True)
        if login_button:
            login_button.clicked.connect(self.on_login_button_clicked)
            shortcut_main = QShortcut(QKeySequence(Qt.Key.Key_Return), login_button)  # 创建回车键的快捷键
            shortcut_main.activated.connect(login_button.click)  # 当快捷键触发时，模拟按钮点击
            shortcut_num = QShortcut(QKeySequence(Qt.Key.Key_Enter), login_button)  # 创建回车键的快捷键
            shortcut_num.activated.connect(login_button.click)  # 当快捷键触发时，模拟按钮点击
        else:
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Icon.Information)
            msg.setText("程序错误")
            msg.setWindowTitle("程序错误")
            msg.exec()
            
        # 将回车键绑定到按钮，以触发点击事件
        # self.setFocusPolicy(Qt.FocusPolicy.StrongFocus)
        # self.keyPressEvent = self.on_key_press_event()
           
        
    def set_login_info(self, login_username, login_password):
        self.username = login_username
        self.password = login_password
        

    def on_login_button_clicked(self):
        username_input = self.findChild(QLineEdit, "username")
        password_input = self.findChild(QLineEdit, "password")
        login_username = username_input.text()
        login_password = password_input.text()
        self.set_login_info(login_username, login_password)
        global login_state
        login_data = UsersLogin.login(login_username, login_password)
        self.session_token = login_data['auth_token']
        ####################################################
        ####        debug
        #####################
        self.username = 'admin'
        if True:
        ####################################################
        ####        debug
        #####################
        # if login_data['login_state']:
            self.show_login_success_dialog()
            self.current_window = self.openMainWin()
            # return login_state[1]
        else:
            # self.current_window = self.openMainWin()
            self.show_login_failed_dialog()
            # return {}
            
    def openMainWin(self):
        mainWin = mainw.MainWindow(self.username, self.session_token).current_window
        mainWin.show()
        self.close()
        return mainWin
    
    def show_login_success_dialog(self):
        msg = QMessageBox()
        msg.setIcon(QMessageBox.Icon.Information)
        msg.setText("登录成功！")
        msg.setWindowTitle("登录成功")
        msg.exec()        

    def show_login_failed_dialog(self):
        msg = QMessageBox()
        msg.setIcon(QMessageBox.Icon.Warning)
        msg.setText("登录失败，请检查用户名和密码。")
        msg.setWindowTitle("登录失败")
        msg.exec()
        
    def on_key_press_event(self, event):
        # 如果按下的是回车键，且焦点在按钮上，则触发按钮点击
        if event.key() == Qt.Key.Key_Return or event.key() == Qt.Key.Key_Enter:
            if isinstance(self.focusWidget(), QPushButton):
                # self.focusWidget().click()
                self.on_login_button_clicked()  # 模拟按钮点击事件
        else:
            super(QPushButton, self).keyPressEvent(event)
            
# def palette_control(self):
#     palette = QPalette()
#     palette.setColor(QPalette.ColorRole.Window, QColor(53, 53, 53))  # 主背景颜色
#     palette.setColor(QPalette.ColorRole.Window, Qt.GlobalColor.darkGray)  # 主背景颜色
#     palette.setColor(QPalette.ColorRole.WindowText, QColor(255, 255, 255))  # 文字颜色
#     palette.setColor(QPalette.ColorRole.Base, Qt.GlobalColor.lightGray)  # 主要元素背景
#     palette.setColor(QPalette.ColorRole.AlternateBase, QColor(53, 53, 53))  # 备用元素背景
#     palette.setColor(QPalette.ColorRole.ToolTipBase, QColor(255, 255, 255))
#     palette.setColor(QPalette.ColorRole.ToolTipText, QColor(255, 255, 255))
#     palette.setColor(QPalette.ColorRole.Text, Qt.GlobalColor.darkCyan)  # 用于LineEdit, TextView等的文字颜色
#     palette.setColor(QPalette.ColorRole.Button, Qt.GlobalColor.darkGray)
#     palette.setColor(QPalette.ColorRole.ButtonText, QColor(255, 255, 255))
#     palette.setColor(QPalette.ColorRole.BrightText, Qt.GlobalColor.red)
#     palette.setColor(QPalette.ColorRole.Link, QColor(42, 130, 218))
#     palette.setColor(QPalette.ColorRole.Highlight, QColor(42, 130, 218))
#     palette.setColor(QPalette.ColorRole.HighlightedText, QColor(0, 0, 0))
#     self.palette = palette
#     return palette

#####
##  python.exe -m PyQt6.uic.pyuic Weather.ui -o Weather.py
#####

# username = ''
# password = ''

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    show_window = ErpWidget().current_window        # 通过切换主窗口对象类型控制显示哪个窗口
    
    palette = QPalette()
    palette.setColor(QPalette.ColorRole.Window, Qt.GlobalColor.lightGray)
    palette.setColor(QPalette.ColorRole.Highlight, Qt.GlobalColor.cyan)
    palette.setColor(QPalette.ColorRole.Link, Qt.GlobalColor.cyan)
    

    app.setPalette(palette)
    
    #################
    ####     debug lines
    ###################
    # show_window = mainWindow.MainWindow().current_window
    ######    pip3 freeze > requirements.txt ########
    show_window.show()
    # mainWindow.load_mainWindow(app)
    # if not app:
    #     app.exec() 
    sys.exit(app.exec())   
