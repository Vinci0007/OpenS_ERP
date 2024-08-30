import pandas as pd
import os

from PyQt6.QtWidgets import QMessageBox

# BomPath = '../data/Bom/Test1_BOM.xlsx'
ProductName = ''
ProductNum = ''
WorkflowNum = ''
OderNum = ''
ProductBomData = []
sheet_name = 'testname'

def bomDataRead_FromExcle(bom_FilePath):
    if bom_FilePath == '' or bom_FilePath is None:
        msg = QMessageBox()
        msg.setIcon(QMessageBox.Icon.Critical)
        msg.setText("未选择 BOM 文件 !")
        msg.setWindowTitle("提示")
        msg.setStandardButtons(QMessageBox.StandardButton.Cancel)
        msg.setStandardButtons(QMessageBox.StandardButton.Ok)
        msg.exec()
        return False 
    _, ext = os.path.splitext(bom_FilePath)
    isExcleFile = ext.lower() in ('.xls', '.xlsx', '.xlsm', '.xlsb', '.csv')
    if not isExcleFile:
        msg = QMessageBox()
        msg.setIcon(QMessageBox.Icon.Critical)
        msg.setText("请选择 BOM 文件 !")
        msg.setWindowTitle("提示")
        msg.setStandardButtons(QMessageBox.StandardButton.Cancel)
        msg.setStandardButtons(QMessageBox.StandardButton.Ok)
        msg.exec()
        return False
    try:     
        # pandas reading Bom excle Data
        bomData = pd.read_excel(bom_FilePath, sheet_name=sheet_name, engine='openpyxl')
        row = 10
        column = 5
        elementsLen_Row = len(bomData.iloc[:,3])
        elementsLen_Column = len(bomData.iloc[4,:])
        for i in range(3,elementsLen_Row):
            ProductTypeNo = bomData.iloc[i, 3]
            ProductTypeName = bomData.iloc[i,4]
            ProductTypeVolume = bomData.iloc[i,7]
            ProductBomData.append([ProductTypeNo,ProductTypeName,ProductTypeVolume])
        return ProductBomData
    except:
        msg = QMessageBox()
        msg.setIcon(QMessageBox.Icon.Critical)
        msg.setText("请上传正确的BOM文件 !!")
        msg.setWindowTitle("提示")
        msg.setStandardButtons(QMessageBox.StandardButton.Cancel)
        msg.setStandardButtons(QMessageBox.StandardButton.Ok)
        msg.exec()
        return False
