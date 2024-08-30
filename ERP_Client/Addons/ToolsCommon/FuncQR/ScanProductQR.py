
import time
import json

from PyQt6.QtWidgets import QMessageBox

from Addons.ToolsCommon.FuncQR import QRClientConfig as qrcc


if qrcc.isExist_ser_ClientQR:
    def scan_barcode(controlState):
        if controlState:
            ser = qrcc.ser_ClientQR
            if ser.in_waiting > 0:
                barcode = ser.readline().decode('utf-8').rstrip()
                # print(f"扫描结果: {barcode}")
            time.sleep(0.5)  # 延时0.5秒，降低CPU占用
            if barcode is not None:
                return barcode
            else:
                return None
        return None
else:
    pass
    # def scan_barcode(controlState):
        # print('无扫码设备， 请在请检查是否正确连接了扫码设备 ！')
        # QMessageBox.warning(None, "警告", "扫码功能错误或未安装 ！") 
        # if controlState:
        #     reData = {
        #         'warning':       'warning', 
        #     }
        #     data_json = json.dumps(reData)
        #     barcode = reData
        #     if qrcc.isSecretInfo == 'True':
        #         data_bytes = data_json.encode('utf-8')
        #         sercretData = qrcc.dataSecretCipherSuite.encrypt(data_bytes)
        #         barcode = sercretData
        #         time.sleep(1)
        #         return barcode
        # return None
        
        
        