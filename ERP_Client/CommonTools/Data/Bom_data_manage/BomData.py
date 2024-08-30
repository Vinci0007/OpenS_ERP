import pandas as pd

BomPath = '../data/Bom/Test1_BOM.xlsx'
ProductName = ''
ProductNum = ''
WorkflowNum = ''
OderNum = ''
ProductBomData = []



# 读取Excel文件
def read_excel(file_path, sheet_name):
    # 使用pandas的read_excel方法读取Excel文件
    data = pd.read_excel(file_path, sheet_name=sheet_name, engine='openpyxl')
    return data


file_path = BomPath  # 请替换为你的Excel文件路径
data = read_excel(file_path, sheet_name='分总成')
row = 10
column = 5
data1 = data.iloc[row-1, column-1]
elementsLen_Row = len(data.iloc[:,3])
elementsLen_Column = len(data.iloc[4,:])

for i in range(3,elementsLen_Row):
    ProductTypeNo = data.iloc[i, 3]
    # for y in elementsLen_Column:
    #     ProductTypeNo = data.iloc
    ProductTypeName = data.iloc[i,4]
    ProductTypeVolume = data.iloc[i,7]
    ProductBomData.append([ProductTypeNo,ProductTypeName,ProductTypeVolume])
#     print(i, ProductTypeNo, ProductTypeName)
#
#
# print(ProductBomData)
