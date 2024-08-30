# from PyQt6.QtWidgets import QApplication, QLineEdit
# from PyQt6.QtCore import Qt

# class ClickToEditLineEdit(QLineEdit):
#     def __init__(self, *args, **kwargs):
#         super(ClickToEditLineEdit, self).__init__(*args, **kwargs)
#         # 设置初始的只读状态和样式
#         self.setReadOnly(True)
#         self.setDefaultStyle()

#     def mousePressEvent(self, event):
#         # 当鼠标单击输入框时
#         if self.isReadOnly():
#             self.setReadOnly(False)
#             # 输入框处于编辑状态时的样式
#             self.setStyleSheet("border: 1px solid black;")  # 根据需要调整边框样式
#         super(ClickToEditLineEdit, self).mousePressEvent(event)

#     def focusOutEvent(self, event):
#         # 当焦点离开输入框时
#         self.setReadOnly(True)
#         self.setDefaultStyle()
#         super(ClickToEditLineEdit, self).focusOutEvent(event)

#     def keyPressEvent(self, event):
#         # 当按下回车键时
#         if event.key() == Qt.Key_Return or event.key() == Qt.Key_Enter:
#             self.setReadOnly(True)
#             self.setDefaultStyle()
#         else:
#             super(ClickToEditLineEdit, self).keyPressEvent(event)

#     def setDefaultStyle(self):
#         # 默认样式，无边框，背景透明
#         self.setStyleSheet("border: none; background-color: transparent;")

# app = QApplication([])

# # 创建自定义的 QLineEdit
# editable_line_edit = ClickToEditLineEdit()
# editable_line_edit.show()

# app.exec_()