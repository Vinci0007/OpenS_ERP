from users_manage import users_data_sql as usersds
from WareHouseData import ShowAllWarehouseData as sawh
from WareHouseData import WarehouseDataOperate as whdo

from flask import Flask, jsonify, request
import logging
# import requests

app = Flask(__name__)

@app.route('/')
def test_route():
    return 'connect success'

@app.route('/login_validation', methods = ['GET', 'POST'])
def login_validation():
    auth_token = request.headers.get('Authorization')
    # login_user = request.data.decode('utf-8')
    # username = request.form['username']
    # password = request.form['password']
    login_user = {
        'username': request.form.get('username'),
        'password': request.form.get('password')
    }
    logging.basicConfig(filename='server.log', level=logging.DEBUG,)
    logger = logging.getLogger('my_logger')
    logger.debug('Data: %s', login_user)
    login_state = usersds.validate_user(auth_token, login_user)   
    return login_state
    # return 'True'
  
@app.route('/find_user_with_username', methods = ['GET', 'POST'])  
def find_user_with_username():
    auth_token = request.headers.get('Authorization')
    login_username = request.form.get('username')
    login_userinfo = usersds.find_user_with_username(auth_token, login_username) 
    return login_userinfo

@app.route('/showAllWarehouseData', methods = ['GET', 'POST']) 
def showAllWarehouseData():
    # auth_token = request.headers.get('Authorization')
    login_username = request.form.get('username')
    allWarehouseData = sawh.showAllWarehouseData() 
    return allWarehouseData

@app.route('/saveWarehouseData', methods = ['GET', 'POST'])  
def saveWarehouseData():
    auth_token = request.headers.get('Authorization')
    # toSaveData = request.form()
    toSaveData = request.get_json()
    allWarehouseData = whdo.saveWarehouseData(auth_token, toSaveData) 
    return allWarehouseData

if __name__ == '__main__':
    # usersds.find_user_with_username('1324654', 'admin')
    # sawh.showAllWarehouseData() 
    # whData = '{"0": {"product_id": "fd", "product_name": "sdf", "product_type": "sdf", "supplier": "sdf", "isoutbound": "", "inbound_time": "2024-05-21 22:24:29", "outbound_time": "", "receive_time": "sdf", "price": "\\u65e0\\u6743\\u9650", "price_unit": "sdf", "quality": "1", "quality_unit": "dsf", "operator": "admin1101051091009720240501000159863", "productCheckID": "RZQOORL32J2FVRX3HPNPORG3RMVF5U5RZU6QJYZGLWTMBAGURCJA===="}}' 
    # whdo.saveWarehouseData('da5d', whData)
    app.run(host='0.0.0.0', port=5000, debug=True)  # 在所有网络接口上监听，端口为5000
    # usersds.find_user_with_username('1q3we165we','123')
    # usersds.validate_user('1q3we165we',{'username':'123',
    #                                       'password': '123'})
    