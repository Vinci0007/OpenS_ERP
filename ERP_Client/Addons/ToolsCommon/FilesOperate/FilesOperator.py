import sys
from PyQt6.QtWidgets import QWidget, QFileDialog, QLabel

filePath = ''
def UpLoadFile():
    fileUploadWindow = QWidget()
    fileUploadWindow.setWindowTitle('上传文件')
    fileUploadWindow.setGeometry(300, 300, 400, 200)
    fileNameLabel = QLabel(fileUploadWindow)

    file_name, _ = QFileDialog.getOpenFileName(fileUploadWindow, '打开文件', '', '所有文件 (*);;文本文件 (*.txt)')
    if file_name:
            fileNameLabel.setText(f'已选择文件：{file_name}')
            global filePath
            filePath = file_name
            return filePath
    
def sendFilePathTo():
    if filePath is not None:
        return filePath
    else:
        return ''
