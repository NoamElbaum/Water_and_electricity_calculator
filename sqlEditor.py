import mysql.connector
from datetime import datetime

db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="rootroot",
    database="apartments"
)

cursor = db.cursor()


def addVal(table, wPrice, ePrice):
    waterNew = int(input('water: '))
    electricityNew = int(input('electricity: '))

    cursor.execute('select max(date) from ' + table)
    lastDate = cursor.fetchone()
    # print(lastDate)
    sqlDate = ''
    count = 0
    for i in str(lastDate):
        if i.isdigit():
            sqlDate += i
        elif i == ',':
            if count < 2:
                sqlDate += '-'
                count += 1

    cursor.execute("select water from " + table + " where date = " + "'" + sqlDate + "'")
    waterVal = cursor.fetchone()
    water = waterVal[0]
    cursor.execute("select electricity from " + table + " where date = " + "'" + sqlDate + "'")
    electricityVal = cursor.fetchone()
    electricity = electricityVal[0]
    # print(sqlDate)
    # print(electricity)
    # print(water)

    if water > waterNew or electricity > electricityNew:
        print('wrong values!!!!!!!!!')
        return False
    now = datetime.now()
    date = now.strftime("%Y-%m-%d")
    waterT = (waterNew - water) * wPrice
    elecT = int((electricityNew - electricity) * ePrice)
    lineVal = [f"'{date}'",
               str(waterNew),
               str(electricityNew),
               f"'({waterNew}-{water})*{wPrice} = {waterT}'",
               f"'({electricityNew}-{electricity})*{ePrice} = {elecT}'",
               str(waterT + elecT)]
    sql = 'insert into ' + table + ' values (' + lineVal[0] + ',' + lineVal[1] + ',' + lineVal[2] + ',' + lineVal[
        3] + ',' + lineVal[4] + ',' + lineVal[5] + ')'
    cursor.execute(sql)
    # print(sql)
    db.commit()
