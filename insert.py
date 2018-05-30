import pandas as pd
import pymysql
import os

#file：导入的excel文件
def get_sql(file):
    #表单名称
    sheets = ("计费类型", "应用流水金额", "应用流水订单量", "应用流水人数", "分省分应用流水", "全国")
    # 表单对应数据库表名称
    tables = {sheets[0]: "application", sheets[1]: "m_amount", sheets[2]: "m_order",
              sheets[3]: "m_user", sheets[4]: "m_province", sheets[5]: "m_nationwide"}
    # 数据库字段对应表单列索引
    columns = {sheets[0]: "A:F", sheets[1]: "A,C,F:AC", sheets[2]: "A,C,F:AC",
               sheets[3]: "A,C,F:AC", sheets[4]: "A,B,D,G:L", sheets[5]: "A,C,F:K"}
    for sheet in sheets:
        sql = "insert ignore into {} values".format(tables[sheet])
        if sheets.index(sheet) >= 4:
            raw_data = pd.read_excel(io=file, sheet_name=sheet, header=1, usecols=columns[sheet])
        else:
            raw_data = pd.read_excel(io=file, sheet_name=sheet, header=0, usecols=columns[sheet])
        for index in raw_data.index:
            temp = tuple(raw_data.loc[index])
            sql += str(temp) + ","
        sql = sql[:-1] + ";"
        yield sql

#file：导入的excel文件
def insert_data(file):
    db = pymysql.connect(host="localhost", user="test", passwd="test123",
                         db="cmic_application_statistics", port=3306, charset="utf8")
    cursor = db.cursor()
    sql = get_sql(file)
    for str in sql:
        print(str)
        try:
            cursor.execute(str)
            db.commit()
        except:
            print("error")
            db.rollback()
    cursor.close()
    db.close()

while True:
    file = input("请输入文件名称：")
    if os.path.exists(file):
        insert_data(file=file)
        break
    else:
        print("文件不存在")

