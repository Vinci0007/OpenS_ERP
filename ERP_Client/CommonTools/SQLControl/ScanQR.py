from pyzbar.pyzbar import decode
from PIL import Image
import json

image_path1 = 'Data/QR_Data/example.png'


def scan_qr_code(image_path):
    image = Image.open(image_path)
    decoded_objects = decode(image)
    product_data = []
    for obj in decoded_objects:
        # print("二维码类型:", obj.type)
        # print("二维码数据:", obj.data.decode('utf-8'))
        product_data.append(obj.data.decode('utf-8'))
    return product_data[0]


# data = json.loads(scan_qr_code(image_path1))
# data = scan_qr_code(image_path1)
# data1 = json.loads(data)
# print(data1)
# print(data['product_id'])
