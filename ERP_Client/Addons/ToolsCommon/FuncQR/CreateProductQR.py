import qrcode
import json

from Addons.ToolsCommon.FuncQR import QRClientConfig as qrcc

def single_create_product_QR():

    qr = qrcode.QRCode(
    version=1,
    error_correction=qrcode.constants.ERROR_CORRECT_L,
    box_size=10,
    border=4,
    )  
    # 设置二维码包含的数据
    # id = create_product_id(data)
    data = {
            # 'id':               '',
            'product_id':       'test-2024-test0007', 
            'product_type':     'test', 
            'product_name':     'test物料', 
            'supplier':         'test_sup', 
            # 'inbound_time':     '', 
            # 'outbound_time':    '', 
            'receive_time':     '20240520 - 17:00', 
            # 'price':            '10000', 
            'price_unit':       '￥', 
            'quality':          '1', 
            'quality_unit':     '个', 
            # 'operator':         '', 
            # 'productCheckID':   '', 
        }
    data_json = json.dumps(data)
    qrData = ''
    if qrcc.isSecretInfo == 'True':
        data_bytes = data_json.encode('utf-8')
        sercretData = qrcc.dataSecretCipherSuite.encrypt(data_bytes)
        qrData = sercretData
    else:
        qrData = data_json
    
    # sercretInfo = b(data_json)
    
    

    
    
    # data['product_id'] = id
    qr.add_data(qrData)
    qr.make(fit=True)
    
    # 创建图像
    img = qr.make_image(fill_color="black", back_color="white")

    # 保存图像为文件
    # img.save("Data/QR_Data/example.png")
    # img.save("TestDATA_FOLDER/QR_Data/example.png")
    
    

    qr = qrcode.QRCode(
    version=1,
    error_correction=qrcode.constants.ERROR_CORRECT_L,
    box_size=10,
    border=4,
    )  
    # 设置二维码包含的数据
    # id = create_product_id(data)
    data = {
            'product_type': 'test',
            'supplier': 'test_sup',
            'product_name': 'test_product',
            'price': '100',
            'quantity': '100',
            'description': 'test_description',
            'product_id': 'id',
        }
    data_json = json.dumps(data)
    
    data['product_id'] = id
    qr.add_data(data_json)
    qr.make(fit=True)
    
    # 创建图像
    img = qr.make_image(fill_color="black", back_color="white")

    # 保存图像为文件
    # img.save("Data/QR_Data/example.png")
    
def batch_create_product_QR(productData_excle):
    qr = qrcode.QRCode(
    version=1,
    error_correction=qrcode.constants.ERROR_CORRECT_L,
    box_size=10,
    border=4,
    )  
    # 设置二维码包含的数据
    # id = create_product_id(data)
    data = {
            'product_type': 'test',
            'supplier': 'test_sup',
            'product_name': 'test_product',
            'price': '100',
            'quantity': '100',
            'description': 'test_description',
            'product_id': 'id',
        }
    data_json = json.dumps(data)
    
    data['product_id'] = id
    qr.add_data(data_json)
    qr.make(fit=True)
    
    # 创建图像
    img = qr.make_image(fill_color="black", back_color="white")

    # 保存图像为文件
    img.save("Data/QR_Data/example.png")
    
    

    qr = qrcode.QRCode(
    version=1,
    error_correction=qrcode.constants.ERROR_CORRECT_L,
    box_size=10,
    border=4,
    )  
    # 设置二维码包含的数据
    # id = create_product_id(data)
    data = {
            'product_type': 'test',
            'supplier': 'test_sup',
            'product_name': 'test_product',
            'price': '100',
            'quantity': '100',
            'description': 'test_description',
            'product_id': 'id',
        }
    data_json = json.dumps(data)
    
    data['product_id'] = id
    qr.add_data(data_json)
    qr.make(fit=True)
    
    # 创建图像
    img = qr.make_image(fill_color="black", back_color="white")

    # 保存图像为文件
    img.save("Data/QR_Data/example.png")
    
#debug test    
# def create_product_id(productInfo):
    
#     return '132456789'
    
    
single_create_product_QR()    